function getSessionId() {
  let sessionId = localStorage.getItem("rag_session_id");

  if (!sessionId) {
    sessionId = "sess_" + Date.now();
    localStorage.setItem("rag_session_id", sessionId);
  }

  return sessionId;
}

function clearSession() {
  localStorage.removeItem("rag_session_id");
  return getSessionId();
}

let SESSION_ID = getSessionId();

const messagesArea = document.getElementById("messagesArea");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const welcomeState = document.getElementById("welcomeState");
const newChatBtn = document.getElementById("newChatBtn");
const chunksMeta = document.getElementById("chunksMeta");


function scrollToBottom() {
  messagesArea.scrollTop = messagesArea.scrollHeight;
}


function formatTime() {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit"
  });
}


function escapeHtml(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}


function appendUserMessage(text) {
  const div = document.createElement("div");

  div.className = "message-row user";

  div.innerHTML = `
    <div class="bubble-wrap">
      <div class="bubble">${escapeHtml(text)}</div>
      <div class="bubble-meta">${formatTime()}</div>
    </div>
  `;

  messagesArea.appendChild(div);

  if (welcomeState) {
    welcomeState.style.display = "none";
  }

  scrollToBottom();
}


function appendBotMessage(text, chunks = 0) {
  const div = document.createElement("div");

  div.className = "message-row bot";

  div.innerHTML = `
    <div class="bubble-wrap">
      <div class="bubble">${escapeHtml(text)}</div>
      <div class="bubble-meta">
        ${formatTime()}
      </div>
    </div>
  `;

  messagesArea.appendChild(div);

  chunksMeta.textContent = `${chunks} chunks retrieved`;

  scrollToBottom();
}


function appendErrorMessage(text) {
  const div = document.createElement("div");

  div.className = "message-row bot";

  div.innerHTML = `
    <div class="bubble-wrap">
      <div class="bubble error">${text}</div>
    </div>
  `;

  messagesArea.appendChild(div);

  scrollToBottom();
}


async function sendMessage(message) {
  const text = message.trim();

  if (!text) return;

  appendUserMessage(text);

  sendBtn.disabled = true;

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        sessionId: SESSION_ID,
        message: text
      })
    });

    const data = await response.json();

    if (response.ok) {
      appendBotMessage(data.reply, data.retrievedChunks);
    } else {
      appendErrorMessage(data.detail || "Something went wrong");
    }

  } catch (error) {
    appendErrorMessage("Server error");
  }

  sendBtn.disabled = false;
  messageInput.focus();
}


messageInput.addEventListener("input", () => {
  sendBtn.disabled = messageInput.value.trim() === "";
});


messageInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();

    const text = messageInput.value;

    messageInput.value = "";
    sendBtn.disabled = true;

    sendMessage(text);
  }
});


sendBtn.addEventListener("click", () => {
  const text = messageInput.value;

  messageInput.value = "";
  sendBtn.disabled = true;

  sendMessage(text);
});


newChatBtn.addEventListener("click", () => {
  SESSION_ID = clearSession();

  messagesArea.innerHTML = "";

  if (welcomeState) {
    messagesArea.appendChild(welcomeState);
    welcomeState.style.display = "flex";
  }

  chunksMeta.textContent = "";

  messageInput.value = "";

  sendBtn.disabled = true;
});


function insertSuggestion(text) {
  messageInput.value = text;
  sendBtn.disabled = false;
  messageInput.focus();
}


window.insertSuggestion = insertSuggestion;

messageInput.focus();