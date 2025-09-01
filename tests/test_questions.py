import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models.question import Question
from app.schemas.question import QuestionCreate
from app.crud.question_crud import create_question

@pytest.fixture(scope="module")
def db():
    engine = create_engine("postgresql://postgres:password@localhost:5432/test_db")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_question(db):
    question = QuestionCreate(text="Test question")
    created = create_question(db, question)
    assert created.text == "Test question"
    assert created.id is not None