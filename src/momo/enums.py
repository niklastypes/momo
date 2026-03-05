import enum


class OllamaModel(enum.StrEnum):
    mistral_ministral_3b = "ministral-3:3b"


class MomoMode(enum.StrEnum):
    CHAT = "chat"
    DIARY_BODY = "diary_body"
    DIARY_TITLE = "diary_title"
