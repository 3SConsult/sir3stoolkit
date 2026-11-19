# -*- coding: utf-8 -*-
"""
The guide for AI assistants that ships with sir3stoolkit: where it is, and making it findable.

AI assistant: before writing code against sir3stoolkit, read the guide for AI assistants - AGENTS.md next to
the installed sir3stoolkit/__init__.py (Initialize_Toolkit() logs its path when run by an AI assistant).
Without the installed package: https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md

- :func:`get_ai_guide_path` / :func:`get_ai_guide_url`: where the guide (``AGENTS.md`` plus the files in
  ``ai/`` next to it) of the installed version is.
- :func:`is_ai_agent`: whether the current process was started by an AI coding agent's tool call - then
  ``Initialize_Toolkit()`` logs the path of the guide (:func:`log_ai_hint_once`).
- :func:`ai_setup`: adds a short pointer to the guide to a project's ``AGENTS.md`` (and ``CLAUDE.md``),
  which AI coding agents load automatically. Command line: ``python -m sir3stoolkit ai-setup``.
"""

from __future__ import annotations

import importlib.metadata
import os
import re
from pathlib import Path
from typing import Optional

_PACKAGE_DIR = Path(__file__).resolve().parent
_GITHUB_RAW = "https://raw.githubusercontent.com/3SConsult/sir3stoolkit/{ref}/AGENTS.md"

HINT_ENV_VAR = "SIR3STOOLKIT_AI_HINT"
"""Environment variable overriding :func:`is_ai_agent`: ``1`` always shows the hint, ``0`` never."""

# Environment variables AI coding agents set in the shell their tool calls run in. Only variables set for
# the agent's own commands - not for terminals a human uses: CLAUDECODE (also set in VS Code terminals of
# the Claude Code extension), CURSOR_TRACE_ID (every Cursor terminal), CI (Cursor sets it too) and generic
# COPILOT_* prefixes are deliberately not used. Value None: any non-empty value.
# AI_AGENT is the emerging cross-tool convention (https://github.com/agentsmd/agents.md/issues/136), checked
# separately: any non-empty value except 0/false/no/off.
_AGENT_ENV_VARS: dict[str, Optional[str]] = {
    "CLAUDE_CODE_CHILD_SESSION": "1",  # Claude Code: Bash/PowerShell tool commands (v2.1.172+)
    "CODEX_THREAD_ID": None,           # OpenAI Codex CLI
    "CODEX_SANDBOX": None,             # OpenAI Codex CLI
    "CODEX_CI": None,                  # OpenAI Codex
    "GEMINI_CLI": "1",                 # Gemini CLI
    "CURSOR_AGENT": "1",               # Cursor agent terminal / cursor-agent CLI
    "COPILOT_AGENT": "1",              # GitHub Copilot agent mode in VS Code
    "COPILOT_CLI": None,               # GitHub Copilot CLI
    "OPENCODE": "1",                   # opencode
    "OPENCODE_CLIENT": None,           # opencode
    "CLINE_ACTIVE": None,              # Cline
}
_FALSE_VALUES = ("0", "false", "no", "off")

_BLOCK_BEGIN = "<!-- BEGIN sir3stoolkit - written by `python -m sir3stoolkit ai-setup`, re-run it to update -->"
_BLOCK_END = "<!-- END sir3stoolkit -->"
_BLOCK_RE = re.compile(r"<!-- BEGIN sir3stoolkit\b.*?<!-- END sir3stoolkit -->", re.DOTALL)
_BLOCK_BODY = """## sir3stoolkit (SIR 3S)

This project uses sir3stoolkit, the Python client for the SIR 3S pipe network simulation software
(3S Consult). Before writing or changing code that uses it, read sir3stoolkit's own guide for AI
assistants completely - a separate file, not this one: `AGENTS.md` in the installed sir3stoolkit
package folder (next to `sir3stoolkit/__init__.py`), matching the installed version. With this
project's Python interpreter,
`python -c "import os, sir3stoolkit; print(os.path.join(os.path.dirname(sir3stoolkit.__file__), 'AGENTS.md'))"`
prints its path; `Initialize_Toolkit()` also logs it when run by an AI assistant."""

_hint_logged = False


def _installed_version() -> Optional[str]:
    try:
        return importlib.metadata.version("sir3stoolkit")
    except importlib.metadata.PackageNotFoundError:
        return None


def get_ai_guide_path() -> Optional[Path]:
    """
    Returns the path of the guide for AI assistants (``AGENTS.md``) of the installed sir3stoolkit.

    :return: The ``AGENTS.md`` shipped in the installed package (its links point at the installed version);
        for an editable install of a repository checkout, the repository's ``AGENTS.md``; None if neither
        exists (then see :func:`get_ai_guide_url`).
    :rtype: Optional[pathlib.Path]
    """
    packaged = _PACKAGE_DIR / "AGENTS.md"
    if packaged.is_file():
        return packaged
    # editable install: <repo>/src/sir3stoolkit
    repo_root = _PACKAGE_DIR.parent.parent
    if _PACKAGE_DIR.parent.name == "src" and (repo_root / "pyproject.toml").is_file():
        candidate = repo_root / "AGENTS.md"
        if candidate.is_file():
            return candidate
    return None


def get_ai_guide_url() -> str:
    """
    Returns the GitHub URL of the guide for AI assistants (``AGENTS.md``) of the installed version.

    :return: The raw URL of ``AGENTS.md`` at the release tag of the installed version, or on ``main`` for
        a development version.
    :rtype: str
    """
    version = _installed_version()
    ref = f"v{version}" if version and re.fullmatch(r"\d+\.\d+\.\d+", version) else "main"
    return _GITHUB_RAW.format(ref=ref)


def get_ai_guide_location() -> str:
    """
    Returns where the guide for AI assistants is: the path from :func:`get_ai_guide_path`, otherwise the URL
    from :func:`get_ai_guide_url`.

    :rtype: str
    """
    path = get_ai_guide_path()
    return str(path) if path is not None else get_ai_guide_url()


def is_ai_agent() -> bool:
    """
    Returns whether the current process was most likely started by an AI coding agent's tool call.

    Checks environment variables that AI coding agents set for the commands they run: ``AI_AGENT`` (the
    emerging cross-tool convention, set e.g. by Claude Code and GitHub Copilot) and agent-specific ones
    (Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, opencode, Cline). Variables also set in
    terminals a human uses (e.g. ``CLAUDECODE``) are not used. ``SIR3STOOLKIT_AI_HINT=1`` / ``=0``
    overrides the detection, e.g. for an agent that isn't detected.

    :rtype: bool
    """
    override = os.environ.get(HINT_ENV_VAR, "").strip().lower()
    if override in ("1", "true", "yes", "on"):
        return True
    if override in _FALSE_VALUES:
        return False
    ai_agent = os.environ.get("AI_AGENT", "").strip().lower()
    if ai_agent and ai_agent not in _FALSE_VALUES:
        return True
    for name, expected in _AGENT_ENV_VARS.items():
        value = os.environ.get(name, "").strip()
        if value and (expected is None or value == expected):
            return True
    return False


def get_ai_hint() -> str:
    """Returns the one-line pointer to the guide that :func:`log_ai_hint_once` logs."""
    return ("AI assistant detected: before writing code against sir3stoolkit, read the guide for AI assistants "
            f"of the installed version completely: {get_ai_guide_location()} ({HINT_ENV_VAR}=0 hides this line).")


def log_ai_hint_once(log) -> bool:
    """
    Logs the pointer to the guide (:func:`get_ai_hint`) with ``log``, once per process and only if
    :func:`is_ai_agent` is True.

    :param log: Callable taking the message, e.g. a logger's ``info``.
    :return: True if the hint was logged by this call.
    :rtype: bool
    """
    global _hint_logged
    if _hint_logged or not is_ai_agent():
        return False
    _hint_logged = True
    log(get_ai_hint())
    return True


def _read_text(path: Path) -> tuple[str, str]:
    """Returns (text, newline) of an existing file, keeping its line endings."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    return text, ("\r\n" if "\r\n" in text else "\n")


def _write_text(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def _block(newline: str) -> str:
    return newline.join([_BLOCK_BEGIN, *_BLOCK_BODY.split("\n"), _BLOCK_END])


def _add_block(path: Path) -> str:
    if not path.exists():
        _write_text(path, _block("\n") + "\n")
        return "created"
    text, nl = _read_text(path)
    block = _block(nl)
    if _BLOCK_RE.search(text):
        new_text = _BLOCK_RE.sub(lambda _: block, text, count=1)
    else:
        new_text = text.rstrip("\r\n") + nl + nl + block + nl if text.strip() else block + nl
    if new_text == text:
        return "unchanged"
    _write_text(path, new_text)
    return "updated"


def _remove_block(path: Path) -> str:
    if not path.is_file():
        return "unchanged"
    text, nl = _read_text(path)
    if not _BLOCK_RE.search(text):
        return "unchanged"
    new_text = _BLOCK_RE.sub("", text, count=1)
    new_text = re.sub(r"(\r?\n){3,}", nl + nl, new_text).strip("\r\n")
    if not new_text.strip():
        path.unlink()  # only contained the block, e.g. created by ai_setup()
        return "removed (file deleted, was empty)"
    _write_text(path, new_text + nl)
    return "removed"


def _claude_md_files(project_dir: Path) -> list[Path]:
    """CLAUDE.md files of the project that need the block: Claude Code doesn't read AGENTS.md when a CLAUDE.md
    exists, unless it imports it (``@AGENTS.md``)."""
    files = [p for p in (project_dir / "CLAUDE.md", project_dir / ".claude" / "CLAUDE.md") if p.is_file()]
    if any(re.search(r"(^|\s)@(\./)?AGENTS\.md\b", _read_text(p)[0]) for p in files):
        return []
    return files


def ai_setup(project_dir: str | os.PathLike = ".", remove: bool = False) -> dict[str, str]:
    """
    Adds a short pointer to the guide for AI assistants to a project's ``AGENTS.md`` - and to its
    ``CLAUDE.md``, if it has one (Claude Code doesn't read ``AGENTS.md`` then) - so AI coding agents working
    in the project read the guide before writing code against sir3stoolkit.

    The pointer is a block between ``<!-- BEGIN sir3stoolkit ...`` and ``<!-- END sir3stoolkit -->``; running
    this again updates the block, the rest of the files stays as it is. ``AGENTS.md`` is created if missing.

    :param project_dir: The project's root folder. Default: the current folder.
    :type project_dir: str | os.PathLike
    :param remove: True removes the block again (a file that contained nothing else is deleted).
    :type remove: bool
    :return: Per file changed or checked: ``"created"``, ``"updated"``, ``"unchanged"``, ``"removed"`` or
        ``"removed (file deleted, was empty)"``.
    :rtype: dict[str, str]
    :raises ValueError: If ``project_dir`` is the folder of sir3stoolkit's own guide (its repository or the
        installed package folder) - the block would point at the file it is in.
    """
    project = Path(project_dir).resolve()
    if not project.is_dir():
        raise NotADirectoryError(f"Project folder not found: {project}")
    guide = get_ai_guide_path()
    if not remove and guide is not None and guide.resolve() == (project / "AGENTS.md").resolve():
        raise ValueError(f"{project} holds sir3stoolkit's own guide ({guide}) - run ai-setup in the folder of a "
                         "project that uses sir3stoolkit instead.")
    results: dict[str, str] = {}
    if remove:
        for path in (project / "AGENTS.md", project / "CLAUDE.md", project / ".claude" / "CLAUDE.md"):
            results[str(path)] = _remove_block(path)
        return results
    for path in [project / "AGENTS.md", *_claude_md_files(project)]:
        results[str(path)] = _add_block(path)
    return results
