import pathlib

import jinja2
import yaml

BASE_DIR = pathlib.Path(__file__).parent

with open(BASE_DIR / "prompts/quirks.yaml", "r") as f:
    yaml_data = yaml.safe_load(f)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(BASE_DIR / "prompts"), undefined=jinja2.StrictUndefined
)

template = env.get_template("system_prompt.j2")

final_prompt = template.render(
    agent_name="Momo", creator_name="Niklas", user_name="Niklas", **yaml_data
)

print(final_prompt)
