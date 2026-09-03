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

## Read the tutorials and docstrings before writing code

The tutorial notebooks under `docs/source/tutorials/` (also rendered in the docs site) are worked,
runnable examples of realistic multi-step workflows — start there rather than composing calls from
scratch. There are two separate tutorial folders, matching the architecture above:

- `docs/source/tutorials/SIR3S_Model/` (Tutorials 000-010) — the `core` API (`SIR3S_Model`).
- `docs/source/tutorials/SIR3S_Model_Mantle/` (Tutorials 050+) — the `mantle` layer
  (`SIR3S_Model_Mantle`), built on top of core.

Together with the docstring on the function you're about to call, these are also the up-to-date
source for behavior quirks and known bugs in the currently released toolkit version — several are
called out directly at the point they matter (a note in a tutorial cell, or in a function's own
docstring). Read both before assuming standard behavior; don't rely on this file for that, since bugs
noted here would go stale fast and duplicate what's already maintained at the source.

### Tutorial index

Each entry links the raw notebook plus its docs-page source (`examples.rst`, line-ranged to that
tutorial's section - the same file for every entry, just a different range), then leads with the
operation/goal the tutorial teaches (match this against what the user actually asked for - they'll
describe a goal, not a function name) followed by the functions it calls, in order of first use (not
exhaustive of what's available). Low-maintenance to keep current - re-derive if a tutorial's
number/scope or the operation it teaches changes.

**`SIR3S_Model/` — core API**

- **[000](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial000_Assets/ToolkitTutorial000.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L20-L28)) How to import and initialize the toolkit against a SirGraf installation, including persisting
  the install path so you don't have to pass it every time. — `Initialize_Toolkit`,
  `Write_SirGraf_Config_Path`, `Read_SirGraf_Config_Path`, `SIR3S_Model()`, `SIR3S_View()`.
- **[001](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial001_Assets/ToolkitTutorial001.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L29-L37)) How to create a brand-new SIR 3S model or open an existing one. — `AllowSirMessageBox`,
  `NewModel`, `GetNetworkType`, `CloseModel`, `OpenModel`, `OpenModelXml`.
- **[002](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial002_Assets/ToolkitTutorial002.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L38-L46)) How to read and change any element's data by its tk (topological key) - properties, geometry,
  saving changes. — `GetTksofElementType`, `GetTkFromIDReference`, `GetObjectTypeof_Key`,
  `GetPropertiesofElementType`, `GetValue`, `GetGeometryInformation`, `GetGeometryData`, `SetValue`,
  `SetGeometryInformation`, `SaveChanges`, `CloseModel`.
- **[003](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial003_Assets/ToolkitTutorial003.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L47-L55)) How to run a calculation and read its results - single values, all timestamps, min/max over
  time. — `ExecCalculation`, `GetResultValue`, `GetResultProperties_from_elementType`,
  `GetResultProperties_from_elementKey`, `GetCurrentTimeStamp`, `GetTimeStamps`,
  `SetCurrentTimeStamp`, `GetResultfortimestamp`, `GetResultforAllTimestamp`, `GetMinResult`,
  `GetMaxResult`, `GetMinResult_for_timestamp`, `GetMaxResult_for_timestamp`.
- **[004](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial004_Assets/ToolkitTutorial004.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L56-L64)) How to make multiple changes to a model safely, grouped into one undoable
  Transaction/EditSession. — `StartTransaction`, `EndTransaction`, `StartEditSession`,
  `EndEditSession`, `RefreshViews`.
- **[005](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial005_Assets/ToolkitTutorial005.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L65-L73)) How to add new elements (nodes, pipes, valves, ...) to a model and connect them to each other.
  — `InsertElement`, `ConnectConnectingElementWithNodes`, `ConnectBypassElementWithNode`,
  `GetMainContainer`, `IsMainContainer`, `GetNumberOfElements`, `DeleteElement`, `AddNewNode`,
  `AddNewPipe`, `AddNewConnectingElement`, `AddNewBypassElement`, `GetEndNodes`, `GetElementInfo`.
- **[006](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial006_Assets/ToolkitTutorial006.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L74-L82)) How to read a SIR 3S table (e.g. a characteristic curve) into Python and add rows to it. —
  `GetTableRows`, `AddTableRow` (for time tables specifically, see mantle Tutorial054's
  `insert_dataframe_into_time_table`/`get_dataframes_from_time_table_type`).
- **[007](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial007_Assets/ToolkitTutorial007.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L83-L91)) How to move elements between groups, or assign a newly created element straight to a group. —
  `InsertElement` + group assignment via `SetValue` (for higher-level group operations, see mantle
  Tutorial081).
- **[008](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial008_Assets/ToolkitTutorial008.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L92-L100)) Grab-bag of things that don't fit the other tutorials: hydraulic-profile data, the log file
  location, suppressing console output, suppressing SIR DB popups. — `GetHydraulicProfileObjectString`,
  `GetCourseOfHydraulicProfile`, `SetLogFilePath`, `EnableOrDisableOutputComments`,
  `AllowSirMessageBox` (see Known gotchas above for why this one matters for unattended runs).
- **[009](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial009_Assets/ToolkitTutorial009.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L101-L109)) How to run SIR 3S's own model-validation check for errors/inconsistencies before calculating.
  — `ExecuteModelValidation`.
- **[010](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial010_Assets/ToolkitTutorial010.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L110-L118)) How to configure a calculation (type, time frame, thermal settings, working directory) and
  inspect/edit the generated XML calc file. — `GetDBSourcePath`, `GetWorkingDirectory`,
  `AllocateWorkingDirectory`, `CreateWorkingDirectory`, `GetCalculationType`, `SetCalculationType`,
  `GetSimulationTimeFrame`, `SetSimulationTimeFrame`, `GetThermalCalculationParemeters`,
  `SetThermalCalculationParemeters`, `WriteSirCalcXmlFile`, `CopyWorkingDirectory`.

**`SIR3S_Model_Mantle/` — mantle layer**

- **[050](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial050_Assets/ToolkitTutorial050.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L131-L139)) How to initialize the mantle layer (the pandas-DataFrame-based API) on top of core. —
  `SIR3S_Model_Dataframes()`/`SIR3S_Model_Mantle()`.
- **[051](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial051_Assets/ToolkitTutorial051.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L140-L148)) How to build a pandas DataFrame of model data or calculation results for one element type
  (nodes, pipes, ...), by hand, property by property. — `generate_element_model_data_dataframe`,
  `generate_element_results_dataframe`, `add_interior_points_to_start_end_sequence`,
  `convert_rows_to_single_tuple_row`.
- **[052](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial052_Assets/ToolkitTutorial052.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L149-L157)) How to build the same kind of element DataFrame more generically, without listing properties
  by hand. — `generate_element_dataframe`.
- **[053](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial053_Assets/ToolkitTutorial053.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L158-L166)) How to build a DataFrame that isn't per-element-type - a longitudinal section along a path, or
  all edges (pipes/valves/...) at once. — `generate_edge_dataframe`,
  `generate_longitudinal_section_dataframes`.
- **[054](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial054_Assets/ToolkitTutorial054.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L167-L175)) How to view, create, edit and delete rows of a time-varying table (e.g. a measured-variable/
  Sollwert table) via a DataFrame. — `insert_dataframe_into_time_table`,
  `get_dataframes_from_time_table_type`.
- **[055](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial055_Assets/ToolkitTutorial055.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L176-L184)) How to run the same model multiple times with different valve positions/operational-status
  data and compare the results. — `generate_edge_dataframe`, `generate_element_dataframe`,
  `plot_node_layer`, `plot_pipe_layer`.
- **[056](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial056_Assets/ToolkitTutorial056.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L185-L193)) How to look up standard nominal-diameter (DN) tables as a DataFrame. —
  `get_dataframes_from_nominal_diameter_tables`.
- **[061](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial061_Assets/ToolkitTutorial061.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L194-L202)) How to export a model as a networkx graph, for graph-based analysis. — `SIR_3S_to_nx_graph`,
  `add_properties_to_graph`.
- **[062](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial062_Assets/ToolkitTutorial062.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L203-L211)) How to export a model as a pandapipes network, e.g. to cross-check against SIR 3S's own
  results. — `SIR_3S_to_pandapipes`.
- **[071](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial071_Assets/ToolkitTutorial071.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L212-L220)) How to plot a result property's value over time for one or more elements. — `plot_time_curves`.
- **[072](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial072_Assets/ToolkitTutorial072.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L221-L229)) WORK IN PROGRESS - how to plot values along a longitudinal section (a path through the
  network). — `generate_longitudinal_section_dataframes`, `add_interior_points_as_multiindex`.
- **[073](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial073_Assets/ToolkitTutorial073.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L230-L238)) How to plot a network-wide color-coded map of a result property (a network color depiction).
  — `plot_node_layer`, `plot_pipe_layer`.
- **[081](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial081_Assets/ToolkitTutorial081.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L239-L246)) How to add, remove, or wholesale replace a group's elements. — `get_tks_of_group_elements`,
  `remove_elements_from_group`, `add_elements_to_group`, `add_element_types_to_tk_list`,
  `set_group_elements`.

## Known gotchas (durable, not tied to a specific bug/version)

- **Running unattended (e.g. as an agent), watch for blocking SIR DB message-box popups** — e.g.
  opening a model created in an older SIR 3S version pops up a migration-confirmation dialog and
  hangs waiting for a click that will never come. Another typical pop-up is model is currently used by another process(read only access). Call `AllowSirMessageBox(bAllow=False)` beforehand
  to suppress these (see Tutorial008); note this also means missing out on deeper error messages, so
  it's not recommended for normal interactive use. If you should provide Code for the user to run, do not use this option unless explicitly stated by user or pop up issues arise. This is mainly useful if you should open the model while the user has the model open in his own UI.
- **`SaveChanges()` commits immediately and permanently**, independent of whether you later call
  `CloseModel(saveChangesBeforeClosing=False)`. Don't call it on exploratory/throwaway edits.
- `AddNewPipe`'s `dn` parameter is a **string** (e.g. `'100'`); `AddNewConnectingElement`'s `dn`
  parameter is a **float** (e.g. `100.0`) — different underlying .NET signatures despite the
  similar-sounding param.
- If an optional third-party dependency (e.g. `pyarrow`, `geopandas`, `shapely`, `pandapipes`) is
  missing, importing the relevant mantle module raises one combined, actionable `ImportError` naming
  what to `pip install` — read that message rather than debugging the underlying traceback.
- SetValue always takes Value as str regardless of the underlying field's type.

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
`dll changed` column is a per-version delta, not cumulative - OR that column across *every* version
strictly between the installed and target version, not just the target's own row (e.g. 90.15.19 ->
90.15.21 needs a DLL update because .20 says "Yes", even though the logic can't stop at just
checking .21's row).
A new mantle dependency being required isn't reliably flagged in the changelog text - instead of
parsing prose for it, just try the actual import; a missing one raises a clear, actionable combined
`ImportError` naming what to `pip install` (see the dependency gotcha above).

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

## Contributing to sir3stoolkit itself

Different audience from the above (using the package vs. changing it) — see
https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/CONTRIBUTING.md.
