from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    filename = Column(String(200))
    content = Column(Text)