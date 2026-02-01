
Application Examples
====================

Here, you will find a variety of tutorials, examples and networks. 
Before proceeding, ensure that the SIR 3S Toolkit is properly installed (see :ref:`Installation instructions <installing-toolkit-label>`). 

The tutorials are designed to help new users to get started with the basic functionalities of the SIR 3S Toolkit.
The application examples build on that foundation and demonstrate how the SIR 3S Toolkit can be used in real-world scenarios.
The included networks illustrate typical topologies of SIR 3S models.

.. tip::

   📘 Are you new to the SIR 3S Toolkit? Start with the Tutorials below.

   ⚙️ Looking for practical scenarios? Jump to the Examples section.

   🧭 Interested in model topologies? Explore the Networks.


Tutorials
---------

These tutorials are designed to introduce new users to the functionalities of the SIR 3S Toolkit. Each class holding functions has its own section of tutorials. The section come in pairs of wrapper classes and their respective pure python mantle class.

Each tutorial is available for **previewing** as a rendered notebook.

Some tutorials are available **downloading** as a `.zip` archive containing all required files.

.. _Ttu1-49:

SIR3S_Model
~~~~~~~~~~~

SIR3S_Model() implements basic functionalities regarding interactions between Python and a SIR 3S model.

You can also download all tutorials regarding SIR3S_Model (0 - 49) and their respective data in a joint `.zip` archive at once `here <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorials000-049_Assets.zip>`_.

.. _Ttu000:

Tutorial 0: Importing and initialization of the SIR 3S Toolkit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tutorial demonstrates how to import the SIR 3S Toolkit and initialize instances of its classes.

View: `Notebook <tutorials/SIR3S_Model/Tutorial000_Assets/ToolkitTutorial000.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial000_Assets.zip>`_.

.. _Ttu001:

Tutorial 1: Creating a new or opening an existing SIR 3S model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tutorial demonstrates how to create new SIR 3S models or open already existing ones.

View: `Notebook <tutorials/SIR3S_Model/Tutorial001_Assets/ToolkitTutorial001.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial001_Assets.zip>`_.

.. _Ttu002:

Tutorial 2: Accessing and modifying model data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tutorial demonstrates how to get and set values of objects based on their topological key (tk).

View: `Notebook <tutorials/SIR3S_Model/Tutorial002_Assets/ToolkitTutorial002.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial002_Assets.zip>`_.

.. _Ttu003:

Tutorial 3: Accessing simulation results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tutorial demonstrates how to get result values of objects based on their tk.

View: `Notebook <tutorials/SIR3S_Model/Tutorial003_Assets/ToolkitTutorial003.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial003_Assets.zip>`_.

.. _Ttu004:

Tutorial 4: Editing a SIR 3S model safely and effectively
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Tutorial demonstrates how to change SIR 3S models properly by grouping changes and saving them.

View: `Notebook <tutorials/SIR3S_Model/Tutorial004_Assets/ToolkitTutorial004.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial004_Assets.zip>`_.

.. _Ttu005:

Tutorial 5: Insert and Connect Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Tutorial demonstrates how new elements such as nodes, pipes, tanks, valves, etc. can be inserted into a SIR 3S model and connected.

View: `Notebook <tutorials/SIR3S_Model/Tutorial005_Assets/ToolkitTutorial005.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial005_Assets.zip>`_.

.. _Ttu006:

Tutorial 6: Tables
^^^^^^^^^^^^^^^^^^

This Tutorial demonstrates how to work with tables.

View: `Notebook <tutorials/SIR3S_Model/Tutorial006_Assets/ToolkitTutorial006.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial006_Assets.zip>`_.

.. _Ttu007:

Tutorial 7: Groups
^^^^^^^^^^^^^^^^^^

This Tutorial demonstrates how to obtain the tks of objects that are part of a Group (Layer) and to change which objects are part of which groups.

View: `Notebook <tutorials/SIR3S_Model/Tutorial007_Assets/ToolkitTutorial007.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial007_Assets.zip>`_.

.. _Ttu008:

Tutorial 8: Miscellaneous
^^^^^^^^^^^^^^^^^^^^^^^^^^

This Tutorial demonstrates miscellaneous functions of the SIR3S_Model() class that cannot be assigned to one of the previous Tutorial topics.

View: `Notebook <tutorials/SIR3S_Model/Tutorial008_Assets/ToolkitTutorial008.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial008_Assets.zip>`_.

.. _Ttu50-99:

SIR3S_Model_Mantle
~~~~~~~~~~~~~~~~~~

SIR3S_Model_Mantle() is a collector class that contains the functions from all other classes defined in the mantle. As of now the model data for these tutorials is not publicly available (internal: T:\SCRATCH\Jablonski\Toolkit).

.. _Ttu50-59:

Tutorial 50: Mantle Import
^^^^^^^^^^^^^^^^^^^^^^^^^^

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial050.html>`_ | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial050.ipynb>`.

SIR3S_Model_Dataframes
^^^^^^^^^^^^^^^^^^^^^^

SIR3S_Model_Dataframes() implements interactions between SIR 3S and pandas dataframes. You can obtain pandas dfs with meta- or resultdata, insert nodes and pipes via a df, etc.

.. _Ttu051:

Tutorial 51: Manual Creation of Element Dataframes
""""""""""""""""""""""""""""""""""""""""""""""""""

This Example demonstrates the capabilities of the class Dataframes_SIR3S_Model that extends SIR3S_Model be abilities to work directley with pandas dataframes. It is shown how to create dataframes containing information about elements such as Nodes, Pipes, etc. existing in a SIR 3S Model. The methods presented are manual, user-defined and detailed. For creating more general dataframes with less input necessary, see Tutorial 52.   

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial051.html>`_ | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial051.ipynb>`.

.. _Ttu052:

Tutorial 52: General Creation of Element Dataframes
"""""""""""""""""""""""""""""""""""""""""""""""""""

This Example demonstrates the capabilities of the class Dataframes_SIR3S_Model that extends SIR3S_Model be abilities to work directley with pandas dataframes. It is shown how to create dataframes containing information about elements such as Nodes, Pipes, etc. existing in a SIR 3S Model. The methods presented are not user-defined and neither efficient, but get you the most important information quickly. For more detailed methods of creating dataframes, see Tutorial 51.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial052.html>`_ | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial052.ipynb>`.

.. _Ttu053:

Tutorial 53: General Non-Element Dataframes
"""""""""""""""""""""""""""""""""""""""""""

This Example demonstrates the capabilities of the class Dataframes_SIR3S_Model that extends SIR3S_Model be abilities to work directley with pandas dataframes. It is shown how to create dataframes containing information that does not concern individual elements types such as Nodes, Pipes, etc. but instead concerning more abstract SIR 3S data such as longitudinal sections or concatenations of multiple element types like hydraulic edges.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial053.html>`_ | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial053.ipynb>`.

.. _Ttu60-69:

SIR3S_Model_Alternative_Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SIR3S_Model_Alternative_Models() implements the generation of SIR 3S models in alternative model formats such as pandapipes or nx-Graphs.

.. _Ttu061:

Tutorial 61: nx-Graph
"""""""""""""""""""""

This Tutorial demonstrates how to create a nx-Graph from a SIR 3S model.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial061.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial061.ipynb>`.

.. _Ttu062:

Tutorial 62: pandapipes
"""""""""""""""""""""""

This Tutorial demonstrates how to create a pandapipes model from a SIR 3S model.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial062.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial062.ipynb>`.

.. _Ttu70-79:

SIR3S_Model_Plotting
^^^^^^^^^^^^^^^^^^^^

SIR3S_Model_Plotting implements general plotting functions for SIR 3S applications.

.. _Ttu071:

Tutorial 71: Time Curves
""""""""""""""""""""""""

This Tutorial demonstrates how to plot time curves.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial071.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial071.ipynb>`.

.. _Ttu072:

Tutorial 72: WORK IN PROGRESS: agsn
"""""""""""""""""""""""""""""""""""

This Tutorial demonstrates how to plot time curves.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial072.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial072.ipynb>`.

.. _Ttu073:

Tutorial 73: Network Color Depiction
""""""""""""""""""""""""""""""""""""

This example demonstrates how to plot network color depictions (ncd).

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial073.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial073.ipynb>`.

.. _Ttu80-89:

SIR3S_Advanced_Operations
^^^^^^^^^^^^^^^^^^^^^^^^^

SIR3S_Advanced_Operations implements functions that extend the basic C# operations with more advanced operations to change a SIR 3S model.

.. _Ttu081:

Tutorial 81: Groups
""""""""""""""""""""""""""""""""""""

This example demonstrates how add, remove, set elements to groups.

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial081.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial081.ipynb>`.

.. _Ttu082:

SIR3S_Advanced_Operations implements functions that extend the basic C# operations with more advanced operations to change a SIR 3S model.

Tutorial 82: Measured Value Tables
""""""""""""""""""""""""""""""""""""

This example demonstrates how view, create, delete and edit measured variable tables (Sollwerttabellen).

View: `Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial082.html>`_  | Download: :download:`Notebook <tutorials/SIR3S_Model_Mantle/ToolkitTutorial082.ipynb>`.

.. 
   .. _Ttu100-149:

   SIR3S_View: 100 - 149
   ~~~~~~~~~~~~~~~~~~~~~

   .. _Ttu150-199:

   SIR3S_View_Mantle: 150 - 199
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. _Ttu200-249:

   SIR3S_ModelRepair: 200 - 249
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. _Ttu250-299:

   SIR3S_ModelRepair_Mantle: 250 - 299
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Examples
--------

These examples are intended for users who are already familiar with the basic functionality of the SIR 3S Toolkit and demonstrate how to apply it to real-world scenarios.

Each example is available for both **viewing** and **downloading** as an `.ipynb` file. 

.. _Tex1:

Example 1: Shape Import
~~~~~~~~~~~~~~~~~~~~~~~

This Example demonstrates how to create a connected topological network of nodes and pipes in SIR 3S via teh SIR 3S Toolkit based on shapefile data. The data used comes from 'SIR 3S\Modelle\Beispiele\Wasser\Manual\Projektdaten\01 Shape-Dateien'.

View: `Notebook <examples/Toolkit_Example001.html>`_ | Download: :download:`Notebook <examples/Toolkit_Example001.ipynb>`.

.. _Tex2:

Example 2: Iterate over SIR 3S calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This Example demonstrates how to use the Dataframes_SIR3S_Model() class extending SIR3S_Model().

View: `Notebook <examples/Toolkit_Example002.html>`_ | Download: :download:`Notebook <examples/Toolkit_Example002.ipynb>`.

.. _TexX:

Example X: Template
~~~~~~~~~~~~~~~~~~~

.. admonition:: Contributor Template

   This is not a user-facing example but a template intended for contributors to create their own example.

View: `Notebook <examples/Toolkit_ExampleX.html>`_ | Download: :download:`Notebook <examples/Toolkit_ExampleX.ipynb>`.


Networks
--------

The networks are examples of SIR 3S model topologies.

Each network is available for **previewing** and **downloading** as an `.py` file. You can open and run it using the Python Console in SIR 3S.

.. _Tnw1:

Network 1
^^^^^^^^^

You can view the code below

.. toggle::

   .. literalinclude:: Networks/Network1.py
      :language: python
      :linenos:

You can download the Network file :download:`here <Networks/Network1.py>`.
