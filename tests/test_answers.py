import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models.question import Question
from app.models.answer import Answer
from app.schemas.question import QuestionCreate
from app.schemas.answer import AnswerCreate
from app.crud.question_crud import create_question
from app.crud.answer_crud import create_answer

@pytest.fixture(scope="module")
def db():
    engine = create_engine("postgresql://postgres:password@localhost:5432/test_db")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_answer(db):
    # Создаем вопрос
    question = QuestionCreate(text="Test question")
    created_question = create_question(db, question)
    
    # Создаем ответ
    answer = AnswerCreate(user_id="user123", text="Test answer")
    created_answer = create_answer(db, answer, created_question.id)
    
    assert created_answer.text == "Test answer"
    assert created_answer.question_id == created_question.id