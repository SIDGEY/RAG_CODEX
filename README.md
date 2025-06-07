# RAG_CODEX

This repository contains a skeleton for a multi-user Retrieval-Augmented Generation (RAG) application with a FastAPI backend and an Angular frontend.

## Structure

- `backend/` – FastAPI project handling authentication, document upload, trainings and RAG chat
- `frontend/` – Angular application for users to interact with documents and trainings

```text
backend/
  app/
    main.py
    models/
    routers/
    services/
  tests/
frontend/
  src/
```

## Running tests

```bash
cd backend
python3 -m pip install -r requirements.txt
pytest
```

## Docker

To run the API using Docker:

```bash
docker build -t rag-codex .
docker run -p 8000:8000 rag-codex
```

Alternatively you can use docker-compose:

```bash
docker-compose up --build
```

