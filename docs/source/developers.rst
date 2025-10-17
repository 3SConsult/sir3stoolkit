For Developers
==============

Welcome to the Developers page! This section provides resources and instructions for developers who want to contribute to Sir3SToolkit-Documentation. 

- **Toolkit Contact**: If you encounter an issue with the Toolkit that should be fixed or have an idea for enhancement, feel free to create an new entry on our `GitHub forum <https://github.com/3SConsult/sir3stoolkit/issues>`_. Please include the Toolkit and SirGraf version you are using and, if available, the Jupyter Notebook you are working with.

- **Documentation Contact**: For additional information regarding this documentation, and contribution inquiries, please contact `sir3stoolkit@3sconsult.de <mailto:sir3stoolkit@3sconsult.de>`_.

- **GitHub Repository:** `GitHub Repository <https://github.com/3SConsult/sir3stoolkit>`_.

- **PyPI Page:** `PyPI Page <https://pypi.org/project/sir3stoolkit/>`_.

Setting Up Git on Your Computer
-------------------------------

Follow these steps to install and configure Git:

1. **Download Git:** Visit the `official Git website <https://git-scm.com/downloads>`_ and download the version that is compatible with your operating system.

2. **Install Git:** Launch the downloaded installer and follow the setup wizard to complete the installation.

3. **Configure Your GitHub Username:** Open your terminal or command prompt and enter the following command, replacing "Your Name" with your actual GitHub username:

   .. code-block:: bash

      git config --global user.name "Your Name"

4. **Configure Your GitHub Email:** Similarly, set your GitHub email using the following command, replacing ``your.email@example.com`` with your actual email:

   .. code-block:: bash

      git config --global user.email "your.email@example.com"

.. note::

   If you're pushing your first commit to GitHub, you might be prompted to authenticate your GitHub account. This usually involves entering your GitHub account credentials in a browser dialogue window that pops up. This is a standard security measure to ensure you have the necessary permissions to push to the repository.

Working with GitHub
-------------------

.. _cloning-github-label: 

Cloning the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To clone a GitHub repository to your local folder, follow these steps:

1. **Navigate to the Parent Directory of Your Project:** Use the ``cd`` command followed by the path to the parent directory of your project (This is the directory that should contain your project folder).

   .. code-block:: bash

      cd "C:\Users\User\3S"

2. **Clone the GitHub Repository:** Use the ``git clone`` command followed by the URL of the repository.

   .. code-block:: bash

      git clone https://github.com/3SConsult/sir3stoolkit


General GitHub Version Control Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These instructions lay out the different steps of the GitHub procedure around contributing to SIR 3S Toolkit. Especially due to the GitHub repository currentley sitting on only one branch (main), following these basic rules is crucial. As soon as SIR 3S Toolkit has a higher amount of frequent contributors, a more suitable system with multiple branches will be implemented.

.. note::
    Before following each step for the first time, read their instructions fully including notes like this one. If an unexpected problem occurs, you can search the :ref:`command-collection-label` for a solution.

Follow these steps every time you contribute to SIR 3S Toolkit:

1. **Get the Latest Version from GitHub**: :ref:`get-latest-version-label`

2. **Edit SIR 3S Toolkit**: Now you can edit the entire SIR 3S Toolkit project locally. Please ensure, that nobody else is working on the project simultaneously in the same sourcefiles, because this could cause problems, when trying to commit.

3. **Commit Your Changes to the GitHub Repository**: :ref:`commit-changes-label`

.. _get-latest-version-label:

Get the Latest Version from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch the latest changes from the origin and merge them into your current branch, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\sir3stoolkit"
      
2. **Pull the latest changes from the origin**: Use the ``git pull`` command. 

   .. code-block:: bash

      git pull origin master
        
   For a more detailed updating process, follow steps 2 and 3 instead.
        
2. **Fetch the latest changes from the origin:** Use the ``git fetch origin`` command.

   .. code-block:: bash

      git fetch origin

3. **Merge the fetched changes into your current branch:** Use the ``git merge origin/master`` command.

   .. code-block:: bash

      git merge origin/master

.. note::
    If you made local changes to files that were also edited by a remote commit, make a local copy of your project directory and use ``git reset --hard origin/master``. Afterwards you can paste you local changes back in. Just make sure that the remote changes to these files were not important or manually include them in your files.

.. code-block:: bash

   git reset --hard origin/master  

.. _commit-changes-label:

Commit Your Changes to the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To commit your changes to the GitHub repository, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\3S\sir3stoolkti"

2. **Add files to the staging area:** Use the ``git add`` command followed by the name of the file. Use ``git add .`` to add all files.

   .. code-block:: bash

      git add .

3. **Create a new commit with a descriptive message:** Use the ``git commit -m "commit_message"`` command.

   .. code-block:: bash

      git commit -m "commit_message"

4. **Push your commit to the GitHub Repository:** Use the ``git push origin master`` command.

   .. code-block:: bash

      git push origin master

.. .. note::
    If you want to push multiple commits back to back, keep in mind that the SIR 3S Toolkit GitHub repository uses :ref:`github-workflow-label` that might require you to fetch after committing to certain directories. Because workflows can automatically author commits, so fetching ensures you have the latest changes. Alternatively you can check the :ref:`current-workflow-label` utilised by the GitHub Repository and whether the might be triggered by your commit.

.. _command-collection-label:

Collection of Useful Git Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To discard all local changes and set your local HEAD to the master, use:

   .. code-block:: bash

      git reset --hard origin/master

To discard all remote changes and force push local HEAD to the master, use:

   .. code-block:: bash

      git push origin master --force
           
To uncommit commited but not yet pushed changes of the previous commit without changing local files (move HEAD pointer back by one commit), use:

   .. code-block:: bash

      git reset --soft HEAD~1

To revert all changes caused by a commit, use:

   .. code-block:: bash

      git revert commitID
      
To load a branch locally, use:

   .. code-block:: bash

      git checkout <branchname>

.. _github-workflow-label:

GitHub Workflows
~~~~~~~~~~~~~~~~

Our GitHub repository uses workflows to facilitate certain processes by automating tasks. Workflows are defined using YAML files and are stored in the `.github/workflows` directory of our repository.

We currently use the following workflows:

.. list-table:: 
   :header-rows: 1

   * - **Name**
     - **Triggers**
     - **Tasks**
   * - `.github/workflows/publish-testpypi.yml`
     - Push to `main` with changes in:<br>• `pyproject.toml`<br>• `setup.py`<br>• `requirements.txt`<br>• `src/**`<br>• the workflow file itself<br>Or push of a tag starting with `v`
     - Builds the Python package using `pyproject.toml`, installs dev dependencies, and publishes to **TestPyPI** and **PyPI** using `twine`.
   * - `.github/workflows/deploy-docs.yml` *(assumed name)*
     - Push to `main`
     - Builds Sphinx documentation (including API docs via `sphinx-apidoc`) and deploys it to the `gh-pages` branch using `peaceiris/actions-gh-pages`. 

Anonymization Setup for Pre-Commit Hook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This guide explains how to set up the anonymization script as a Git pre-commit hook. It ensures that sensitive names in Jupyter notebooks are replaced before committing to the repository.

Step 1: Locate the Pre-Commit Hook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Navigate to the Git hooks directory of your local repository:

::

    <your_repo_root>/.git/hooks/

You will find a file named ``pre-commit.sample``. Rename it to ``pre-commit`` (without any file extension). Other contents of the file can be deleted, if not needed by the user for other purposes:

::

    mv pre-commit.sample pre-commit

Step 2: Edit the Pre-Commit Hook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open the ``pre-commit`` file in a text editor and replace its contents with the following:

::

      #!/bin/sh

      echo "🔒 Running anonymization script..."
      "C:/Users/<your_username>/AppData/Local/anaconda3/python.exe" "docs/source/anonymize_notebooks.py"

      if [ $? -ne 0 ]; then
      echo "❌ Anonymization failed. Commit aborted."
      exit 1
      fi

      # Re-stage any modified notebooks
      git ls-files -m | grep '\.ipynb$' | while read -r file; do
      git add "$file"
      done


Replace ``<your_username>`` with your actual Windows username or adjust the Python path to match your local installation.

Step 3: Create the Names File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the same directory as ``anonymize_notebooks.py`` (``docs/source/``), create a file named ``names_to_anonymize.txt``. Add one name per line that should be anonymized:

::

    Müller
    Schmidt

Step 4: Verify the Setup
^^^^^^^^^^^^^^^^^^^^^^^^
Make a small change in a Jupyter notebook that contains one of the names listed. Then run:

::

    git add .
    git commit -m "Test anonymization"

You should see output indicating that the anonymization script ran and which names were replaced.

Troubleshooting
^^^^^^^^^^^^^^^
- If you see an error like ``Python not found``, verify that the Python path in the hook is correct.
- Ensure that ``names_to_anonymize.txt`` exists and is in the correct directory.
- The hook must be named ``pre-commit`` with no file extension.


Generating the Documentation
----------------------------


The Toolkit documentation is edited in sir3stoolkit/docs/source on the main branch.

If you want to edit the documentation yourself, you have to install sphinx and sphinx related python packages.

You find all necssary packages in the dev and sphinx optional project dependencies in `pyproject.toml<https://github.com/3SConsult/sir3stoolkit/blob/main/pyproject.toml>`

   .. code-block:: bash

      pip install sphinx nbsphinx sphinx_copybutton sphinx-rtd-theme sphinx-togglebutton

To generate documentation, follow these steps:

1. **Edit the documentation:** Make your changes on the rst files in the sir3stoolkit/docs/source.

.. note:: Our GitHub Workflow sphinx.yaml automatically builds and deploys the documentation. If you do not need to view a local build of your changes, you can jump to step 4.

2. **Navigate to the sir3stoolkit directory:** Use the ``cd`` command.

   .. code-block:: bash

      cd "C:\Users\User\3S\sir3stoolkit"

3. **Make an HTML build:** Use ``python3 -m sphinx.cmd.build -b html . /_build/html`` (for python env)  or ``.\make.bat html`` (for conda env (recommended to use conda shell)).

   .. code-block:: bash

      python3 -m sphinx.cmd.build -b html . /_build/html
   
   .. code-block:: bash

      .\make.bat html


4. **Commit the changes.** Commit all files from sir3stoolkit to GitHub (:ref:`commit-changes-label`).

The new documentation can be found at `https://3sconsult.github.io/sir3stoolkit/index.html <https://3sconsult.github.io/sir3stoolkit/index.html>`_
