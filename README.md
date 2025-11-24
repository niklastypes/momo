# Momo

## Setup

Make sure to have `uv` installed:

```bash
brew install uv
```

Install the Python version pinned in `.python-version` via:

```bash
uv python install
```

Create & activate a new virtual environment:

```bash
uv venv
source .venv/bin/activate
```

To install the project dependencies, run:

```bash
uv sync --group dev
```

To install the pre-commit hooks, run:

```bash
uv run pre-commit install
```

Run the pre-commit hooks via:

```bash
uv run pre-commit run --all-files
```

## Usage

To know which tag and additions to the `CHANGELOG.md` will be created from the current stack of commits (e.g. when formulating the next release notes), simply run:

```bash
uv run cz bump --dry-run
```
