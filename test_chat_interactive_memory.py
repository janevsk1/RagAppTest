# ✅ Enhanced test_chat_interactive.py with Conversation Memory
# test_chat_interactive_memory.py
import requests
from collections import deque

API_URL = "http://127.0.0.1:5000/chat"

# Notes:
# You can change MEMORY_LIMIT = 5 to remember more turns.
# Memory is stored locally in RAM — when you close the script, it resets.
# Works great with Ollama models like llama3, mistral, or phi3.

# Keep the last N conversation messages
MEMORY_LIMIT = 5

def build_context(history):
    """Convert recent chat history into a formatted text block."""
    context_lines = []
    for role, msg in history:
        context_lines.append(f"{role}: {msg}")
    return "\n".join(context_lines)

def ask_backend(query: str, history) -> str:
    """Send query + short memory context to Flask backend."""
    try:
        # Prepare the combined prompt
        context = build_context(history)
        full_query = f"{context}\nUser: {query}" if context else query

        response = requests.post(API_URL, json={"query": full_query})
        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "")
            sources = data.get("sources", [])
            source_info = f"\n📄 Sources: {', '.join(sources)}" if sources else ""
            return f"{answer}{source_info}"
        else:
            return f"⚠️ Server returned {response.status_code}: {response.text}"
    except requests.exceptions.ConnectionError:
        return "❌ Could not connect to Flask server (is it running on port 5000?)."
    except Exception as e:
        return f"❌ Unexpected error: {e}"

def main():
    print("💬 Local RAG Chatbot with Memory")
    print("Type your questions below. Type 'exit' or 'quit' to stop.\n")

    # Memory: a deque keeps the most recent turns
    history = deque(maxlen=MEMORY_LIMIT)

    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        if not user_input:
            continue

        print("🤖 Bot is thinking...")
        answer = ask_backend(user_input, history)

        # Save both question and answer to memory
        history.append(("User", user_input))
        history.append(("Bot", answer))

        print(f"\n🤖 Bot: {answer}\n" + "-" * 60)

if __name__ == "__main__":
    main()
