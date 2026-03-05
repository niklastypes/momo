import pydantic_ai


# this currently reads the whole CHANGELOG.md
def load_changelog(path: str) -> str:
    with open(path) as f:
        return f.read()


def generate_diary_entry_body(agent: pydantic_ai.Agent, changelog: str, comment: str) -> str:
    diary_entry_information = f"These are the CHANGELOG updates:\n{changelog}"
    if comment:
        diary_entry_information += f"\n**Special Instructions**: {comment}"
    return agent.run_sync(diary_entry_information).output
