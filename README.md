# RAG Assistant

A simple RAG-based chatbot built using FastAPI, Gemini API, and sentence-transformers.

The assistant answers questions using semantic search over a local knowledge base.

---

## Features

- FastAPI backend
- Gemini API integration
- Semantic search
- Vector similarity retrieval
- Session chat history
- Simple responsive frontend

---

## Tech Stack

- FastAPI
- Python
- Gemini API
- sentence-transformers
- HTML
- CSS
- JavaScript

---

## Run Locally

```bash
pip install -r requirements.txt
```

Create `.env`

```env
LLM_API_KEY=your_gemini_api_key
```

Run:

```bash
python -m uvicorn app.main:app --reload
```

Open:

```bash
http://127.0.0.1:8000
```

---

## How It Works

```text
User Question
      ↓
Semantic Search
      ↓
Retrieve Relevant Chunks
      ↓
Send Context to Gemini
      ↓
Generate Response
```

---

## Author

Srikanth Banoth