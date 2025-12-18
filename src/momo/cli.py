import typer

from momo import agent, config

app = typer.Typer(name="momo-cli")


@app.command()
def chat() -> None:
    momo_config = config.load_momo_config()
    momo_agent = agent.build_momo_agent_from_config(momo_config)

    while True:
        user_input = input("User: ")
        result = momo_agent.run_sync(user_input)
        print(f"Momo: {result.output}\n")


@app.command()
def status() -> None:
    print("Nothing to see here yet - come back later!")


if __name__ == "__main__":
    app()
