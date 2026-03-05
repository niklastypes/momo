import typer

from momo import agent, config, constants, diary, enums

app = typer.Typer(name="momo-cli")


@app.command()
def chat(
    user_name: str = typer.Option(
        constants.DEFAULT_USER_NAME,
        "--user-name",
        help="Customize the interaction by providing your name",
    ),
) -> None:
    momo_chat_config = config.load_momo_config(user_name=user_name, mode=enums.MomoMode.CHAT)
    momo_chat_agent = agent.build_momo_agent_from_config(momo_chat_config)

    while True:
        user_input = input(f"{user_name}: ")
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
    file_name: str = typer.Option("local", "--file-name", help="Specify file name for diary entry"),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Output generated diary entry onto terminal instead of text files. For local testing & debugging",
    ),
) -> None:
    diary_entry = diary.generate_diary_entry(comment)
    if dry_run:
        print(diary_entry)
    else:
        diary.save_diary_entry_to_disk(file_name, diary_entry)


if __name__ == "__main__":
    app()
