from app.services.embeddings import generate_embedding
from app.vectorstore.store import vector_store

TOP_K = 3
SIMILARITY_THRESHOLD = 0.3


def retrieve_relevant_chunks(query):
    query_embedding = generate_embedding(query)

    return vector_store.similarity_search(
        query_embedding=query_embedding,
        top_k=TOP_K,
        threshold=SIMILARITY_THRESHOLD
    )


def build_context_string(chunks):
    context = []

    for i, chunk in enumerate(chunks, start=1):
        context.append(
            f"[Source {i}: {chunk['title']}]\n{chunk['text']}"
        )

    return "\n\n".join(context)