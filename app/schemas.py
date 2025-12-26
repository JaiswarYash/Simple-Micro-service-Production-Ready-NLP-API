from pydantic import BaseModel, Field, field_validator
from typing import Optional
from pydantic import ConfigDict

class NlpRequest(BaseModel):
    text: str = Field(
        ...,
        title="Input Text",
        description="The text to be analyzed by the NLP model.",
        min_length=3,
        max_length=512
    )

    # Professional way to provide examples in V2
    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "I love using FastAPI for building APIs!"
            }
        }
    }
    # custom validation:
    @field_validator('text')
    def text_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Text must not be empty or whitespace')
        return v

class NlpResponse(BaseModel):

    model_config = ConfigDict(protected_namespaces=())
    
    text: str          # Must be 'text', not 'title'
    sentiment: str     # Correct spelling (one 's')
    confidence: float
    model_version: Optional[str] = "v1"