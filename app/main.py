import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes.chat import router as chat_router
from app.routes.health import router as health_router
from app.services.embeddings import generate_embeddings
from app.utils.chunker import chunk_documents
from app.vectorstore.store import vector_store

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("docs.json", "r", encoding="utf-8") as file:
    documents = json.load(file)

chunks = chunk_documents(documents)

texts = [chunk["text"] for chunk in chunks]

embeddings = generate_embeddings(texts)

vector_store.add_chunks(chunks, embeddings)

app.include_router(chat_router)
app.include_router(health_router)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
async def home():
    return FileResponse("frontend/index.html")