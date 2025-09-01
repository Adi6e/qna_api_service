from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question import QuestionCreate

def create_question(db: Session, question: QuestionCreate):
    db_question = Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Question).offset(skip).limit(limit).all()

def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)
    if db_question:
        db.delete(db_question)
        db.commit()
    return db_question