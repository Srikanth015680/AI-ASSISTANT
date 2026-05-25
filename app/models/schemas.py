from pydantic import BaseModel


class ChatRequest(BaseModel):
    sessionId: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    tokensUsed: int = 0
    retrievedChunks: int = 0