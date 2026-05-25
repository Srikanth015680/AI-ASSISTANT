MAX_HISTORY = 10

sessions = {}


def get_history(session_id):
    return sessions.get(session_id, [])


def add_message(session_id, role, content):
    if session_id not in sessions:
        sessions[session_id] = []

    sessions[session_id].append({
        "role": role,
        "content": content
    })

    sessions[session_id] = sessions[session_id][-MAX_HISTORY:]