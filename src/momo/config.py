import pydantic_settings
import structlog

from momo import enums

log = structlog.get_logger()


class MomoConfig(pydantic_settings.BaseSettings):
    model_name: enums.OllamaModel
    temperature: float
    prompt: str


def load_momo_config() -> MomoConfig:
    momo_config = MomoConfig(
        model_name=enums.OllamaModel.mistral_ministral_3b,
        temperature=0.05,
        prompt="Your name is Momo. You are a helpful assistant.",
    )

    log.info("Successfully initialized Momo config:\n", config=momo_config)
    return momo_config
