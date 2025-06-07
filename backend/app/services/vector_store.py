"""Very small in-memory vector store using TF-IDF."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class VectorStore:
    """Simple TF‑IDF based vector store for demo purposes."""

    def __init__(self) -> None:
        self.texts: list[str] = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None

    def add_document(self, text: str) -> None:
        """Add a new document to the store."""
        self.texts.append(text)
        self.vectors = self.vectorizer.fit_transform(self.texts)

    def query(self, q: str, top_k: int = 1) -> str:
        """Return concatenated top documents for a query."""
        if not self.texts:
            return ""

        q_vec = self.vectorizer.transform([q])
        sims = cosine_similarity(q_vec, self.vectors).flatten()
        best_idx = sims.argsort()[-top_k:][::-1]
        return " ".join(self.texts[i] for i in best_idx)


# Global store used by routers
vector_store = VectorStore()
