# Digital Health Template

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FUMCU-Digital-Health%2FDigital_Health_Template%2Fmain%2F%257B%257Bcookiecutter.project_name%257D%257D%2Fpyproject.toml)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/UMCU-Digital-Health/Digital_Health_Template/test_cookiecutter.yml)
![GitHub License](https://img.shields.io/github/license/UMCU-Digital-Health/Digital_Health_Template)

## Introduction 
A template repository for Digital Health projects.

## Usage
To use this cookiecutter install the `cookiecutter` package (`uv tool install cookiecutter`) and run:
```{bash}
cookiecutter gh:UMCU-Digital-Health/Digital_Health_Template
```

## Version control
Version control is required for all projects. At DH we work with git and GitHub. The following are suggested for git usage
  * Keep your branch strategy simple and use  feature branches and optionally release branches (see: https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops) 
  * The main branch is protected through a pull request
  * Commit messages are written in English and adhere to the following rules:
    1. The title-line starts with a capital letter, is 50 characters (or less), 
       and has no punctuation at the end.
    2. It should be in the imperative voice. i.e. 
       'Add new About Us page' or 'Refactor tests for the order model'
    3. It should correctly complete the sentence: "If accepted, this commit will <your commit message goes here>."

### Data Version Control
For data version control we use [DVC](https://dvc.org/doc)

### Changelog
Keep a changelog in your root folder (see: CHANGELOG.md). This log is meant for humans and shows which changes were made and when. Our changelog format is based on [Keep a changelog](https://keepachangelog.com/)

### GitHub actions
After creating a project with cookiecutter, you can find the linting and unit test GitHub workflows in `.github/workflows/`, which enables standard flake8 linting and unit tests.
You still need to set add this workflow to branch protection rules for new repos.

## Python package
We use uv as a package manager, see [uv](https://docs.astral.sh/uv/) for more information.

To prevent having to add the `src/` folder to the system path, it's often easier to structure your code as a Python package.
This project template follows the `src/` package structure, where each folder in the `src` folder is a Python package.

To locally install your package use:
```{bash}
uv sync
```

This creates an editable install, which means that after you make changes to your local package, you don't have to reinstall the package to use it.
The standard template also contains optional dependencies for testing and developing, which are automatically installed by uv when running `uv sync`.

If your package is called `my_package` you can import it anywhere by using:

```{python}
import my_package
from my_package.my_module import my_function
```

When working with Jupyter notebooks to prevent having to reinstall your local package after every edit, add the following lines at the top of your notebook:
```{python}
%load_ext autoreload
%autoreload 2
```

## Specifying dependencies
You can specify dependencies in the `pyproject.toml` either as normal dependecies, or dependency groups (like dev dependencies).

Installing packages is done by using `uv add <package_name>` or `uv add <package_name> --dev` for development dependencies.

That way these packages will always be installed along with your package. You can use version specifiers for the dependencies (see: https://peps.python.org/pep-0440/#version-specifiers). 
It is advisable to use the compatible release specifier (`~=`). For example `~=2.2` is the same as `>=2.2,==2.*`. Using this specifier you can set your package to accept all patch changes, but not the next minor or major release.

It is recommended to also use a requirements.txt file to pin specific package versions `==2.2.1`, which makes contributing and deployment easier. But don't forget to update these versions regularly. You can use `uv export --no-dev --no-hashes -o requirements.txt` to automatically generate a requirements.txt file from the `pyproject.toml` file. 

For versioning we use the PEP 440 versioning scheme (see: https://peps.python.org/pep-0440/#version-scheme).
To update the version of your package, you can either set the version in the `pyproject.toml` file or use the `uv version --bump major|minor|patch` command.

## Virtual environment
Virtual environments are automatically created and managed by `uv`.
To run commands in the virtual environment, use `uv run <command>` or manually activate the virtual environment by running `. .venv/bin/activate` (Linux) or `.\.venv\Scripts\activate` (Windows).

## Documentation and styleguide
Styleguides can be checked with linters. We use `ruff` for compatibility and speed. By default, we adhere to the PEP-8 conventions and include some other checks. 

The line-length is automatically formatted by `ruff` and has a maximum of 88 (default setting).
The import are sorted by `ruff` (in vscode: rightclick `sort imports`) or auto organise imports on save, see [Editor Settings](#editor-settings).

See [pyproject.toml]({{cookiecutter.project_name}}/pyproject.toml) for the `ruff` settings.
`ruff` can either be installed by uv or by using the Visual Studio Code extensions.

Code can be formatted, organized and checked using:
```{bash}
ruff format src/
ruff check --select I --fix .  # Only fix the isort errors
ruff check .
```
This can also be done automatically, see [Editor Settings](#editor-settings). 

### Docstrings
We adhere to PEP-8 and PEP-257 with respect to docstrings. 
This implies a line length of at most 72 characters.
The following missing docstrings are currently ignored
* D100 Missing docstring in public module
* D104 Missing docstring in public package

### Sphinx
With `Sphinx` documentation can be automatically generated as html or pdf
from the docstrings.

Generate the documentation as follows

```{bash}
sphinx-build -b html docs docs/_build
```

## Editor settings

### VS Code
To automatically sort imports and run `ruff` formatting on save, first install the [Ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) in VS Code. Then, add the following lines to your VS Code user settings (`command + shift + p` -> `Preferences: Open user settings (JSON)`):

```{json}
"[python]": {
   "editor.defaultFormatter": "charliermarsh.ruff",
   "editor.formatOnSave": true,
   "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
   },
   "editor.formatOnType": true
},
"notebook.formatOnSave.enabled": true,
"notebook.codeActionsOnSave": {
   "source.organizeImports": "explicit"
},
```

## Deployment
For deployment we use [Posit Connect](https://posit.co/products/enterprise/connect/).

### Initial deployment
Before you can use the deployment script (see [below](#deployment-script)) you need to manually deploy the app for the first time. This is neccessary to obtain an app id from Posit Connect. 

Before the inital deployment you need to get your personal API Key. You API Key van be obtained by going to [Posit Connect](https://rsc.ds.umcutrecht.nl/), login and click on your acount in the top-right corner, then press `API Keys` and create a new API Key (note that you will have to save the API key in a password manager, since Posit Connect will not show your old API Keys). Never store your API Key in git or share it with anyone!

After you've obtained your API key, deploy using the following command:
```{bash}
rsconnect deploy dash --entrypoint run.app:app --server https://rsc.ds.umcutrecht.nl/ --api-key <insert-api-key-here> .
```
Replace `dash` by your app or api (`flask`/`fastapi` etc.). 

After deployment you can find your APP ID on [Posit Connect](https://rsc.ds.umcutrecht.nl/) by going to your app/api, go to the info pane and look for the GUID.
Store your API Key and APP ID in a `.env` file, so subsequent deployments can be done using the deploy script. Don't add the .env file to git! (the .env file is automatically ignored)

### Deployment script
To deploy your app or api to Posit Connect after initial deployment you can use the `deploy.sh` script. The script assumes a dash application, in case of fastapi or flask you have to replace `dash` by `fastapi`/`flask` in the deployment script. 
The script expects three environment variables: `API_KEY`, `APP_ID` and `APP_NAME`. Either use a `.env` file with `python-dotenv` or manually export those variables. When using a `.env` file for your environment variables, use the following commands to deploy your app to Posit Connect:
```{bash}
source .env
source deploy.sh
```
