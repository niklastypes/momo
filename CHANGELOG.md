## v0.3.0 (2026-01-20)

### ✨ Features

- introduce lean momo-cli tool with typer
- introduce logging via structlog
- enable first simple stateless chat via cli
- introduce MomoConfig
- add very first pydanticAI momo agent iteration

### 🐛 Fixes

- update dev blog path

### ♻️ Refactors

- extract ollama model as StrEnum
- extract ollama base URL into .env

### 📚 Documentation Changes

- add dev diary entry for v0.3.0

### 🔧 Chores

- update ruff-pre-commit-hook
- update .pre-commit-config.yaml

## v0.2.0 (2025-12-11)

### ✨ Features

- customize cz
- add suite of pre-commit hooks
- add conventional-pre-commit hook

### 👷 CICD Changes

- add job to publish dev diary entries to dev blog
- add GitLab release job
- add bump version job
- add first CICD configuration & QA stage job

### 📚 Documentation Changes

- add dev diary entry for v0.2.0
- add small instructions on how to delete a tag & release
- add small instruction to know which tag will be created
- add release notes for v0.1.0
- update README.me with setup information

### 🔧 Chores

- update mirrors-mypy pre-commit hook to v1.19.0
- add project description to pyproject.toml
- update .pre-commit-config.yaml
- exclude mdformat pre-commit hook from being updated by pre-commit-update hook
- gitignore .DS_Store
- add .gitignore
- add pyproject.toml
- fix Python version
- Initial commit
