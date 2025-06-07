"""Placeholder vector store implementation."""

class VectorStore:
    def __init__(self):
        self.documents = []

    def add_document(self, text: str):
        self.documents.append(text)

    def query(self, q: str) -> str:
        # Fake retrieval
        return "".join(self.documents)
