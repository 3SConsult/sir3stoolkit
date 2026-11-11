# Tutorial index — sir3stoolkit

Part of the sir3stoolkit guide for AI assistants - start with [`AGENTS.md`](../AGENTS.md) (quick facts,
architecture, known gotchas), then come here to pick the tutorial that matches the task.

The tutorial notebooks under `docs/source/tutorials/` (also rendered in the docs site) are worked,
runnable examples of realistic multi-step workflows — start there rather than composing calls from
scratch. There are two separate tutorial folders, matching the architecture (core vs. mantle):

- `docs/source/tutorials/SIR3S_Model/` (Tutorials 000-010) — the `core` API (`SIR3S_Model`).
- `docs/source/tutorials/SIR3S_Model_Mantle/` (Tutorials 050+) — the `mantle` layer
  (`SIR3S_Model_Mantle`), built on top of core.

## Reading a tutorial

**In the installed package (from 90.15.27 on), the cell sources of every tutorial are next to this
file as plain markdown: `tutorials/ToolkitTutorialNNN.md` (e.g. `tutorials/ToolkitTutorial057.md`) -
of exactly the installed version, readable offline. Prefer these.** (They are generated for the
package only; a repository checkout has just the notebooks.)

The `.ipynb` files are mostly JSON and stored outputs (Tutorial 57: 1.5 MB). To read just the cells
(Tutorial 57: ~7 KB), download the raw notebook and print its cell sources:

    python -c "import json,sys; [print(''.join(c['source'])+'\n') for c in json.load(open(sys.argv[1],encoding='utf-8'))['cells']]" ToolkitTutorial057.ipynb

Together with the docstring on the function you're about to call, these are also the up-to-date
source for behavior quirks and known bugs in the currently released toolkit version — several are
called out directly at the point they matter (a note in a tutorial cell, or in a function's own
docstring). Read both before assuming standard behavior; don't rely on the guide for that, since bugs
noted there would go stale fast and duplicate what's already maintained at the source.

## Index

Each entry links the raw notebook plus its docs-page source (`examples.rst`, line-ranged to that
tutorial's section - the same file for every entry, just a different range), then leads with the
operation/goal the tutorial teaches (match this against what the user actually asked for - they'll
describe a goal, not a function name) followed by the functions it calls, in order of first use (not
exhaustive of what's available). Low-maintenance to keep current - re-derive if a tutorial's
number/scope or the operation it teaches changes.

**`SIR3S_Model/` — core API**

- **[000](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model/Tutorial000_Assets/ToolkitTutorial000.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L20-L28)) How to import and initialize the toolkit against a SirGraf installation, including persisting
  the install path so you don't have to pass it every time, and checking the file version of the
  Sir3S_Toolkit.dll in it. — `Initialize_Toolkit`, `Get_Toolkit_Dll_File_Version`,
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
  location, raising vs. only logging toolkit errors, suppressing console output, suppressing SIR DB
  popups. — `GetHydraulicProfileObjectString`, `GetCourseOfHydraulicProfile`, `SetLogFilePath`,
  `Set_Raise_On_Error` (`SIR3S_ToolkitError`), `EnableOrDisableOutputComments`,
  `AllowSirMessageBox` (see Known gotchas in `AGENTS.md` for why this one matters for unattended runs).
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
  (nodes, pipes, ...), by hand, property by property - incl. looking up an element type's properties,
  result properties (with standard units), category and how to create it in the shipped object type
  reference. — `get_object_type_reference`, `generate_element_model_data_dataframe`,
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
- **[057](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial057_Assets/ToolkitTutorial057.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L194-L202)) How to read results quickly straight from the result files (bulk=True) instead of one API call per
  value, incl. the interior-point formats (str/multiindex) and merging them with model data, and how to read
  the time-curve result file of a model with two output factors. — `generate_element_results_dataframe`
  (`bulk`, `vec_format`, `output_factor`, `include_name_and_end_nodes`), `get_result_file_properties`,
  `merge_model_data_and_results`,
  `add_interior_points_to_start_end_sequence`, `convert_rows_to_single_tuple_row`.
- **[061](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial061_Assets/ToolkitTutorial061.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L203-L211)) How to export a model as a networkx graph, for graph-based analysis. — `SIR_3S_to_nx_graph`,
  `add_properties_to_graph`.
- **[062](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial062_Assets/ToolkitTutorial062.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L212-L220)) How to export a model as a pandapipes network, e.g. to cross-check against SIR 3S's own
  results. — `SIR_3S_to_pandapipes`.
- **[071](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial071_Assets/ToolkitTutorial071.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L221-L229)) How to plot a result property's value over time for one or more elements. — `plot_time_curves`.
- **[072](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial072_Assets/ToolkitTutorial072.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L230-L238)) WORK IN PROGRESS - how to plot values along a longitudinal section (a path through the
  network). — `generate_longitudinal_section_dataframes`, `add_interior_points_as_multiindex`.
- **[073](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial073_Assets/ToolkitTutorial073.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L239-L247)) How to plot a network-wide color-coded map of a result property (a network color depiction).
  — `plot_node_layer`, `plot_pipe_layer`.
- **[081](https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/docs/source/tutorials/SIR3S_Model_Mantle/Tutorial081_Assets/ToolkitTutorial081.ipynb)** ([docs page](https://github.com/3SConsult/sir3stoolkit/blob/main/docs/source/examples.rst#L248-L255)) How to add, remove, or wholesale replace a group's elements. — `get_tks_of_group_elements`,
  `remove_elements_from_group`, `add_elements_to_group`, `add_element_types_to_tk_list`,
  `set_group_elements`.
