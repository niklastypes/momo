import pathlib
import typing as t

import jinja2
import yaml

BASE_DIR = pathlib.Path(__file__).parent  # .../momo/src/momo
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(BASE_DIR / "prompts"), undefined=jinja2.StrictUndefined
)


def _load_yaml(path: str) -> t.Any:
    with open(BASE_DIR / path, "r") as file:
        return yaml.safe_load(file)


def construct_system_prompt() -> str:
    template = JINJA_ENV.get_template("system_prompt.j2")
    return template.render(
        agent_name="Momo",
        creator_name="Niklas",
        user_name="Niklas",
        **_load_yaml("prompts/quirks.yaml"),
    )
