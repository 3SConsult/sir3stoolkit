# AGENTS.md — sir3stoolkit

Guidance for AI assistants writing code against **sir3stoolkit**, the Python client for SIR 3S
(pipe network simulation/analysis software by 3S Consult). If you were asked to "use sir3stoolkit"
to build/modify/read a SIR 3S model, start here.

**This file is the core of the guide - read all of it before writing code.** It is followed by
files in [`ai/`](ai/), read when needed:

- [`ai/tutorials.md`](ai/tutorials.md) - the full tutorial index (links, goals, functions per
  tutorial). Read it before writing code for a workflow - the [Tutorials](#tutorials) section below
  only lists topics.
- [`ai/updates-and-issues.md`](ai/updates-and-issues.md) - checking for updates (incl. whether a
  `Sir3S_Toolkit.dll` replacement is needed) and the known issues on GitHub. Read it when the user
  asks about updating, or when behavior looks like a genuine bug.

Sections: [Quick facts](#quick-facts) · [Architecture](#architecture) ·
[Where to get the real API surface](#where-to-get-the-real-api-surface) · [Tutorials](#tutorials) ·
[Known gotchas](#known-gotchas-durable-not-tied-to-a-specific-bugversion) ·
[Making this guide findable](#making-this-guide-findable-in-the-users-project) ·
[Contributing](#contributing-to-sir3stoolkit-itself)

## Quick facts

- **Windows only**: needs a local SIR 3S (SirGraf) installation with a valid license, accessed via
  pythonnet/.NET (`Sir3S_Toolkit.dll`). Without it nothing can run - code can only be written, not executed.
- **Versions**: sir3stoolkit 90.15.x targets SIR 3S 90-15 (Quebec); the third number is the toolkit's own
  release counter. Which SirGraf version each release was tested with, and whether it needs a new
  `Sir3S_Toolkit.dll`, is in the release notes (see [`ai/updates-and-issues.md`](ai/updates-and-issues.md)).
- **Imports**: `from sir3stoolkit.core import wrapper` (core: `wrapper.SIR3S_Model()`) and
  `from sir3stoolkit.mantle.mantle import SIR3S_Model_Mantle` (core + all mantle functions).
  `from sir3stoolkit.mantle import SIR3S_Model_Mantle` does not work - `sir3stoolkit.mantle` only
  exposes its submodules. The tutorials often instantiate a single mantle class instead (e.g.
  `SIR3S_Model_Dataframes` from `sir3stoolkit.mantle.dataframes`, `SIR3S_Model_Alternative_Models` from
  `sir3stoolkit.mantle.alternative_models`) - that works too; `SIR3S_Model_Mantle` combines all of them.
- **Core returns strings**: e.g. `GetValue` returns `(value, type name)`, both `str`. tks are always
  `str` (exception: `SIR_3S_to_nx_graph()` casts them to `int64`, see Known gotchas).
- **Mantle functions mostly log errors and return an empty DataFrame/graph** instead of raising - check
  `.empty` and the log. Core calls you make directly raise `wrapper.SIR3S_ToolkitError` (outside SirGraf).

## Architecture

- `sir3stoolkit.core.wrapper` — thin, low-level wrapper around the SIR 3S .NET Toolkit API
  (`SIR3S_Model` and friends: `OpenModel`, `SetValue`/`GetValue`, `AddNewNode`/`AddNewPipe`/...,
  `ExecCalculation`, `GetResultValue`, ...). One call ≈ one underlying API call.
- `sir3stoolkit.mantle` — higher-level convenience functions built on top of core (dataframes,
  advanced model-editing operations, plotting, alternative-model export). Prefer mantle functions
  when one exists for what you need; they handle validation/batching the core API doesn't.
- Everything is a method on (a subclass of) `SIR3S_Model` — instantiate once via
  `wrapper.Initialize_Toolkit(sirgraf_dir)` then `model = wrapper.SIR3S_Model()`, `model.OpenModel(...)`.
- The `src/sir3stoolkit/mcp/` folder in the GitHub repository is an unfinished MCP server draft: it
  is not usable, not part of the pip package, and not a way to drive SIR 3S - don't try to use or fix
  it; write Python against `core`/`mantle` instead.

## Where to get the real API surface

Docstrings on the installed package are the ground truth for exact signatures/params/returns —
introspect them directly (`help(...)`, or just read the source under `core/` and `mantle/`) rather
than guessing. Full docs: https://3sconsult.github.io/sir3stoolkit/ - its raw source,
https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/modules.rst, is the
class/method list plus a hand-curated API Index, but NOT the expanded docstring content (that's
`.. automodule::` directives Sphinx fills in at build time from the real .py docstrings) - go straight
to the source under `core/`/`mantle/` for that instead, same as above.

For `GetValue`/`SetValue`/`GetResultValue` and friends, the *property name strings* and each element
type's OBJTYPE table code are opaque and must match exactly — use the generated reference:
https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/object_types_props_results_snippet_global_mapped_with_descriptions.rst
(machine-generated from the toolkit's own `ObjectTypes_TableNames`/`GetPropertiesofElementType()`/
`GetResultProperties_from_elementType()` — authoritative for the installed SIR 3S version).

The same reference ships with the package and can be queried per element type, without an open model:
`SIR3S_Model_Dataframes.get_object_type_reference(s3s.ObjectTypes.Pipe)` (Tutorial051) returns `table_name`
(`"ROHR"`), `category` (connecting element, bypass element, table, signal model element, ... or
`"unknown"`), `create_with` (only methods shown to create a real instance of the type, e.g.
`["SIR3S_Model.AddNewPipe"]`, `["SIR3S_View.AddNewHouse"]` - `[]` means none is known, not that
`InsertElement` works), `insertable_in` (network types), `properties` (name → value type) and
`result_properties` (name → German `description`/`unit`). To query across all element types, read the
JSON itself (`{"notice": [...], "object_types": {...}}`, keyed by `ObjectTypes` member name):
`mantle/object_type_reference.json` in the installed package, or
https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/src/sir3stoolkit/mantle/object_type_reference.json.
Same caveat as the RST: at runtime, `GetPropertiesofElementType()`/`GetResultProperties_from_elementType()`
remain authoritative for the installed SIR 3S version.

## Tutorials

The tutorial notebooks are worked, runnable examples of realistic multi-step workflows — start there
rather than composing calls from scratch, and read the docstring of each function you call: both are
the up-to-date source for behavior quirks and known bugs (this guide deliberately doesn't duplicate
them).

**In the installed package, the code of every tutorial is next to this file as plain text:
`ai/tutorials/ToolkitTutorialNNN.md` (e.g. `ai/tutorials/ToolkitTutorial057.md`; markdown and code cells,
outputs left out) - of exactly the installed version, no download needed. Read these** instead of
fetching the notebooks. (A repository checkout has only the notebooks, see
[`ai/tutorials.md`](ai/tutorials.md).)

Topics, to match against the user's goal - the functions each tutorial uses are in
[`ai/tutorials.md`](ai/tutorials.md):

- **Core (`SIR3S_Model/`)**: 000 import/initialize, SirGraf path, DLL version · 001 create/open a
  model · 002 read/change element data by tk · 003 run a calculation, read results over time · 004
  transactions/edit sessions · 005 add and connect elements · 006 tables (e.g. characteristic curves)
  · 007 groups · 008 hydraulic profile, log file, raising vs. logging errors, console output, SIR DB
  popups · 009 model validation · 010 calculation settings, working directory, calc XML file.
- **Mantle (`SIR3S_Model_Mantle/`)**: 050 initialize mantle · 051 element DataFrames property by
  property, incl. results, and looking up an element type in the object type reference · 052 element DataFrames generically · 053 edge and longitudinal-section
  DataFrames · 054 time tables via DataFrames · 055 runs with different valve positions, compare
  results · 056 nominal-diameter (DN) tables · 057 fast bulk results from the result files · 061
  networkx export · 062 pandapipes export · 071 time-curve plots · 072 longitudinal-section plots
  (work in progress) · 073 network color map of a result property · 081 group elements.

## Known gotchas (durable, not tied to a specific bug/version)

- **Running unattended (e.g. as an agent), watch for blocking SIR DB message-box popups** — e.g.
  opening a model created in an older SIR 3S version pops up a migration-confirmation dialog and
  hangs waiting for a click that will never come. Another typical pop-up is model is currently used by another process(read only access). Call `AllowSirMessageBox(bAllow=False)` beforehand
  to suppress these (see Tutorial008); note this also means missing out on deeper error messages, so
  it's not recommended for normal interactive use. If you should provide Code for the user to run, do not use this option unless explicitly stated by user or pop up issues arise. This is mainly useful if you should open the model while the user has the model open in his own UI.
- **Errors while initializing the toolkit can come from an outdated `Sir3S_Toolkit.dll`** in the
  SirGraf directory (some sir3stoolkit versions need it replaced, see
  [`ai/updates-and-issues.md`](ai/updates-and-issues.md)) -
  e.g. `wrapper.SIR3S_Model()` failing with "Could not find .NET enum ...", or newer methods missing
  on the toolkit object. Before debugging further, check the `Initialize_Toolkit()` log: it warns if the
  DLL's file version differs from the one the installed sir3stoolkit ships with
  (`wrapper.Get_Toolkit_Dll_File_Version()` returns it; DLLs before sir3stoolkit 90.15.26 report
  `1.0.0.0`). The fix is copying `lib/<newest version>/Sir3S_Toolkit.dll` from the installed package
  into the SirGraf directory - tell the user rather than doing it unasked (it modifies their SIR 3S
  installation).
- **`SaveChanges()` commits immediately and permanently**, independent of whether you later call
  `CloseModel(saveChangesBeforeClosing=False)`. Don't call it on exploratory/throwaway edits.
- `AddNewPipe`'s `dn` parameter is a **string** (e.g. `'100'`); `AddNewConnectingElement`'s `dn`
  parameter is a **float** (e.g. `100.0`) — different underlying .NET signatures despite the
  similar-sounding param.
- If an optional third-party dependency (e.g. `pyarrow`, `geopandas`, `shapely`, `pandapipes`) is
  missing, importing the relevant mantle module raises one combined, actionable `ImportError` naming
  what to `pip install` — read that message rather than debugging the underlying traceback.
- SetValue always takes Value as str regardless of the underlying field's type.
- Property names: core `GetValue` ignores case (`"FkCont"` and `"Fkcont"` both work), but mantle
  functions match the names in `properties=[...]` exactly and leave out unknown ones with a warning
  (`"FkCont"` is dropped). Always use the exact spelling from the generated reference (`Fkcont`).
- `GetValue` formats decimal numbers with the Windows/.NET culture: `'1,25'` under e.g. `de-DE`, `'1.25'`
  under `en-US` - while `GetResultValue` uses a dot (`'6.002027'`) even under `de-DE`. So
  `float(GetValue(...)[0])` fails on comma locales; replace the comma before converting. `SetValue`
  accepts both `'1.25'` and `'1,25'`.
- Outside SirGraf, errors reported by the toolkit raise `wrapper.SIR3S_ToolkitError` (inside SirGraf,
  and for core calls made inside mantle methods, they are only logged and the call returns e.g.
  `None`/`'-1'`/`('', '')`). See `Set_Raise_On_Error` (Tutorial008). Not every invalid input is reported as an
  error by the toolkit, though - check what was actually stored (`GetValue`) and run
  `ExecuteModelValidation` before trusting a model built from scratch.
- The calculation status `EXSTAT` (GeneralSection result) is stored per timestamp - the stationary
  timestamp has the stationary calculation's status, the others the transient calculation's. Reading it
  once with `GetResultValue` right after a calculation only gives the stationary one; loop over all
  timestamps (Tutorial003). `ExecCalculation(waitForSirCalcToExit=True)` checks this itself.
- For new code reading interior-point results (`...VEC` properties like `PVEC`), use
  `generate_element_results_dataframe(..., vec_format="multiindex")`: one float32 column per interior
  point, exact values, much faster and smaller. The default `"str"` (tab-separated strings, 7
  significant digits) only exists for backwards compatibility (Tutorial057).
- `generate_element_results_dataframe(..., include_name_and_end_nodes=False)` leaves out the `name`/
  `end_nodes` column levels (columns: `tk`, `property`[, `interior points`]). Use it whenever you don't need
  them, especially on large models: they cost two API calls per element (~8 s for 68,000 pipes), while the
  `bulk=True` read itself takes ~0.1 s. `merge_model_data_and_results()` accepts results with or without them.
- `generate_edge_dataframe()` marks each row's element type in a column named `"element type"` (with a
  space), holding the `ObjectTypes` member name (`"Pipe"`, `"Valve"`, ...).
- `SIR_3S_to_nx_graph()` (Tutorial061) currently has known limitations - check whether these issues are
  still open before relying on it:
  - It builds an `nx.DiGraph`, which holds one edge per node pair: elements in parallel between the same
    two nodes (e.g. several consumers on one supply/return pair, parallel pipes) silently overwrite each
    other, so edges are missing - compare `G.number_of_edges()` with the number of edge elements
    ([#25](https://github.com/3SConsult/sir3stoolkit/issues/25)).
  - It fails (returns an empty graph) on a model without result files - calculate the model first
    ([#26](https://github.com/3SConsult/sir3stoolkit/issues/26)).
  - Node and edge tks in the graph are `int64`, not `str` as everywhere else.

## Making this guide findable in the user's project

AI assistants working in a project that merely *uses* sir3stoolkit don't load this file on their own
(`Initialize_Toolkit()` logs its path when run by an AI assistant). If the user wants their future AI
sessions to read it before writing any code, suggest `python -m sir3stoolkit ai-setup` (run in their
project folder): it adds a short pointer to the project's `AGENTS.md` (and `CLAUDE.md`, if there is
one). Don't run it unasked - it edits the user's project files.

## Contributing to sir3stoolkit itself

Different audience from the above (using the package vs. changing it) — see
https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/CONTRIBUTING.md.
