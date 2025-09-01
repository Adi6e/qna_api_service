from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate

def create_answer(db: Session, answer: AnswerCreate, question_id: int):
    db_answer = Answer(
        question_id=question_id,
        user_id=answer.user_id,
        text=answer.text
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.id == answer_id).first()

def delete_answer(db: Session, answer_id: int):
    db_answer = get_answer(db, answer_id)
    if db_answer:
        db.delete(db_answer)
        db.commit()
    return db_answer