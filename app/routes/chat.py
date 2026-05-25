from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.rag import run_rag_pipeline
from app.services.session import get_history, add_message

router = APIRouter(prefix="/api")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    message = request.message.strip()
    session_id = request.sessionId.strip()

    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    history = get_history(session_id)

    result = run_rag_pipeline(
        user_message=message,
        conversation_history=history
    )

    add_message(session_id, "user", message)
    add_message(session_id, "assistant", result["reply"])

    return ChatResponse(
        reply=result["reply"],
        tokensUsed=result["tokensUsed"],
        retrievedChunks=result["retrievedChunks"]
    )