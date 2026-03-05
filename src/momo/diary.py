import typing as t

import pydantic_ai

MomoDiaryEntryTitle = t.NewType("MomoDiaryEntryTitle", str)
MomoDiaryEntryBody = t.NewType("MomoDiaryEntryBody", str)


# this currently reads the whole CHANGELOG.md
def load_changelog(path: str) -> str:
    with open(path) as f:
        return f.read()


def generate_diary_entry_body(
    agent: pydantic_ai.Agent, changelog: str, comment: str
) -> MomoDiaryEntryBody:
    diary_entry_information = f"These are the CHANGELOG updates:\n{changelog}"
    if comment:
        diary_entry_information += f"\n**Special Instructions**: {comment}"
    return MomoDiaryEntryBody(agent.run_sync(diary_entry_information).output)


def generate_diary_entry_title(
    agent: pydantic_ai.Agent, diary_entry_body: MomoDiaryEntryBody
) -> MomoDiaryEntryTitle:
    return MomoDiaryEntryTitle(agent.run_sync(diary_entry_body).output)
