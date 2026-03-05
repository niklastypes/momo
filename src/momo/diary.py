import typing as t

import pydantic
import structlog

from momo import agent, config, constants, enums

log = structlog.get_logger()

MomoDiaryEntryTitle = t.NewType("MomoDiaryEntryTitle", str)
MomoDiaryEntryBody = t.NewType("MomoDiaryEntryBody", str)


class MomoDiaryEntry(pydantic.BaseModel):
    title: MomoDiaryEntryTitle
    body: MomoDiaryEntryBody


# this currently reads the whole CHANGELOG.md
def _read_file_contents_from_path(path: str) -> str:
    with open(path) as f:
        return f.read()


def _generate_diary_entry_body(changelog: str, comment: str) -> MomoDiaryEntryBody:
    momo_diary_body_config = config.load_momo_config(mode=enums.MomoMode.DIARY_BODY)
    momo_diary_body_agent = agent.build_momo_agent_from_config(momo_diary_body_config)
    diary_entry_information = f"These are the CHANGELOG updates:\n{changelog}"
    if comment:
        diary_entry_information += f"\n**Special Instructions**: {comment}"
    log.debug("Generating diary entry body using:\n", context=diary_entry_information)

    diary_entry_body = MomoDiaryEntryBody(
        momo_diary_body_agent.run_sync(diary_entry_information).output
    )
    log.debug("Successfully generated diary entry body:\n", body=diary_entry_body)

    return diary_entry_body


def _generate_diary_entry_title(diary_entry_body: MomoDiaryEntryBody) -> MomoDiaryEntryTitle:
    momo_diary_title_config = config.load_momo_config(mode=enums.MomoMode.DIARY_TITLE)
    momo_diary_title_agent = agent.build_momo_agent_from_config(momo_diary_title_config)
    log.debug("Generating diary entry title using:\n", body=diary_entry_body)

    diary_entry_title = MomoDiaryEntryTitle(
        momo_diary_title_agent.run_sync(diary_entry_body).output
    )
    log.debug("Successfully generated diary entry title:\n", title=diary_entry_title)
    return diary_entry_title


def _optionally_remove_special_characters_from_title(
    title: MomoDiaryEntryTitle,
) -> MomoDiaryEntryTitle:
    chars_to_remove = ['*', '"']
    cleaned_title = title
    for char in chars_to_remove:
        cleaned_title = cleaned_title.replace(char, "")
    return MomoDiaryEntryTitle(cleaned_title)


def generate_diary_entry(comment: str) -> MomoDiaryEntry:
    changelog = _read_file_contents_from_path(constants.CHANGELOG_PATH)
    diary_entry_body = _generate_diary_entry_body(changelog, comment)
    diary_entry_title = _generate_diary_entry_title(diary_entry_body)
    clean_diary_entry_title = _optionally_remove_special_characters_from_title(diary_entry_title)

    return MomoDiaryEntry(title=clean_diary_entry_title, body=diary_entry_body)
