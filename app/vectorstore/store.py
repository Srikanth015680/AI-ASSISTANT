import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class VectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = None

    def add_chunks(self, chunks, embeddings):
        self.chunks = chunks
        self.embeddings = np.array(embeddings, dtype=np.float32)

    def similarity_search(self, query_embedding, top_k=3, threshold=0.3):
        if self.embeddings is None:
            return []

        query_vector = np.array(query_embedding).reshape(1, -1)

        scores = cosine_similarity(
            query_vector,
            self.embeddings
        )[0]

        sorted_indexes = np.argsort(scores)[::-1]

        results = []

        for idx in sorted_indexes[:top_k]:
            score = float(scores[idx])

            if score < threshold:
                continue

            results.append({
                "text": self.chunks[idx]["text"],
                "title": self.chunks[idx]["title"],
                "chunk_id": self.chunks[idx]["chunk_id"],
                "score": round(score, 4)
            })

        return results

    def stats(self):
        return {
            "total_chunks": len(self.chunks)
        }


vector_store = VectorStore()