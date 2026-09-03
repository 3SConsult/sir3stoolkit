# AGENTS.md — sir3stoolkit

Guidance for AI assistants writing code against **sir3stoolkit**, the Python client for SIR 3S
(pipe network simulation/analysis software by 3S Consult). If you were asked to "use sir3stoolkit"
to build/modify/read a SIR 3S model, start here.

## Architecture

- `sir3stoolkit.core.wrapper` — thin, low-level wrapper around the SIR 3S .NET Toolkit API
  (`SIR3S_Model` and friends: `OpenModel`, `SetValue`/`GetValue`, `AddNewNode`/`AddNewPipe`/...,
  `ExecCalculation`, `GetResultValue`, ...). One call ≈ one underlying API call.
- `sir3stoolkit.mantle` — higher-level convenience functions built on top of core (dataframes,
  advanced model-editing operations, plotting, alternative-model export). Prefer mantle functions
  when one exists for what you need; they handle validation/batching the core API doesn't.
- Everything is a method on (a subclass of) `SIR3S_Model` — instantiate once via
  `wrapper.Initialize_Toolkit(sirgraf_dir)` then `model = wrapper.SIR3S_Model()`, `model.OpenModel(...)`.

## Where to get the real API surface

Docstrings on the installed package are the ground truth for exact signatures/params/returns —
introspect them directly (`help(...)`, or just read the source under `core/` and `mantle/`) rather
than guessing. Full docs: https://3sconsult.github.io/sir3stoolkit/

For `GetValue`/`SetValue`/`GetResultValue` and friends, the *property name strings* and each element
type's OBJTYPE table code are opaque and must match exactly — use the generated reference:
https://3sconsult.github.io/sir3stoolkit/object_types_props_results_snippet_global_mapped.html
(machine-generated from the toolkit's own `ObjectTypes_TableNames`/`GetPropertiesofElementType()`/
`GetResultProperties_from_elementType()` — authoritative for the installed SIR 3S version).

## Read the tutorials and docstrings before writing code

The tutorial notebooks under `docs/source/tutorials/` (also rendered in the docs site) are worked,
runnable examples of realistic multi-step workflows — start there rather than composing calls from
scratch. Together with the docstring on the function you're about to call, they're also the
up-to-date source for behavior quirks and known bugs in the currently released toolkit version —
several are called out directly at the point they matter (a note in a tutorial cell, or in a
function's own docstring). Read both before assuming standard behavior; don't rely on this file for
that, since bugs noted here would go stale fast and duplicate what's already maintained at the source.

## Known gotchas (durable, not tied to a specific bug/version)

- **`SaveChanges()` commits immediately and permanently**, independent of whether you later call
  `CloseModel(saveChangesBeforeClosing=False)`. Don't call it on exploratory/throwaway edits.
- `AddNewPipe`'s `dn` parameter is a **string** (e.g. `'100'`); `AddNewConnectingElement`'s `dn`
  parameter is a **float** (e.g. `100.0`) — different underlying .NET signatures despite the
  similar-sounding param.
- If an optional third-party dependency (e.g. `pyarrow`, `geopandas`, `shapely`, `pandapipes`) is
  missing, importing the relevant mantle module raises one combined, actionable `ImportError` naming
  what to `pip install` — read that message rather than debugging the underlying traceback.

## Current known issues / roadmap

https://github.com/3SConsult/sir3stoolkit/issues — filter to open issues; several closed ones are
historical. Useful for "is this a known gap" context, not a substitute for the docstring on the
specific function you're calling.

## Contributing to sir3stoolkit itself

Different audience from the above (using the package vs. changing it) — see `CONTRIBUTING.md`.
