from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    X_BEARER_TOKEN: str
    X_API_KEY: str
    X_API_SECRET: str
    X_ACCESS_TOKEN: str
    X_ACCESS_SECRET: str
    X_CLIENT_ID: str
    X_CLIENT_SECRET: str
    NASA_APOD_KEY: str


    model_config = {
        "env_file": ".env"
    }

environment = Settings()