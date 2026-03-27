Releases
========

The SIR 3S Toolkit python package often receives updates including bug fixes or new functionalities.

There are two types of updates:

1. **Python-only updates** - Install via:

   .. code-block:: bash

      pip install --upgrade sir3stoolkit

   .. code-block:: bash

      pip install --upgrade sir3stoolkit==90.15.12 # for specific version

2. **Core updates with DLL changes** - Requires manual replacement of ``Sir3S_Toolkit.dll`` in the SirGraf directory after pip upgrade (1). The newest version of the ``Sir3S_Toolkit.dll`` is shipped alongside the updated pure python code.    


The release notes indicate whether a version includes changes to the C# side and therefore if (2) is necessary. 

SIR 3S: 90-15 Quebec
--------------------

.. _Overview:

Overview
^^^^^^^^

Below an overview over all Toolkit Versions for SIR 3S 90-15 Quebec is given. It is stated with which specific SIR 3S version the Toolkit version was developed and tested and whether replacing the Sir3S_Toolkit.dll is necessary.

+----------------+---------------------------+-------------+--------------+
| Toolkit Version| SIR 3S Version            | dll changed | Release Date |
+================+===========================+=============+==============+
| 90.15.16       | 90-15-00-24-Upd2          | No          | 2026-03-15   |
+----------------+---------------------------+-------------+--------------+
| 90.15.15       | 90-15-00-23-Upd2          | Yes         | 2026-03-03   |
+----------------+---------------------------+-------------+--------------+
| 90.15.14       | 90-15-00-22-Upd2          | No          | 2026-02-25   |
+----------------+---------------------------+-------------+--------------+
| 90.15.13       | 90-15-00-22-Upd2          | No          | 2026-02-20   |
+----------------+---------------------------+-------------+--------------+
| 90.15.12       | 90-15-00-22-Upd2          | Yes         | 2026-02-12   |
+----------------+---------------------------+-------------+--------------+
| 90.15.11       | 90-15-00-21-Upd2          | No          | 2026-02-08   |
+----------------+---------------------------+-------------+--------------+
| 90.15.10       | 90-15-00-21-Upd2          | No          | 2026-02-01   |
+----------------+---------------------------+-------------+--------------+
| 90.15.9        | 90-15-00-21-Upd2          | No          | 2026-01-25   |
+----------------+---------------------------+-------------+--------------+
| 90.15.8        | 90-15-00-20-Upd1          | No          | 2026-01-19   |
+----------------+---------------------------+-------------+--------------+
| 90.15.7        | 90-15-00-20-Upd1          | No          | 2026-01-10   |
+----------------+---------------------------+-------------+--------------+
| 90.15.6        | 90-15-00-20-Upd1          | Yes         | 2026-01-09   |
+----------------+---------------------------+-------------+--------------+
| 90.15.5        | 90-15-00-19               | Yes         | 2025-11-24   |
+----------------+---------------------------+-------------+--------------+
| 90.15.4        | 90-15-00-19               | No          | 2025-10-31   |
+----------------+---------------------------+-------------+--------------+
| 90.15.3 (Init) | 90-15-00-15               | Yes         | 2025-10-09   |
+----------------+---------------------------+-------------+--------------+

Below the release history with all changes is given in detail.

SIR 3S: 90-15-00-24-Upd2
^^^^^^^^^^^^^^^^^^^^^^^^

Version 90.15.17
""""""""""""""""

Changes
~~~~~~~

- dataframes.py:
   - new function: get_dataframes_from_nominal_diameter_tables()

Version 90.15.16
""""""""""""""""

Bug Fixes
~~~~~~~~~
- dataframes.py: get_dataframe_from_time_table() fixed importing float-valued time tables from SIR Graf
- dll files now included under src/sir3stoolkit/lib/ in every PyPI release

SIR 3S: 90-15-00-23-Upd2
^^^^^^^^^^^^^^^^^^^^^^^^

Version 90.15.15
""""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-23-Upd2

C# Changes
~~~~~~~~~~
- Deleting objects: References to the object are reset/handled.

Bug Fixes
~~~~~~~~~
- insert_dataframe_into_time_table():
   - Now works in addition with s3s.ObjectTypes.ThermalOutputTable" and s3s.ObjectTypes.TemperatureTable
   - ","-"." formatting issue for milliseconds Fixed
   - previous entries in table are deleted properly

SIR 3S: 90-15-00-22-Upd2
^^^^^^^^^^^^^^^^^^^^^^^^

Version 90.15.14
""""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-22-Upd2

Changes
~~~~~~~

- dataframes.py:
   - new function: add_interior_points_to_start_end_sequence(): turn column of a vectorized propertry in three columns: property_start(float), propertry_end(float), propertry_sequence(Tuple: start, ..., end)
   - generate_element_dataframe():
      - uses add_interior_points_to_start_end_sequence() to format vectorized result dataframe
      - new param: timestamp to determine for which timestamp result values should be obtained
      - end nodes only attempted to return if they are defined for element type: removes unnessesary warning 
   - generate_element_result_dataframe():
      - new param: drop_full_place_holder_columns:  Determine whether columns, that are completley filled with place holder values, get dropped.
   - deleted generate_pipe_vector_dataframe() and generate_longitudinal_section_vector_dataframes(), since handeling vectorized data is now built into lower level functions, therefore generate_element_dataframe(self.ObjectTypes.Pipe) also returns vectorized results.
   - generate_longitudinal_section_dataframes(): instead of lists of dataframes a list of size-2-tuples with Supply and Return is returned.

Version 90.15.13
""""""""""""""""

Changes
~~~~~~~

- All time table related functions moved from advanced_operations.py (SIR3S_Model_Advanced_Operations) to dataframes.py (SIR3S_Model_Dataframes)

Bug Fixes
~~~~~~~~~

- dataframes.py: logger(f"{e}"") without except fixed

Version 90.15.12
""""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-22-Upd2

C# Changes
~~~~~~~~~~
- Fixed Calculation Bug: Could not start Model Calculation: SirCalc Path 'C:\3S Consult\SIR3S-90-15-00-19-Quebec\SirCalc-90-15-02-20_Quebec\SirCalc.exe' not found

Bug Fixes
~~~~~~~~~
- insert_dataframe_into_time_table(): internal_ref_time = self.GetTimeStamps()[0][0]
- dataframes.py: generate_element_dataframe() minor safe guard added

Version 90.15.11
""""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-21-Upd2

- advanced_operations.py:
   - new function:
      - get_dataframes_from_time_table_type()
   - changed functions: 
      - insert_dataframe_into_measured_variable_table() changed to insert_dataframe_into_time_table()
      - get_dataframe_from_measured_variable_table() changed to get_dataframe_from_time_table()

SIR 3S: 90-15-00-21-Upd2
^^^^^^^^^^^^^^^^^^^^^^^^

Version 90.15.10
""""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-21-Upd2

- advanced_operations.py:
   - new functions: 
      - insert_dataframe_into_measured_variable_table()
      - get_dataframe_from_measured_variable_table()

Version 90.15.9
"""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-21-Upd2

- advanced_operations.py: new module with new class SIR3S_Model_Advanced_Operations()
   - new functions: 
      - set_group_elements()
      - add_elements_to_group()
      - remove_elements_from_group()
      - add_element_types_to_tk_list()
      - get_tks_of_group_elements()
      - get_element_type_from_tk()

SIR 3S: 90-15-00-20-Upd1
^^^^^^^^^^^^^^^^^^^^^^^^

Version 90.15.8
"""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-20-Upd1

- plotting.py  
   - new function: plot_time_curves()

- Fix: SIR_3S_to_nx_graph(): generate_hydraulic_edge_dataframe() renamed to generate_edge_dataframe() + datatype fix

Version 90.15.7
"""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-20-Upd1

Changes
~~~~~~~
- dataframes.py: 
   - metadata renamed to model_data
   - hydraulic_edge renamed to edge
   - add_interior_points_to_results_dataframe renamed to add_interior_points_as_multiindex()
   - new function: add_interior_points_as_flat_cols()
   - new function: generate_longitudinal_section_vector_dataframes()
   - new function: generate_pipe_vector_dataframe()

Version 90.15.6
"""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-20-Upd1

C# Changes
~~~~~~~~~~

- Hydraulic Profile related functions added

Improvements
~~~~~~~~~~~~

- dataframes.py
   - generate_element_results_dataframe() returns float values instead of object type
   - new method: add_interior_points_to_results_dataframe() to transform result df into vectorized result df with additonal multi index
   - new method: generate_element_dataframe() to generate basic dfs with metadata and result values of components
   - new method: generate_longitudinal_section_dataframes() to generate dfs for longitudinal sections

- plotting.py
   - plot_pipe_layer() and plot_node_layer() introduced as new functions for network color depictions

Changes
~~~~~~~

- mantle sub classes renaming:
   - from Alternative_Models_SIR3S_Model to SIR3S_Model_Alternative_Models
   - from Dataframes_SIR3S_Model to SIR3S_Model_Dataframes
   - from Plotting_SIR3S_Model to SIR3S_Model_Plotting

SIR 3S: 90-15-00-19
^^^^^^^^^^^^^^^^^^^

Version 90.15.5
"""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-19

C# Changes
~~~~~~~~~~

- Model Repair Class added

Bug Fixes
~~~~~~~~~~

- dataframes.py: 
   - logger.error(f"[metadata] Error occured while filtering with filter_container_tks.") no longer triggers unwarranted
   - logger.info(f"[metadata] {len(used_cols)} non-empty end node columns were created.") no longer triggers unwarranted

Improvements
~~~~~~~~~~~~

- alternative_models.py: 
   - SIR_3S_to_nx_graph() now created minimal graph with additional properties
   - add_properties_to_graph() new function for user defined addition of properties (metadata and result) to nx Graph
- dataframes.py:
   - generate_element_metadata_dataframe(geometry=True) returns gpd.GeoDataFrame instead of pd.DataFrame
   - generate_element_metadata_dataframe() and generate_element_result_dataframe() now have paramter tks to give a list which tks of the element type to include.
   - new function get_EPSG() returns tuple of SRID, SRID2, SRIDSTRING for crs
   - new function generate_hydraulic_edge_dataframe() returns a pandas dataframe containing all hydraulic edges of a model (eg. pipes, valves, compressors, etc.)

Version 90.15.4
"""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-19
- Implementation of Higher level functions (mantle):
   - alternative_models.py
      - nx graphs
      - pandapipes
   - dataframes.py
      - metadata dfs 
      - result dfs
   - mantle.py: collector for above modules
- Mantle Import fixed: mantle dependencies no longer needed, when importing sir3stoolkit

SIR 3S: 90-15-00-15
^^^^^^^^^^^^^^^^^^^

Version 90.15.3 (Initial Release)
"""""""""""""""""""""""""""""""""

Developed and tested using SIR 3S Version: 90-15-00-15

- First official public release of the SIR 3S Toolkit
- Introduced core wrapping API for SIR 3S object model (nodes, pipes, etc.)
- Compatible with SIR 3S 90-15 Quebec (requires Sir3S_Toolkit.dll)
- Included example workflows and basic simulation access
