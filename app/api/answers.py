from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.models.question import Question

router = APIRouter(prefix="/questions/{question_id}/answers", tags=["answers"])

@router.post("/", response_model=schemas.Answer)
def create_answer(
    question_id: int,
    answer: schemas.AnswerCreate,
    db: Session = Depends(get_db)
):
    # Проверяем существование вопроса
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return crud.create_answer(db, answer, question_id)

@router.get("/{answer_id}", response_model=schemas.Answer)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    db_answer = crud.get_answer(db, answer_id)
    if not db_answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer

@router.delete("/{answer_id}")
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_answer(db, answer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"message": "Answer deleted"}