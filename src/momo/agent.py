import os

import dotenv
import pydantic_ai
from pydantic_ai import settings
from pydantic_ai.models import openai
from pydantic_ai.providers import ollama

from momo import config

dotenv.load_dotenv()


def build_momo_agent_from_config(config: config.MomoConfig) -> pydantic_ai.Agent:
    ollama_model = openai.OpenAIChatModel(
        model_name=config.model_name,
        provider=ollama.OllamaProvider(base_url=os.getenv("OLLAMA_BASE_URL")),
        settings=settings.ModelSettings(temperature=config.temperature),
    )

    return pydantic_ai.Agent(model=ollama_model, instructions=config.prompt)
