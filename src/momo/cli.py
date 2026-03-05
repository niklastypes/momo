import typer

from momo import agent, config, diary, enums

app = typer.Typer(name="momo-cli")


@app.command()
def chat() -> None:
    momo_chat_config = config.load_momo_config(user_name="Niklas", mode=enums.MomoMode.CHAT)
    momo_chat_agent = agent.build_momo_agent_from_config(momo_chat_config)

    while True:
        user_input = input("User: ")
        result = momo_chat_agent.run_sync(user_input)
        print(f"Momo: {result.output}\n")


@app.command()
def status() -> None:
    print("Nothing to see here yet - come back later!")


@app.command()
def diary_entry(
    comment: str = typer.Option(
        "", "--comment", help="Add special instructions on top of system prompt"
    ),
    changelog_path: str = "CHANGELOG.md",
) -> None:
    momo_diary_body_config = config.load_momo_config(
        user_name="Niklas", mode=enums.MomoMode.DIARY_BODY
    )
    momo_diary_body_agent = agent.build_momo_agent_from_config(momo_diary_body_config)

    changelog = diary.load_changelog(changelog_path)
    diary_entry_body = diary.generate_diary_entry_body(momo_diary_body_agent, changelog, comment)
    print(diary_entry_body)

    momo_diary_title_config = config.load_momo_config(
        user_name="Niklas", mode=enums.MomoMode.DIARY_TITLE
    )
    momo_diary_title_agent = agent.build_momo_agent_from_config(momo_diary_title_config)
    diary_entry_title = diary.generate_diary_entry_title(momo_diary_title_agent, diary_entry_body)
    print(f"Title: {diary_entry_title}")


if __name__ == "__main__":
    app()
