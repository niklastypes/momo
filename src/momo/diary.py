# this currently reads the whole CHANGELOG.md
def load_changelog(path: str) -> str:
    with open(path) as f:
        return f.read()
