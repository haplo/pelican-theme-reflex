# Development

Reflex uses gulp to compile LESS files into CSS and optimize the final build.

## Setup

```bash
npm install
pip install pre-commit  # or install system-wide
pre-commit install
```

### System Dependencies

- **Stork** (optional, for search): Install from [stork-search.net](https://stork-search.net/docs/install) if you want to test the search functionality locally.

## Compilation

`npm run watch`

## Example site

Create a virtualenv and install dependencies:

```shell
cd example
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run pelican:

```shell
make devserver
```

To deploy to Github Pages:

```shell
make github
```

## Pre-commit Hooks

[Pre-commit](https://pre-commit.com/) hooks run automatically on each commit to enforce code style and verify compiled assets:

```bash
# Run manually on all files
pre-commit run --all-files
```

Hooks include:
- File hygiene (trailing whitespace, EOF fixes)
- JSON/YAML validation
- Template formatting and linting with [djlint](https://djlint.com/)
- Asset build verification (when LESS source files change)
