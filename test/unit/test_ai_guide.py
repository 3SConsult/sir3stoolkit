import importlib.util
from pathlib import Path

import pytest

from sir3stoolkit import ai_guide
from sir3stoolkit.__main__ import main as cli_main

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def no_agent_env(monkeypatch):
    for name in [ai_guide.HINT_ENV_VAR, "AI_AGENT", *ai_guide._AGENT_ENV_VARS]:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(ai_guide, "_hint_logged", False)


# --- guide location -------------------------------------------------------------------------------

def test_guide_path_in_repo_checkout_is_repo_agents_md():
    # tests run against src/ of the repository, which has no packaged copy
    assert ai_guide.get_ai_guide_path() == ROOT / "AGENTS.md"


def test_guide_path_prefers_packaged_copy(monkeypatch, tmp_path):
    (tmp_path / "AGENTS.md").write_text("# packaged", encoding="utf-8")
    monkeypatch.setattr(ai_guide, "_PACKAGE_DIR", tmp_path)
    assert ai_guide.get_ai_guide_path() == tmp_path / "AGENTS.md"


def test_guide_location_falls_back_to_url(monkeypatch, tmp_path):
    monkeypatch.setattr(ai_guide, "_PACKAGE_DIR", tmp_path / "site-packages" / "sir3stoolkit")
    assert ai_guide.get_ai_guide_path() is None
    assert ai_guide.get_ai_guide_location() == ai_guide.get_ai_guide_url()


@pytest.mark.parametrize("version, ref", [("90.15.27", "v90.15.27"), ("90.15.0.1.dev1", "main"), (None, "main")])
def test_guide_url_points_at_release_tag(monkeypatch, version, ref):
    monkeypatch.setattr(ai_guide, "_installed_version", lambda: version)
    assert ai_guide.get_ai_guide_url() == f"https://raw.githubusercontent.com/3SConsult/sir3stoolkit/{ref}/AGENTS.md"


def test_every_docstring_pointer_names_agents_md_and_a_link_for_agents_without_the_package():
    # agents reading the source on GitHub/PyPI or in a chat have no installed package to look into
    src = ROOT / "src" / "sir3stoolkit"
    files = [p for p in src.rglob("*.py") if "mcp" not in p.parts]
    pointers = 0
    for p in files:
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if line.lstrip().lstrip('"').startswith(("AI assistant:", "AI assistant writing code")):
                pointers += 1
                following = " ".join(lines[i:i + 4])
                where = f"{p.relative_to(ROOT)}:{i + 1}"
                assert "AGENTS.md" in following, f"{where}: pointer doesn't name AGENTS.md"
                assert "https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md" in following, \
                    f"{where}: pointer without the GitHub link"
                assert "ai-guide" not in following, f"{where}: refers to the removed ai-guide command"
    assert pointers >= 17


def test_guide_files_linked_from_agents_md_exist():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for rel in ("ai/tutorials.md", "ai/updates-and-issues.md"):
        assert f"]({rel})" in text
        assert (ROOT / rel).is_file()


# --- agent detection and hint ---------------------------------------------------------------------

def test_no_agent_detected_without_env(no_agent_env):
    assert ai_guide.is_ai_agent() is False


def test_claude_code_tool_call_detected(no_agent_env, monkeypatch):
    monkeypatch.setenv("CLAUDE_CODE_CHILD_SESSION", "1")
    assert ai_guide.is_ai_agent() is True


@pytest.mark.parametrize("value, expected", [("claude-code_2-1-318_agent", True), ("github_copilot_vscode_agent", True),
                                             ("0", False), ("false", False), ("", False)])
def test_ai_agent_convention(no_agent_env, monkeypatch, value, expected):
    monkeypatch.setenv("AI_AGENT", value)
    assert ai_guide.is_ai_agent() is expected


@pytest.mark.parametrize("name, value", [("CODEX_THREAD_ID", "abc"), ("GEMINI_CLI", "1"), ("CURSOR_AGENT", "1"),
                                         ("COPILOT_AGENT", "1"), ("CLINE_ACTIVE", "true")])
def test_other_agents_detected(no_agent_env, monkeypatch, name, value):
    monkeypatch.setenv(name, value)
    assert ai_guide.is_ai_agent() is True


@pytest.mark.parametrize("name", ["CLAUDECODE", "CURSOR_TRACE_ID", "CI"])
def test_human_terminal_variables_are_not_an_agent(no_agent_env, monkeypatch, name):
    monkeypatch.setenv(name, "1")
    assert ai_guide.is_ai_agent() is False


def test_claudecode_alone_is_not_an_agent(no_agent_env, monkeypatch):
    # also set in VS Code terminals of the Claude Code extension, i.e. for humans
    monkeypatch.setenv("CLAUDECODE", "1")
    assert ai_guide.is_ai_agent() is False


@pytest.mark.parametrize("value, expected", [("1", True), ("true", True), ("0", False), ("off", False)])
def test_env_override(no_agent_env, monkeypatch, value, expected):
    monkeypatch.setenv("CLAUDE_CODE_CHILD_SESSION", "0" if expected else "1")
    monkeypatch.setenv(ai_guide.HINT_ENV_VAR, value)
    assert ai_guide.is_ai_agent() is expected


def test_hint_logged_once_and_only_for_agents(no_agent_env, monkeypatch):
    messages = []
    assert ai_guide.log_ai_hint_once(messages.append) is False
    monkeypatch.setenv("CLAUDE_CODE_CHILD_SESSION", "1")
    assert ai_guide.log_ai_hint_once(messages.append) is True
    assert ai_guide.log_ai_hint_once(messages.append) is False
    assert len(messages) == 1
    assert str(ROOT / "AGENTS.md") in messages[0]
    # the hint must not look like an error to _log_message (which raises on "Error"/"Could not")
    assert not messages[0].lower().startswith(("error", "could not"))


def test_initialize_toolkit_logs_hint_for_agents(no_agent_env, monkeypatch, initialized_wrapper_factory, caplog):
    monkeypatch.setenv("CLAUDE_CODE_CHILD_SESSION", "1")
    with caplog.at_level("INFO"):
        initialized_wrapper_factory()
    assert any("AI assistant detected" in r.getMessage() for r in caplog.records)


@pytest.fixture
def initialized_wrapper_factory(monkeypatch, tmp_path):
    from sir3stoolkit.core import wrapper

    resolved_dir = tmp_path / "sirgraf"
    resolved_dir.mkdir()
    original_sys_path = list(wrapper.sys.path)
    original_sirgraf_dir = wrapper.SIR3S_SIRGRAF_DIR
    monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: str(resolved_dir))
    monkeypatch.setattr(wrapper.net, "AddReference", lambda *_: None)
    monkeypatch.setattr(wrapper, "_check_toolkit_dll_version", lambda *_: None)
    yield lambda: wrapper.Initialize_Toolkit(None)
    wrapper.sys.path[:] = original_sys_path
    wrapper.SIR3S_SIRGRAF_DIR = original_sirgraf_dir


# --- ai_setup -------------------------------------------------------------------------------------

def test_setup_creates_agents_md(tmp_path):
    result = ai_guide.ai_setup(tmp_path)
    assert result == {str(tmp_path / "AGENTS.md"): "created"}
    text = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert "`AGENTS.md` in the installed sir3stoolkit" in text and "ai-guide" not in text
    assert ai_guide.ai_setup(tmp_path) == {str(tmp_path / "AGENTS.md"): "unchanged"}


def test_setup_appends_to_existing_files_keeping_crlf(tmp_path):
    original = b"# My project\r\n\r\nOur rules.\r\n"
    (tmp_path / "AGENTS.md").write_bytes(original)
    (tmp_path / "CLAUDE.md").write_bytes(original)
    result = ai_guide.ai_setup(tmp_path)
    assert set(result.values()) == {"updated"}
    for name in ("AGENTS.md", "CLAUDE.md"):
        raw = (tmp_path / name).read_bytes()
        assert raw.startswith(original)
        assert b"\n" not in raw.replace(b"\r\n", b"")  # no bare LF
    # removing restores the original files
    ai_guide.ai_setup(tmp_path, remove=True)
    assert (tmp_path / "AGENTS.md").read_bytes() == original
    assert (tmp_path / "CLAUDE.md").read_bytes() == original


def test_setup_replaces_outdated_block(tmp_path):
    (tmp_path / "AGENTS.md").write_text(
        "intro\n\n<!-- BEGIN sir3stoolkit old -->\nold text\n<!-- END sir3stoolkit -->\n\noutro\n", encoding="utf-8")
    assert ai_guide.ai_setup(tmp_path)[str(tmp_path / "AGENTS.md")] == "updated"
    text = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert "old text" not in text
    assert text.count("<!-- BEGIN sir3stoolkit") == 1
    assert text.startswith("intro") and text.rstrip().endswith("outro")


def test_setup_skips_claude_md_importing_agents_md(tmp_path):
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    result = ai_guide.ai_setup(tmp_path)
    assert str(tmp_path / "CLAUDE.md") not in result
    assert (tmp_path / "CLAUDE.md").read_text(encoding="utf-8") == "@AGENTS.md\n"


def test_remove_deletes_file_that_only_held_the_block(tmp_path):
    ai_guide.ai_setup(tmp_path)
    result = ai_guide.ai_setup(tmp_path, remove=True)
    assert result[str(tmp_path / "AGENTS.md")].startswith("removed")
    assert not (tmp_path / "AGENTS.md").exists()


def test_setup_block_says_it_points_to_another_file(tmp_path):
    ai_guide.ai_setup(tmp_path)
    text = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert "a separate file, not this one" in text
    assert "sir3stoolkit.__file__" in text


def test_setup_refuses_the_folder_of_sir3stoolkits_own_guide(capsys):
    agents_md = (ROOT / "AGENTS.md").read_bytes()
    with pytest.raises(ValueError, match="own guide"):
        ai_guide.ai_setup(ROOT)
    assert cli_main(["ai-setup", str(ROOT)]) == 1
    assert "own guide" in capsys.readouterr().err
    assert (ROOT / "AGENTS.md").read_bytes() == agents_md


def test_setup_rejects_missing_folder(tmp_path):
    with pytest.raises(NotADirectoryError):
        ai_guide.ai_setup(tmp_path / "missing")


# --- command line ---------------------------------------------------------------------------------

def test_cli_ai_setup(tmp_path, capsys):
    assert cli_main(["ai-setup", str(tmp_path)]) == 0
    assert "created" in capsys.readouterr().out
    assert (tmp_path / "AGENTS.md").is_file()


# --- sync script of the release build -------------------------------------------------------------

def _load_sync_script():
    path = ROOT / ".github" / "actions" / "sync-agents-md" / "sync_agent_docs.py"
    spec = importlib.util.spec_from_file_location("sync_agent_docs", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sync_points_links_at_tag_and_exports_tutorials(tmp_path):
    sync = _load_sync_script()
    result = sync.sync(ROOT, tmp_path, "90.15.999")
    assert result["tutorials"] > 20
    agents = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert "ships with the installed sir3stoolkit 90.15.999" in agents
    assert "sir3stoolkit/main/CONTRIBUTING.md" in agents
    tutorials = (tmp_path / "ai" / "tutorials.md").read_text(encoding="utf-8")
    assert "/main/docs/source/tutorials" not in tutorials and "/v90.15.999/docs/source/tutorials" in tutorials
    t057 = (tmp_path / "ai" / "tutorials" / "ToolkitTutorial057.md").read_text(encoding="utf-8")
    assert "```python" in t057 and '"outputs"' not in t057


def test_sync_without_version_copies_unchanged(tmp_path):
    _load_sync_script().sync(ROOT, tmp_path, "")
    assert (tmp_path / "AGENTS.md").read_bytes() == (ROOT / "AGENTS.md").read_bytes()
    assert (tmp_path / "ai" / "tutorials.md").read_bytes() == (ROOT / "ai" / "tutorials.md").read_bytes()
