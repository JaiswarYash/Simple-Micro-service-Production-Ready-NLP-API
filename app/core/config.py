from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class AppConfig(BaseSettings):
    PROJECT_NAME: str = "NLP Production API"
    API_V1_STR: str = "/api/v1"
    
    # Keeping the field name as model_name is fine once we fix the namespace config below
    model_name: str = Field(
        default="distilbert-base-uncased-finetuned-sst-2-english", 
        validation_alias="MODEL_NAME"
    )
    
    text_input: int = 500
    debug: bool = False

    # COMBINED CONFIG: Use SettingsConfigDict for pydantic-settings
    model_config = SettingsConfigDict(
        env_file=".env", 
        case_sensitive=True,
        extra="ignore",
        # This is the magic line that stops the "model_" namespace warning
        protected_namespaces=() 
    )

app_config = AppConfig()