from fastapi import APIRouter, UploadFile, File, Depends
from typing import List

router = APIRouter(prefix="/documents", tags=["documents"])

db_documents = []

@router.post("/")
def upload_document(file: UploadFile = File(...), user_id: int = 1):
    text = file.file.read().decode("utf-8")
    doc = {"id": len(db_documents) + 1, "user_id": user_id, "filename": file.filename, "text": text}
    db_documents.append(doc)
    return doc

@router.get("/")
def list_documents(user_id: int = 1) -> List[dict]:
    return [d for d in db_documents if d["user_id"] == user_id]
