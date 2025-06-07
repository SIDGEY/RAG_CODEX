from fastapi import APIRouter

from app.services.vector_store import vector_store

router = APIRouter(prefix="/rag", tags=["rag"])

@router.post("/chat")
def chat(query: str, user_id: int = 1):
    """Return content of the most relevant document for the query."""
    answer = vector_store.query(query)
    return {"answer": answer}
