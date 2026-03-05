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
    momo_diary_config = config.load_momo_config(user_name="Niklas", mode=enums.MomoMode.DIARY)
    momo_diary_agent = agent.build_momo_agent_from_config(momo_diary_config)

    changelog = diary.load_changelog(changelog_path)
    diary_entry = diary.generate_diary_entry(momo_diary_agent, changelog, comment)
    print(diary_entry)


if __name__ == "__main__":
    app()
