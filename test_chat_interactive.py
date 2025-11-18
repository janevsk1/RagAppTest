# test_chat.py
import requests

API_URL = "http://127.0.0.1:5000/chat"

def ask_backend(query: str) -> str:
    """Send query to Flask backend and return answer."""
    try:
        response = requests.post(API_URL, json={"query": query})
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
    print("💬 Local RAG Chatbot (connected to http://127.0.0.1:5000/chat)")
    print("Type your questions below. Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        if not user_input:
            continue

        print("🤖 Bot is thinking...")
        answer = ask_backend(user_input)
        print(f"\n🤖 Bot: {answer}\n" + "-" * 60)

if __name__ == "__main__":
    main()
