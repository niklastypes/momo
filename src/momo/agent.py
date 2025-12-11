import os

import dotenv
import pydantic_ai
from pydantic_ai import settings
from pydantic_ai.models import openai
from pydantic_ai.providers import ollama

from momo.config import MOMO_CONFIG

dotenv.load_dotenv()

ollama_model = openai.OpenAIChatModel(
    model_name=MOMO_CONFIG.model_name,
    provider=ollama.OllamaProvider(base_url=os.getenv("OLLAMA_BASE_URL")),
    settings=settings.ModelSettings(temperature=MOMO_CONFIG.temperature),
)

momo_agent = pydantic_ai.Agent(
    model=ollama_model, instructions=MOMO_CONFIG.prompt
)

while True:
    user_input = input("User: ")
    result = momo_agent.run_sync(user_input)
    print(f"Momo: {result.output}\n")
