# 🌸 Momo

## Setup

Make sure to have `uv` & `ollama` installed:

```bash
brew install uv
brew install ollama
```

During the very first setup, run

```bash
brew services start ollama
```

to run the `ollama` server in the background.

Use the `ollama` cli tool to download `ministral-3:3b` as LLM of choice:

```bash
ollama pull ministral-3:3b
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

### CLI

Interact with Momo via the command line using:

```bash
uv run momo <command>
```

So far, two commands have been defined (use `uv run momo --help` to view all available commands):

- `chat`: start a simple stateless back-and-forth chat with Momo
- `status`: placeholder command to print the current Momo status to the console

### Git tags

To know which tag and additions to the `CHANGELOG.md` will be created from the current stack of commits (e.g. when formulating the next release notes), simply run:

```bash
uv run cz bump --dry-run
```

To delete a new tag & release (e.g. after testing), run:

```bash
git pull
git tag -d vx.x.x
git push origin :refs/tags/vx.x.x
```

To delete the corresponding `bump` commit, run:

```bash
git reset --hard HEAD~1
git push --force
```
