from .answer import Answer, AnswerCreate
from .question import Question, QuestionCreate

# Важно: после импорта обеих моделей
Question.model_rebuild()

__all__ = ["Question", "QuestionCreate", "Answer", "AnswerCreate"]
