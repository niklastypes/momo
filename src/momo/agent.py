import pydantic_ai
from pydantic_ai.models import openai
from pydantic_ai.providers import ollama

ollama_model = openai.OpenAIChatModel(
    model_name="ministral-3:3b",
    provider=ollama.OllamaProvider(base_url="http://localhost:11434/v1"),
)

momo_agent = pydantic_ai.Agent(
    model=ollama_model, instructions="Your name is Momo. You are a helpful assistant."
)

result = momo_agent.run_sync("Hi! What is your name?")
print(result.output)
