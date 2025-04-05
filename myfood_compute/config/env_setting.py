from pydantic import BaseModel
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    class Config:
        env_file = "config.dev.env"
        extra = "ignore"

    user: str
    host: str
    password: str
    database: str
    port: int


def env_setting():
    return EnvironmentSettings()
