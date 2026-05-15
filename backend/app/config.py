from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Interactive AI Bio/Chem Discovery Simulator"
    app_version: str = "0.1.0"
    service_name: str = "biology-api-test"
    backend_env: str = "development"
    frontend_origin: str = "http://localhost:3000"
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com"
    deepseek_model: str = "deepseek-v4-pro"
    deepseek_reasoning_effort: str = "high"
    external_api_timeout_seconds: float = 4.0

    model_config = SettingsConfigDict(env_file=(".env", "../.env"), extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
