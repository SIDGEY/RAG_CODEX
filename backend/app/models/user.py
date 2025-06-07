from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str
    trainings: List[int] = []
