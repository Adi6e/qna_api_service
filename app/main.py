from fastapi import FastAPI
from app.api.questions import router as questions_router
from app.api.answers import router as answers_router
from app.database import engine, Base
from app.models import Question, Answer

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Q&A API",
    description="API для управления вопросами и ответами",
    version="1.0.0"
)

app.include_router(questions_router)
app.include_router(answers_router)

@app.get("/")
async def root():
    return {"message": "Q&A API is running"}