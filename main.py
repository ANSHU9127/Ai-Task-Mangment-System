from fastapi import FastAPI
from app.routes import auth, task, document, search, analytics

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Task & Knowledge System Running 🚀"}

app.include_router(auth.router, prefix="/auth")
app.include_router(task.router, prefix="/tasks")
app.include_router(document.router, prefix="/documents")
app.include_router(search.router)
app.include_router(analytics.router)
