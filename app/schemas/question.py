from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime
    # forward ref + безопасный дефолт
    answers: list["Answer"] = Field(default_factory=list)

    # Pydantic v2
    model_config = ConfigDict(from_attributes=True)
