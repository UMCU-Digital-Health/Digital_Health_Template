# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.6] - 2024-05-23

## Removed
- Removed Sphinx documentation from the template

## Changed
- Changed readme to use uv instead of pip
- Update GitHub actions to use uv
- Default to use Python 3.12

## Added
- Added a post install script to install nbstripout and set it up

## [1.0.5] - 2024-04-04

## Added
- Added some shields to the README

## Changed
- Updated Python version
- Updated GitHub actions
- Updated tools to use ruff

## Fixes
- Fixes ruff linting setting to prevent deprecation warning

## [1.0.4] - 2024-02-02

### Fixed
- Updated VS Code organizeImports settings

## [1.0.3] - 2023-12-05

### Added
- Added an example model card in the `docs/` folder

### Changed
- Changed to location of example dataset card to `docs/` folder

## [1.0.2] - 2023-12-05

### Added
- Added nbstripout to automatically delete notebook outputs as git filter

### Fixed
- Moved deploy script to project folder

## [1.0.1] - 2023-11-24

### Added
- Added an example dataset card in `data/`

### Changed
- Changed default linter from flake8 to ruff and removed setup.cfg file

## [1.0.0] - 2023-09-18

### Added
- Added Changelog to template project and added explanation in README

### Fixed
- Moved requirements.txt file in the project folder
