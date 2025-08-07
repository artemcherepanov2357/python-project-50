### Hexlet tests and linter status:
[![Actions Status](https://github.com/artemcherepanov2357/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artemcherepanov2357/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=artemcherepanov2357_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=artemcherepanov2357_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=artemcherepanov2357_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=artemcherepanov2357_python-project-50)
[![Python CI](https://github.com/artemcherepanov2357/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/artemcherepanov2357/python-project-50/actions)

# GENDIFF (Difference Generator)
**GENDIFF** is a command-line utility that compares two files (JSON or YAML) and shows the differences in a human-readable or machine-readable format.

## Features

- Supports JSON and YAML formats
- Output differences in three formats:
  - `stylish` (default) - colored, human-readable output
  - `plain` - flat text format
  - `json` - machine-readable JSON output

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/artemcherepanov2357/python-project-50.git
make install
source .venv/bin/activate
```

## Launch example
```bash
gendiff tests/fixtures/nested/file1.json tests/fixtures/nested/file2.json --format stylish
gendiff tests/fixtures/nested/file1.json tests/fixtures/nested/file2.json --format plain
gendiff tests/fixtures/nested/file1.json tests/fixtures/nested/file2.json --format json
