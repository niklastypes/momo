import pathlib
import typing as t

import jinja2
import yaml

if t.TYPE_CHECKING:
    from momo import config

BASE_DIR = pathlib.Path(__file__).parent  # .../momo/src/momo
PROMPTS_DIR = BASE_DIR / "prompts"
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(PROMPTS_DIR), undefined=jinja2.StrictUndefined
)


def _load_yaml(path: str) -> t.Any:
    with open(path, "r") as file:
        return yaml.safe_load(file)


def construct_system_prompt_from_config(system_prompt_config: "config.SystemPromptConfig") -> str:
    template = JINJA_ENV.get_template(system_prompt_config.template_name)
    return template.render(
        agent_name=system_prompt_config.agent_name,
        creator_name=system_prompt_config.creator_name,
        user_name=system_prompt_config.user_name,
        mode=system_prompt_config.mode,
        changelog=system_prompt_config.changelog,
        comment=system_prompt_config.comment,
        **_load_yaml(str(PROMPTS_DIR / "quirks.yaml")),
    )
