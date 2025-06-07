from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/trainings", tags=["trainings"])

db_trainings = [
    {"id": 1, "title": "Angular Basics", "description": "Intro to Angular"},
    {"id": 2, "title": "FastAPI", "description": "Building APIs"},
]

@router.get("/")
def list_trainings() -> List[dict]:
    return db_trainings
