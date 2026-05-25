from app.services.retrieval import retrieve_relevant_chunks, build_context_string
from app.services.llm import call_llm
from app.prompts.templates import SYSTEM_PROMPT, build_prompt

FALLBACK_RESPONSE = (
    "I could not find enough information in the knowledge base to answer this question."
)


def run_rag_pipeline(user_message, conversation_history):
    chunks = retrieve_relevant_chunks(user_message)

    if not chunks:
        return {
            "reply": FALLBACK_RESPONSE,
            "tokensUsed": 0,
            "retrievedChunks": 0
        }

    context = build_context_string(chunks)

    prompt = build_prompt(
        context=context,
        history=conversation_history,
        question=user_message
    )

    reply, tokens_used = call_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt
    )

    return {
        "reply": reply,
        "tokensUsed": tokens_used,
        "retrievedChunks": len(chunks)
    }