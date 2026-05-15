from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Interactive AI Bio/Chem Discovery Simulator"
    app_version: str = "0.1.0"
    service_name: str = "biology-api-test"
    backend_env: str = "development"
    frontend_origin: str = "http://localhost:3000"
    zhipu_api_key: str = ""
    zhipu_model: str = "glm-4-plus"
    external_api_timeout_seconds: float = 4.0

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
