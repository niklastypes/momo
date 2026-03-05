import pydantic_settings
import structlog

from momo import constants, enums, prompt

log = structlog.get_logger()


class MomoConfig(pydantic_settings.BaseSettings):
    model_name: enums.OllamaModel
    temperature: float
    prompt: str


class SystemPromptConfig(pydantic_settings.BaseSettings):
    template_name: str = "system_prompt.j2"
    agent_name: str = constants.AGENT_NAME
    creator_name: str = constants.CREATOR_NAME
    user_name: str
    mode: enums.MomoMode
    changelog: str
    comment: str


def _load_system_prompt_config(
    user_name: str, mode: enums.MomoMode, changelog: str, comment: str
) -> SystemPromptConfig:
    system_prompt_config = SystemPromptConfig(
        user_name=user_name, mode=mode, changelog=changelog, comment=comment
    )

    log.info("Successfully initialized system prompt config:\n", config=system_prompt_config)
    return system_prompt_config


def load_momo_config(
    user_name: str, mode: enums.MomoMode, changelog: str = "", comment: str = ""
) -> MomoConfig:
    momo_config = MomoConfig(
        model_name=enums.OllamaModel.mistral_ministral_3b,
        temperature=0.05,
        prompt=prompt.construct_system_prompt_from_config(
            _load_system_prompt_config(
                user_name=user_name, mode=mode, changelog=changelog, comment=comment
            )
        ),
    )

    log.info("Successfully initialized Momo config:\n", config=momo_config)
    return momo_config
