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

Function lists below are what each notebook calls, in order of first use — not exhaustive of what's
available, but enough to pick the right tutorial for what you need. This index only records
titles/function names, not behavior, so it's low-maintenance to keep current; re-derive it if a
tutorial's number/scope changes.

**`SIR3S_Model/` — core API**

- **[000](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial000_Assets/ToolkitTutorial000.ipynb)** Importing and initialization of the SIR 3S Toolkit — `Initialize_Toolkit`,
  `Write_SirGraf_Config_Path`, `Read_SirGraf_Config_Path` (persist the SirGraf install path once so
  later `Initialize_Toolkit()` calls need no `basePath` argument), `SIR3S_Model()`, `SIR3S_View()`.
- **[001](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial001_Assets/ToolkitTutorial001.ipynb)** Creating a new or opening an existing model — `AllowSirMessageBox`, `NewModel`,
  `GetNetworkType`, `CloseModel`, `OpenModel`, `OpenModelXml`.
- **[002](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial002_Assets/ToolkitTutorial002.ipynb)** Accessing/modifying model data by tk — `GetTksofElementType`, `GetTkFromIDReference`,
  `GetObjectTypeof_Key`, `GetPropertiesofElementType`, `GetValue`, `GetGeometryInformation`,
  `GetGeometryData`, `SetValue`, `SetGeometryInformation`, `SaveChanges`, `CloseModel`.
- **[003](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial003_Assets/ToolkitTutorial003.ipynb)** Calculating and accessing results — `ExecCalculation`, `GetResultValue`,
  `GetResultProperties_from_elementType`, `GetResultProperties_from_elementKey`,
  `GetCurrentTimeStamp`, `GetTimeStamps`, `SetCurrentTimeStamp`, `GetResultfortimestamp`,
  `GetResultforAllTimestamp`, `GetMinResult`, `GetMaxResult`, `GetMinResult_for_timestamp`,
  `GetMaxResult_for_timestamp`.
- **[004](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial004_Assets/ToolkitTutorial004.ipynb)** Editing safely via Transactions/EditSessions — `StartTransaction`, `EndTransaction`,
  `StartEditSession`, `EndEditSession`, `RefreshViews`.
- **[005](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial005_Assets/ToolkitTutorial005.ipynb)** Inserting/connecting elements (nodes, pipes, valves, ...) — `InsertElement`,
  `ConnectConnectingElementWithNodes`, `ConnectBypassElementWithNode`, `GetMainContainer`,
  `IsMainContainer`, `GetNumberOfElements`, `DeleteElement`, `AddNewNode`, `AddNewPipe`,
  `AddNewConnectingElement`, `AddNewBypassElement`, `GetEndNodes`, `GetElementInfo`.
- **[006](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial006_Assets/ToolkitTutorial006.ipynb)** Working with tables — `GetTableRows`, `AddTableRow` (for time tables specifically, see
  mantle Tutorial054's `insert_dataframe_into_time_table`/`get_dataframes_from_time_table_type`).
- **[007](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial007_Assets/ToolkitTutorial007.ipynb)** Working with groups — `InsertElement` + group assignment via `SetValue` (for higher-level
  group operations, see mantle Tutorial081).
- **[008](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial008_Assets/ToolkitTutorial008.ipynb)** Miscellaneous (things that don't fit elsewhere) — `GetHydraulicProfileObjectString`,
  `GetCourseOfHydraulicProfile`, `SetLogFilePath`, `EnableOrDisableOutputComments`,
  `AllowSirMessageBox` (see Known gotchas above for why this one matters for unattended runs).
- **[009](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial009_Assets/ToolkitTutorial009.ipynb)** Model validation — `ExecuteModelValidation`.
- **[010](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model/Tutorial010_Assets/ToolkitTutorial010.ipynb)** Calculation settings (type, time frame, thermal, working directory, XML calc file) —
  `GetDBSourcePath`, `GetWorkingDirectory`, `AllocateWorkingDirectory`, `CreateWorkingDirectory`,
  `GetCalculationType`, `SetCalculationType`, `GetSimulationTimeFrame`, `SetSimulationTimeFrame`,
  `GetThermalCalculationParemeters`, `SetThermalCalculationParemeters`, `WriteSirCalcXmlFile`,
  `CopyWorkingDirectory`.

**`SIR3S_Model_Mantle/` — mantle layer**

- **[050](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial050_Assets/ToolkitTutorial050.ipynb)** Initializing the mantle model (`SIR3S_Model_Dataframes()`/`SIR3S_Model_Mantle()`).
- **[051](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial051_Assets/ToolkitTutorial051.ipynb)** Manual creation of element dataframes — `generate_element_model_data_dataframe`,
  `generate_element_results_dataframe`, `add_interior_points_to_start_end_sequence`,
  `convert_rows_to_single_tuple_row`.
- **[052](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial052_Assets/ToolkitTutorial052.ipynb)** General/generic element dataframe creation — `generate_element_dataframe`.
- **[053](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial053_Assets/ToolkitTutorial053.ipynb)** Longitudinal-section and edge dataframes — `generate_edge_dataframe`,
  `generate_longitudinal_section_dataframes`.
- **[054](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial054_Assets/ToolkitTutorial054.ipynb)** Time tables (measured-variable and similar) as dataframes —
  `insert_dataframe_into_time_table`, `get_dataframes_from_time_table_type`.
- **[055](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial055_Assets/ToolkitTutorial055.ipynb)** Comparing calculations across adjusted operational status data — `generate_edge_dataframe`,
  `generate_element_dataframe`, `plot_node_layer`, `plot_pipe_layer`.
- **[056](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial056_Assets/ToolkitTutorial056.ipynb)** Nominal diameter tables — `get_dataframes_from_nominal_diameter_tables`.
- **[061](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial061_Assets/ToolkitTutorial061.ipynb)** Exporting to an nx-Graph — `SIR_3S_to_nx_graph`, `add_properties_to_graph`.
- **[062](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial062_Assets/ToolkitTutorial062.ipynb)** Exporting to pandapipes — `SIR_3S_to_pandapipes` (note: SIR 3S's `PH` is gauge pressure,
  pandapipes' `pn_bar`/`p_bar` are absolute — the +1 bar atmospheric offset matters here).
- **[071](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial071_Assets/ToolkitTutorial071.ipynb)** Time curves — `plot_time_curves`.
- **[072](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial072_Assets/ToolkitTutorial072.ipynb)** WORK IN PROGRESS: longitudinal sections (plotting) — `generate_longitudinal_section_dataframes`,
  `add_interior_points_as_multiindex`.
- **[073](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial073_Assets/ToolkitTutorial073.ipynb)** Network color depiction (ncd) plots — `plot_node_layer`, `plot_pipe_layer`.
- **[081](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial081_Assets/ToolkitTutorial081.ipynb)** Groups (higher-level than core Tutorial007) — `get_tks_of_group_elements`,
  `remove_elements_from_group`, `add_elements_to_group`, `add_element_types_to_tk_list`,
  `set_group_elements`.

## Known gotchas (durable, not tied to a specific bug/version)

- **Running unattended (e.g. as an agent), watch for blocking SIR DB message-box popups** — e.g.
  opening a model created in an older SIR 3S version pops up a migration-confirmation dialog and
  hangs waiting for a click that will never come. Another typical pop-up is model is currently used by another process(read only access). Call `AllowSirMessageBox(bAllow=False)` beforehand
  to suppress these (see Tutorial008); note this also means missing out on deeper error messages, so
  it's not recommended for normal interactive use.
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
