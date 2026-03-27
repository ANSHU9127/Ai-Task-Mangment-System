from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    status = Column(String(20))
