def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()

    if len(words) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size

        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_documents(documents):
    all_chunks = []

    for doc_index, doc in enumerate(documents):
        chunks = chunk_text(doc["content"])

        for chunk_index, chunk in enumerate(chunks):
            all_chunks.append({
                "title": doc["title"],
                "chunk_id": f"{doc_index}_{chunk_index}",
                "text": chunk
            })

    return all_chunks