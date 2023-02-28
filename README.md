# Digital Health Template

## Introduction 
A template repository for Digital Health projects.

## Usage
To use this cookiecutter install the `cookiecutter` package (`pip install cookiecutter`) and run:
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

## Python package
To prevent having to add the `src/` folder to the system path, it's often easier to structure your code as a Python package.
This project template follows the `src/` package structure, where each folder in the `src` folder is a Python package.
To locally install your package use:
```{bash}
pip install -e .
```
This creates an editable install, which means that after you make changes to your local package, you don't have to reinstall the package to use it.
The standard template also contains optional dependencies for testing and developing. To also install the optional dependencies use: `pip install -e ".[dev]"` or `pip install -e ".[test]"`.

If your package is called `my_package` you can import it anywhere by using:
```{python}
import my_package
from my_package import my_function
```

## Specifying dependencies
You can specify dependencies in the `pyproject.toml` either as normal dependecies, or optional dependencies (like dev and test dependencies).
That way these packages will always be installed along with your package.

It is recommended to also use a requirements.txt file to pin specific package versions, which makes contributing and deployment easier. But don't forgot to update these versions regularly.

## Virtual environment
### Using conda
```{bash}
conda env create -f environment.yml
conda activate
```

### Using venv
```{bash}
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Documentation and styleguide
Styleguids can be checked with linters, for instance, `flake8`.
By default, we adhere to the PEP-8 conventions
The line-length is automatically formatted by `black`
and has a maximum of 88.
The import are sorted by isort (in vscode: rightclick `sort imports` or auto organise imports on save)
The `setup.cfg` files contains the setup for flake8, including ignored folder (like tests/ and notebooks/).
The configuration for black and isort can be found in `pyproject.toml`.

Code can be formatted (`black`) and checked (e.g. `flake8`) and imports can be organized (`isort`) using:
```{bash}
black src/
flake8 src/
isort .
```

### Docstrings
We adhere to PEP-8 and PEP-257 with respect to docstrings. 
This implies a line length of at most 72 characters.
The following missing docstrings are currently ignored (see `.setup.cfg`)
* D100 Missing docstring in public module
* D104 Missing docstring in public package

### GitHub actions
After creating a project with cookiecutter, you can find the linting and unit test GitHub workflows in `.github/workflows/`, which enables standard flake8 linting and unit tests.
You still need to set add this workflow to branch protection rules for new repos.

### Sphinx
With `Sphinx` documentation can be automatically generated as html or pdf
from the docstrings.

Generate the documentation as follows

```{bash}
sphinx-build -b html docs docs/_build
```
