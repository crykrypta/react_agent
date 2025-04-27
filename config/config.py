from pydantic import BaseModel, SecretStr, Field
from environs import Env


class OpenAIScheme(BaseModel):
    api_key: SecretStr = Field(description='API-key for OpenAI')


class Config(BaseModel):
    # -| API keys |-
    openai: OpenAIScheme = Field(description='OpenAI config')


def load_config() -> Config:
    """Loads config from .env"""
    env = Env()
    env.read_env()

    return Config(
        openai=OpenAIScheme(
            api_key=SecretStr(env.str('OPENAI_API_KEY'))
        )
    )


inited_config = load_config()
