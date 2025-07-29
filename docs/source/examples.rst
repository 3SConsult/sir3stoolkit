
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

These tutorials are designed to introduce new users to the basic functionalities of the SIR 3S Toolkit. 

Each tutorial is available for **previewing** as a rendered notebook and for **downloading** as a `.zip` archive containing all required files.

You can also download all tutorials and their respective data in a joint `.zip` archive at once `here <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial1-X_Assets.zip>`_.

.. _Ttu1:

Tutorial 1: Importing and initialization of the SIR 3S Toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial demonstrates how to import the SIR 3S Toolkit and initialize instances of its classes.

View: `Notebook <tutorials/Tutorial1_Assets/ToolkitTutorial1.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial1_Assets.zip>`_.

.. _Ttu2:

Tutorial 2: Creating a new or opening an existing SIR 3S model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial demonstrates how to create new SIR 3S models or open already existing ones.

View: `Notebook <tutorials/Tutorial2_Assets/ToolkitTutorial2.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial2_Assets.zip>`_.

.. _Ttu3:

Tutorial 3: Accessing and modifying model data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial demonstrates how to get and set values of objects based on their topological key (tk).

View: `Notebook <tutorials/Tutorial3_Assets/ToolkitTutorial3.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial3_Assets.zip>`_.

.. _Ttu4:

Tutorial 4: Accessing simulation results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial demonstrates how to get result values of objects based on their tk.

View: `Notebook <tutorials/Tutorial4_Assets/ToolkitTutorial4.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial4_Assets.zip>`_.

.. _Ttu5:

Tutorial 5: Editing a SIR 3S model safely and effectively
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This Tutorial demonstrates how to change SIR 3S models properly by grouping changes and saving them.

View: `Notebook <tutorials/Tutorial5_Assets/ToolkitTutorial5.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/Tutorial5_Assets.zip>`_.

.. _TtuX:

Tutorial X: Template
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Contributor template

   This is not a user-facing tutorial but a template intended for contributors to create their own tutorial.


View: `Notebook <tutorials/TutorialX_Assets/ToolkitTutorialX.html>`_ | Download: `ZIP archive <https://github.com/3SConsult/sir3stoolkit/releases/download/tutorial_assets/TutorialX_Assets.zip>`_.

Examples
--------

These examples are intended for users who are already familiar with the basic functionality of the SIR 3S Toolkit and demonstrate how to apply it to real-world scenarios.

Each example is available for both **viewing** and **downloading** as an `.ipynb` file. 

.. _Tex1:

Example 1: Shape Import
~~~~~~~~~~~~~~~~~~~~~~~

This Example demonstrates how to create a connected topological network of nodes and pipes in SIR 3S via teh SIR 3S Toolkit based on shapefile data. The data used comes from 'SIR 3S\Modelle\Beispiele\Wasser\Manual\Projektdaten\01 Shape-Dateien'.

View: `Notebook <examples/Toolkit_Example1.html>`_ | Download: :download:`Notebook <examples/Toolkit_Example1.ipynb>`.

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
~~~~~~~~~

You can view the code below

.. toggle::

   .. literalinclude:: Networks/Network1.py
      :language: python
      :linenos:

You can download the Network file :download:`here <Networks/Network1.py>`.