SYSTEM_PROMPT = """
You are a helpful assistant.

Answer only from the provided context.

If the answer is not in the context, say:
"I could not find enough information in the knowledge base to answer this question."
"""


def format_conversation_history(history):
    if not history:
        return ""

    lines = []

    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        lines.append(f"{role}: {msg['content']}")

    return "\n".join(lines)


def build_prompt(context, history, question):
    history_text = format_conversation_history(history)

    return f"""
Context:
{context}

Conversation History:
{history_text}

Question:
{question}

Answer:
"""