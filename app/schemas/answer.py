from datetime import datetime
from pydantic import BaseModel, ConfigDict

class AnswerBase(BaseModel):
    user_id: str
    text: str

class AnswerCreate(AnswerBase):
    pass

class Answer(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
