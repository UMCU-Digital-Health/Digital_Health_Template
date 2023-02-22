# {{cookiecutter.project_name}}

Author: {{cookiecutter.full_name}}
Email: {{cookiecutter.email}}

## Installation

To install the {{cookiecutter.package_name}} package use:

```{bash}
pip install -e .
```

## Deploying to PositConnect

To deploy to PositConnect install rsconnect (`pip install rsconnect-python`) and run (in case of a dash app):
```{bash}
rsconnect deploy dash --server https://rsc.ds.umcutrecht.nl/ --api-key <(user specific key)> --entrypoint run.app:app .
```

## Documentation
Generate the Sphinx documentation as follows:

```
sphinx-build -b html docs docs/_build
```
