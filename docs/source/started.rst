Getting Started
===============

.. note::
    This documentation is still WORK IN PROGRESS.

Welcome to the Getting Started guide for the SIR 3S Toolkit! This guide is your first step towards understanding and utilizing the Toolkit. The purpose of the Toolkit and its applications will be explained.

**The SIR 3S Toolkit is only of interest to users with access to SIR 3S models and a licensed SIR 3S version**

What is SIR 3S Toolkit?
-----------------------

SIR 3S Toolkit is a Python package developed by 3S Consult that provides full programmatic control over SIR 3S models. At its core, the package wraps C# functionality, offering low-level access through methods like SetValue(), GetValue(), AddNewNode(), and more.

Built on top of this core are additional subpackages that offer higher-level abstractions, enabling more powerful and intuitive interactions with SIR 3S models. This layered design ensures flexibility and makes the Toolkit easily extensible for future enhancements.

Why is the Toolkit valuable when Working with SIR 3S?
-----------------------------------------------------

When working solely with SIR 3S, you're bound by its many—but still limited—capabilities. The SIR 3S Toolkit breaks those boundaries, giving you full control over your model with all the flexibility Python offers.

Whether you're setting up a model from scratch—defining nodes, pipes, and more—you can do it entirely in Python, tailored to your database and logic, rather than relying on SIR 3S's built-in import tools. For analysis, you can open your model in Python and craft custom algorithms when the built-in functions fall short. And if your algorithm needs to make changes based on its findings, the Toolkit is ready to handle that too.

What is the difference between SIR 3S Toolkit and PT3S?
-------------------------------------------------------

Since SIR 3S already offers `PT3S <https://github.com/3SConsult/PT3S>`_ as a Python package for accessing model data, you might wonder: why use the Toolkit if you're already working with PT3S?

PT3S provides powerful access to a model's database and calculation results by reading .mx and .db3 files via SQL. However, it operates from the outside—offering read-only access to exposed data structures. What it doesn't offer is a straightforward way to create, modify, or interact with core SIR 3S objects like nodes, pipes, and more.

That's where the SIR 3S Toolkit comes in. It goes beyond file access and interacts directly with the internal structure of a SIR 3S model, enabling full programmatic control over model creation, editing, and analysis.

If you want maximal Python capabilities concerning your SIR 3S model, it is advised to use both packages. In the future it is possible that the PT3S functionalities will slowly be integrated into the Toolkit.


Get SIR 3S Version with Toolkit Compatibility: Internal Preliminary Guide
-------------------------------------------------------------------------

.. note:: This guide can be deleted after the official public release of 90-15 Quebec.

Follow these steps:

1. **Get SIR 3S Version with Python Compatibility**: Copy ``S:\Softwareentwicklung\SIR 3S\Sir3S-90\Release\2025-06-27_Release_Quebec\SirCalc-90-15-02-03_Quebec_x64.zip`` and ``S:\Softwareentwicklung\SIR 3S\Sir3S-90\Release\2025-06-27_Release_Quebec\SirGraf-90-15-00-13_Quebec_x64.ZIP`` to your local machine preferably to ``C:/3S/SIR 3S Entwicklung``.

2. **Unpack .zip files**: Unpack both zip-folders.

3. **Get Common folder with Python for new SIR 3S Version**: Copy ``S:/Softwareentwicklung/SIR 3S/Sir3S-90/Common`` to your local machine preferably to ``C:/3S/SIR 3S Entwicklung``.

4. **Unpack .zip files**: Unpack the python zip folder in the Common folder. Make sure that ``C:/3S/SIR 3S Entwicklung/Common/Python312/python.exe`` exists.

5. **Get License for SIR 3S 90**: Copy ``SIR3S-90.LIC`` from ``T:/SCRATCH/Jablonski`` to ``C:/3S/SIR 3S Entwicklung/Common``.

6. **Upgrade pip and install numpy**: Open a cmd and enter the following commands:

   .. code-block:: bash

       cd "C:/3S/SIR 3S Entwicklung/Common/Python312"
       #python.exe -m pip install --upgrade pip (if needed)
       python.exe -m pip install numpy

7. **Continue** with the step 2 of Install Toolkit

.. _installing-toolkit-label: 

Install Toolkit
---------------

To install the Toolkit, follow these steps:

1. **Obtain SIR 3S:** The Toolkit requires an installed SIR 3S version of 90-15 Quebec or higher. As this is the first version with Python capabilities and the included ``Sir3S_Toolkit.dll``

2. **Install Toolkit via pip in SIR 3S Environment:** Open a cmd and enter the following commands, to install the Toolkit in the Python environment in the ``Common`` folder of your SIR 3S installation:

   .. code-block:: bash

       cd "C:/3S/SIR 3S Entwicklung/Common/Python312" #change to your local path
       python.exe -m pip install sir3stoolkit


3. **Optional: Install Toolkit via pip in other Environment:** Open a cmd in the desired environment and enter the following commands, to install the Toolkit in another Python environment:

   .. code-block:: bash

       pip install sir3stoolkit
       
If you encounter issues with that, located the python.exe file of the environment and follow step 1.

We now invite you to visit the :doc:`examples` page to understand basic Toolkit functionalities.
