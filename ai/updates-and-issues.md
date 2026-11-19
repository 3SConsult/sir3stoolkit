# Updates and known issues — sir3stoolkit

Part of the sir3stoolkit guide for AI assistants - start with [`AGENTS.md`](../AGENTS.md). Read this
file when the user asks about updating / being current, or when behavior contradicts a tutorial or
docstring and looks like a genuine bug.

## Checking for updates

If relevant to what the user's asking (they mention updating, or ask if they're current) - not
something to check unconditionally every time - compare the installed version against the latest on
PyPI and tell them if they differ:

- Installed: `importlib.metadata.version("sir3stoolkit")`.
- Latest: https://pypi.org/pypi/sir3stoolkit/json (`info.version`) - needs network access; without it,
  just point the user at https://pypi.org/project/sir3stoolkit/ instead of guessing.

If they differ, check `docs/source/releases.rst`'s version-overview table
(https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/releases.rst) for whether
upgrading also needs a manual `Sir3S_Toolkit.dll` replacement in the SirGraf directory. The table's
`dll changed + file version` column is a per-version delta, not cumulative - OR that column across
*every* version strictly between the installed and target version, not just the target's own row
(e.g. 90.15.19 -> 90.15.21 needs a DLL update because .20 says "Yes", even though the logic can't
stop at just checking .21's row).
From 90.15.26 on, `Sir3S_Toolkit.dll` carries a file version (90.15.26: `90.15.10.0`; all earlier DLLs
report `1.0.0.0`), and that column also states it. So the DLL actually installed can be checked
directly instead of inferred: `wrapper.Get_Toolkit_Dll_File_Version()` returns the file version of the
DLL in the SirGraf directory (or of any DLL path passed); `Initialize_Toolkit()` logs it and warns if it
differs from the DLL shipped with the installed sir3stoolkit version (`lib/<version>/` in the package).
If that warning appears, the DLL needs replacing (or sir3stoolkit upgrading) before trusting results.
A new mantle dependency being required isn't reliably flagged in the changelog text - instead of
parsing prose for it, just try the actual import; a missing one raises a clear, actionable combined
`ImportError` naming what to `pip install` (see the dependency gotcha in `AGENTS.md`).

This is also worth doing unprompted, not just when asked about updates: if behavior contradicts a
tutorial or docstring and looks like a genuine bug rather than misuse, check the installed version
against `releases.rst`/the issues (same mechanics as above) before concluding it's user error - recent
point releases have fixed real result-correctness bugs, not just added features.

## Current known issues / roadmap

https://github.com/3SConsult/sir3stoolkit/issues to browse - but that's GitHub's rendered UI, not
reliably fetchable/parseable. If you have network access, use the REST API instead for clean
structured data (title, body, state, labels, comment count) without needing to parse a rendered page:
https://api.github.com/repos/3SConsult/sir3stoolkit/issues?state=open&per_page=100 (no auth needed,
public repo; add `state=all` to include closed/historical ones, or `per_page`/pagination for more than
100). Useful for "is this a known gap" context, not a substitute for the docstring on the specific
function you're calling.

If you're debugging something for the user and would normally check this but can't (no network,
rate-limited - unauthenticated GitHub API calls are capped at 60/hour per IP, easy to hit), say so
explicitly rather than silently skipping the check or guessing - the user can then check the page
themselves if it matters for what they're debugging. If rate-limited, don't loop-retry - it's an
hourly cap, retrying within the same session won't help.
