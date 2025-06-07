from fastapi import FastAPI

from .routers import auth, documents, rag, training

app = FastAPI()

app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(training.router)
app.include_router(rag.router)

@app.get("/")
def read_root():
    return {"message": "RAG Codex API"}
