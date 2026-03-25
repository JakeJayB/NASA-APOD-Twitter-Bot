from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NASA_APOD_KEY: str
    UPLOADCARE_KEY: str


    model_config = {
        "env_file": ".env"
    }

environment = Settings()