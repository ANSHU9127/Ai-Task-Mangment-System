from fastapi import APIRouter
from app.services.ai_service import search_doc

router = APIRouter()

@router.get("/search")
def search(q: str):
    return {"results": search_doc(q)}