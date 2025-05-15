from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = "model/model.pkl"
    vectorizer_path: str = "model/vectorizer.pkl"
    env: str = "dev"
    port: int = 8000

    model_config = {
        "env_file": ".env",
        "protected_namespaces": ("settings_",)
    }


settings = Settings()