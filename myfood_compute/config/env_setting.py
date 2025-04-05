from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseModel):
    user: str
    host: str
    password: str
    database: str
    port: int


class ServerSettings(BaseModel):
    url: str


class EnvironmentSettings(BaseSettings):
    class Config:
        env_file = "config.dev.env"
        extra = "ignore"

    user: str
    host: str
    password: str
    database: str
    port: int
    url: str

    def get_database_settings(self) -> DatabaseSettings:
        return DatabaseSettings(**self.model_dump())

    def get_server_settings(self) -> ServerSettings:
        return ServerSettings(**self.model_dump())


def database_setting():
    return EnvironmentSettings().get_database_settings()


def server_setting() -> str:
    return EnvironmentSettings().get_server_settings()
