import pydantic
import pydantic_settings
import structlog

from momo import enums


class MomoConfig(pydantic_settings.BaseSettings):
    model_name: enums.OllamaModel
    temperature: float
    prompt: str


log = structlog.get_logger()

try:
    MOMO_CONFIG = MomoConfig(
        model_name=enums.OllamaModel.mistral_ministral_3b,
        temperature=0.05,
        prompt="Your name is Momo. You are a helpful assistant.",
    )

    log.info("Successfully initialized Momo with config:\n", config=MOMO_CONFIG)

except pydantic.ValidationError:
    log.error("Momo config validation failed. Please try again with valid field values.")
