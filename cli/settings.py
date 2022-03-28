from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    SW_HOST: str
    SW_USER: str
    SW_PASS: str

    class Config:
        env_file = ".env"


@lru_cache
def load_settings():
    return Settings()
