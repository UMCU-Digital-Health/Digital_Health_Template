# Digital Health Template

## Introduction 
A template repository for Digital Health (DH) projects.

## Usage
To use this cookiecutter install the `cookiecutter` package (`pip install cookiecutter`) and run:
```
cookiecutter gh:UMCU-Digital-Health/Digital_Health_Template
```

## Version control
Version control is required for all projects. At DH we work with git and GitHub. The following are suggested for git usage
  * Use a feature branch or 
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow
  * The main branch is protected through a pull request
  * Commit messages are written in English and adhere to the following rules:
    1. The title-line starts with a capital letter, is 50 characters (or less), 
       and has no punctuation at the end.
    2. It should be in the imperative voice. i.e. 
       'Add new About Us page' or 'Refactor tests for the order model'
    3. It should correctly complete the sentence: "If accepted, this commit will <your commit message goes here>."


## Virtual environment
### Using conda
```
conda env create -f environment.yml
conda activate
```

### Using venv
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

To add your local packages to you pythonpath run 
`export PYTHONPATH="${PYTHONPATH}:."`

## Documentation and styleguide
Styleguids can be checked with linters, for instance, `flake8`.
By default, we adhere to the PEP-8 conventions
The line-length is automatically formatted by `black`
and has a maximum of 88. Line lengths of upto 119 characters are permissible.
The `setup.cfg` files contains guidelines we choose to ignore.

Code can be formatted (`black`) and checked (e.g. `flake8`)
```
black src/
flake8 --max-line-length 119 src/
```

### Docstrings
We adhere to PEP-8 and PEP-257 with respect to docstrings. 
This implies a line length of at most 72 characters.
The following missing docstrings are currently ignored (see `.flake8`)
* D100 Missing docstring in public module
* D104 Missing docstring in public package

### GitHub actions
After creating a project with cookiecutter, you can find the linting GitHub workflow in `.github/workflows/`, 
which enables standard flake8 linting.
You still need to set add this workflow to branch protection rules for new repos.

### Sphinx
With `Sphinx` documentation can be automatically generated as html or pdf
from the docstrings.

Generate the documentation as follows

```
sphinx-build -b html docs docs/_build
```
