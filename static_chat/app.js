const API_URL = "http://127.0.0.1:5000/chat";

const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message-input");
const sendBtn = document.getElementById("send-btn");

// Add message to UI
function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender === "user" ? "user-message" : "bot-message");
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const userText = input.value.trim();
    if (!userText) return;

    addMessage(userText, "user");
    input.value = "";

    // Show typing animation
    const typingIndicator = document.getElementById("typing-indicator");
    typingIndicator.style.display = "flex";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: userText })
        });

        const data = await response.json();

        // Hide typing animation
        typingIndicator.style.display = "none";

        addMessage(data.answer || "No response", "bot");

    } catch (error) {
        typingIndicator.style.display = "none";
        addMessage("❌ Connection error: " + error, "bot");
    }
}

sendBtn.addEventListener("click", sendMessage);
input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});
