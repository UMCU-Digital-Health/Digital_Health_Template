# {{cookiecutter.project_name}}

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Author: {{cookiecutter.full_name}}
Email: {{cookiecutter.email}}

## Installation

To install the {{cookiecutter.package_name}} package use:

```{bash}
pip install -e .
```

or for development:

```{bash}
pip install -e ".[dev]"
```

This will also install the nbstripout package, which will strip out the output of notebooks when committing to git.

In order to configure the package, run the command:

```{bash}
nbstripout --install
```

## Deploying to PositConnect

To deploy to PositConnect install rsconnect (`pip install rsconnect-python`) and run (in case of a dash app):
```{bash}
rsconnect deploy dash --server https://rsc.ds.umcutrecht.nl/ --api-key <(user specific key)> --entrypoint run.app:app .
```

## Documentation
Dataset and model information can be found in the [dataset card](docs/dataset_card.md) and [model card](docs/model_card.md), respectively.

Generate the Sphinx documentation as follows:

```
sphinx-build -b html docs docs/_build
```
