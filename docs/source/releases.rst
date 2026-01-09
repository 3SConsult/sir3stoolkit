Releases
========

The SIR 3S Toolkit will first be released alongside SIR 3S version 90-15 Quebec, under the version 90.15.2. 
Between major SIR 3S releases, the Toolkit may receive interim updates to fix bugs or extend functionality.

There are two types of updates:

1. **Python-only updates** - Install via:

   .. code-block:: bash

      pip install --upgrade sir3stoolkit

2. **Core updates with DLL changes** - Requires manual replacement of ``Sir3S_Toolkit.dll`` in the SirGraf directory after pip upgrade (1). The newest version of the ``Sir3S_Toolkit.dll`` is shipped alongside the updated pure python code.    


The release notes indicate whether a version includes changes to the C# side and therefore if (2) is necessary. 

90-15 Quebec
------------

Version 90.15.7 (TO BE RELEASED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Improvements
^^^^^^^^^^^^
- dataframes.py: metadata renamed to model data


Version 90.15.6
~~~~~~~~~~~~~~~

For SIR 3S Version: 90-15-00-20-Upd1

C# Changes
^^^^^^^^^^

- Hydraulic Profile related functions added

Improvements
^^^^^^^^^^^^

- dataframes.py
   - generate_element_results_dataframe() returns float values instead of object type
   - new method: add_interior_points_to_results_dataframe() to transform result df into vectorized result df with additonal multi index
   - new method: generate_element_dataframe() to generate basic dfs with metadata and result values of components
   - new method: generate_longitudinal_section_dataframes() to generate dfs for longitudinal sections

- plotting.py
   - plot_pipe_layer() and plot_node_layer() introduced as new functions for network color depictions

Version 90.15.5
~~~~~~~~~~~~~~~

For SIR 3S Version: 90-15-00-19

C# Changes
^^^^^^^^^^

- Model Repair Class added

Bug Fixes
^^^^^^^^^^

- dataframes.py: 
   - logger.error(f"[metadata] Error occured while filtering with filter_container_tks.") no longer triggers unwarranted
   - logger.info(f"[metadata] {len(used_cols)} non-empty end node columns were created.") no longer triggers unwarranted

Improvements
^^^^^^^^^^^^

- alternative_models.py: 
   - SIR_3S_to_nx_graph() now created minimal graph with additional properties
   - add_properties_to_graph() new function for user defined addition of properties (metadata and result) to nx Graph
- dataframes.py:
   - generate_element_metadata_dataframe(geometry=True) returns gpd.GeoDataFrame instead of pd.DataFrame
   - generate_element_metadata_dataframe() and generate_element_result_dataframe() now have paramter tks to give a list which tks of the element type to include.
   - new function get_EPSG() returns tuple of SRID, SRID2, SRIDSTRING for crs
   - new function generate_hydraulic_edge_dataframe() returns a pandas dataframe containing all hydraulic edges of a model (eg. pipes, valves, compressors, etc.)

Version 90.15.4
~~~~~~~~~~~~~~~

- For SIR 3S Version: 90-15-00-19
- Implementation of Higher level functions (mantle):
   - alternative_models.py
      - nx graphs
      - pandapipes
   - dataframes.py
      - metadata dfs 
      - result dfs
   - mantle.py: collector for above modules
- Mantle Import fixed: mantle dependencies no longer needed, when importing sir3stoolkit

Version 90.15.3 (Initial Release)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- First official public release of the SIR 3S Toolkit (for SIR 3S Version: 90-15-00-16)
- Introduced core wrapping API for SIR 3S object model (nodes, pipes, etc.)
- Compatible with SIR 3S 90-15 Quebec (requires Sir3S_Toolkit.dll)
- Included example workflows and basic simulation access
