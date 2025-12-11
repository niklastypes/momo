import pydantic
import pydantic_settings

from momo import enums


class MomoConfig(pydantic_settings.BaseSettings):
    model_name: enums.OllamaModel
    temperature: float
    prompt: str


try:
    MOMO_CONFIG = MomoConfig(
        model_name=enums.OllamaModel.mistral_ministral_3b,
        temperature=0.05,
        prompt="Your name is Momo. You are a helpful assistant."
    )
    print("---")
    print(f"Initialized Momo with config: \n{MOMO_CONFIG=}")
    print("---\n")

except pydantic.ValidationError:
    print("Exception - cannot initialize MomoConfig")
