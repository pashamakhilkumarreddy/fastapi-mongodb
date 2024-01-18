from functools import lru_cache

from pydantic.dataclasses import dataclass
from pydantic_settings import BaseSettings


# @dataclass
class Settings(BaseSettings):
    env: str = 'production'
    host: str = '127.0.0.1'
    LOG_LEVEL: str = 'info'
    port: int
    app_name: str = 'FastAPI MongoDB Server'
    mongo_url: str

    class Config:
        env_prefix = ''
        env_file_encoding = 'utf-8'
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
