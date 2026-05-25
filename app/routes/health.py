from fastapi import APIRouter
from app.vectorstore.store import vector_store

router = APIRouter()


@router.get("/health")
async def health():
    stats = vector_store.stats()

    return {
        "status": "healthy",
        "documentsIndexed": stats["total_chunks"]
    }