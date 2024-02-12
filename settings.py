from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath

from functools import lru_cache

from pathlib import Path


class EnvSettings(BaseSettings):  
    root_dir: DirectoryPath = Path(__file__).parent
    model_config = SettingsConfigDict(
        env_file=f'{root_dir}/.env',
        env_file_encoding='utf-8',
    )

    BOT_TOKEN: str
    WHOOK: str


class Settings:
    env: EnvSettings = EnvSettings()


@lru_cache(typed=True)
def get_settings() -> Settings:
    return Settings()


if __name__ == '__main__':
    print(get_settings().env.BOT_TOKEN)
    print(get_settings().env.URL)
