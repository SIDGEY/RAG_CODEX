from fastapi import APIRouter

router = APIRouter(prefix="/rag", tags=["rag"])

@router.post("/chat")
def chat(query: str, user_id: int = 1):
    # Placeholder chat logic
    return {"answer": f"You asked: {query}"}
