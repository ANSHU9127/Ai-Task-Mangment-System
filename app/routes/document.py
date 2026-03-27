from fastapi import APIRouter, UploadFile
from app.services.ai_service import add_doc
from app.db.database import SessionLocal
from app.models.document import Document

router = APIRouter()

@router.post("/")
async def upload(file: UploadFile):
    text = (await file.read()).decode()

    db = SessionLocal()
    db.add(Document(filename=file.filename, content=text))
    db.commit()

    add_doc(text)

    return {"msg": "uploaded"}