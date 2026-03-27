from fastapi import APIRouter
from app.db.database import SessionLocal
from app.models.task import Task

router = APIRouter()

@router.get("/analytics")
def analytics():
    db = SessionLocal()

    total = db.query(Task).count()
    completed = db.query(Task).filter(Task.status=="completed").count()

    return {
        "total_tasks": total,
        "completed": completed,
        "pending": total - completed
    }