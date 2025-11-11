from commitizen import defaults
from commitizen.cz import conventional_commits

BUMP_TYPES = {
    "feat",
    "fix",
    "hotfix",
    "revert",
    "refactor",
    "perf",
    "build",
    "infr",
}

CHANGELOG_TYPES = (
    BUMP_TYPES | {"ci", "test", "style", "docs", "chore"}
)  # all conventional commit types defined in '.pre-commit-config.yaml', except for 'bump' and 'merge'
ALL_TYPES = BUMP_TYPES | CHANGELOG_TYPES

COMMIT_PARSER_REGEX = (
    rf"^((?P<change_type>{'|'.join(ALL_TYPES)}|BREAKING_CHANGE)"
    r"(?:\((?P<scope>[^()\r\n]*)\)|\()?(?P<breaking>!)?|\w+!):\s(?P<message>.*)?"
)

BUMP_MAP = {
    r"^.+!$": defaults.MAJOR,
    r"^BREAKING[\-\ ]CHANGE": defaults.MAJOR,
    r"^feat": defaults.MINOR,
    r"^fix": defaults.PATCH,
    r"^hotfix": defaults.PATCH,
    r"^revert": defaults.PATCH,
    r"^refactor": defaults.PATCH,
    r"^perf": defaults.PATCH,
    r"^build": defaults.PATCH,
    r"^infr": defaults.PATCH,
}

BUMP_MAP_ZERO = {
    r"^.+!$": defaults.MINOR,
    r"^BREAKING[\-\ ]CHANGE": defaults.MINOR,
    r"^feat": defaults.MINOR,
    r"^fix": defaults.PATCH,
    r"^hotfix": defaults.PATCH,
    r"^revert": defaults.PATCH,
    r"^refactor": defaults.PATCH,
    r"^perf": defaults.PATCH,
    r"^build": defaults.PATCH,
    r"^infr": defaults.PATCH,
}


class CustomMomoCz(conventional_commits.ConventionalCommitsCz):
    """Subclass of the default 'cz_conventional_commits' commitizen ruleset

    With some key configuration values changed to add more commit types to
    either bump the version (e.g. 'infr') or be included in the changelog (e.g. 'ci').

    Instead of inheriting from the 'BaseCommitizen' as mentioned in the docs
    (https://commitizen-tools.github.io/commitizen/customization/#2-customize-through-customizing-a-class),
    this inherits from 'ConventionalCommitsCz' to use most of that logic, and just tweak it.
    """

    # overall parser that finds commits to act on
    commit_parser = COMMIT_PARSER_REGEX

    # which commits cause a bump
    bump_pattern = rf"^(((BREAKING[\-\ ]CHANGE|{'|'.join(BUMP_TYPES)})(\(.+\))?(!)?)|\w+!):"

    # rules for which commit type causes what level of bump
    bump_map = BUMP_MAP

    # when in version 0.x.x, hold off from doing a major bump
    bump_map_major_version_zero = BUMP_MAP_ZERO

    # which commits to consider for the changelog
    changelog_pattern = (
        rf"^(((BREAKING[\-\ ]CHANGE|{'|'.join(CHANGELOG_TYPES)})(\(.+\))?(!)?)|\w+!):"
    )

    # corresponding terms to use in the changelog
    change_type_map = {
        "BREAKING CHANGE": "💥 BREAKING CHANGES",
        "feat": "✨ Features",
        "fix": "🐛 Fixes",
        "hotfix": "🚑️ Hot Fixes",
        "revert": "🔙 Reversions",
        "refactor": "♻️ Refactors",
        "perf": "⚡️ Performance Improvements",
        "build": "📦 Build Changes",
        "infr": "🏗️ Infrastructure Changes",
        "ci": "👷 CICD Changes",
        "test": "🧪 Tests",
        "style": "🎨 Style Changes",
        "docs": "📚 Documentation Changes",
        "chore": "🔧 Chores",
    }

    change_type_order = list(change_type_map.values())
