from fastapi import APIRouter, HTTPException
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

# Dummy user
fake_user = {
    "id": 1,
    "username": "admin",
    "password": "1234",
    "role": "admin"
}

@router.post("/login")
def login(username: str, password: str):
    if username != fake_user["username"] or password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {
            "user_id": fake_user["id"],
            "role": fake_user["role"],
            "exp": datetime.utcnow() + timedelta(hours=2)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {"access_token": token}