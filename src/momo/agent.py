import os

import dotenv
import pydantic_ai
from pydantic_ai.models import openai
from pydantic_ai.providers import ollama

from momo import enums

dotenv.load_dotenv()

ollama_model = openai.OpenAIChatModel(
    model_name=enums.OllamaModel.mistral_ministral_3b,
    provider=ollama.OllamaProvider(base_url=os.getenv("OLLAMA_BASE_URL")),
)

momo_agent = pydantic_ai.Agent(
    model=ollama_model, instructions="Your name is Momo. You are a helpful assistant."
)

result = momo_agent.run_sync("Hi! What is your name?")
print(result.output)
