from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    log_path: str
    diabetes_dataset_path: str
    heart_disease_dataset_path: str
    diabetes_model_path: str
    heart_disease_model_path: str
    diabetes_target: str
    heart_target: str
    test_size: float
    rs: int
    hyper_params_yaml_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )