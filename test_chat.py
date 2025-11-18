# test_chat.py
import requests
import json

# URL of your Flask chatbot backend
API_URL = "http://127.0.0.1:5000/chat"

# The user query you want to test
query = "How do I reset the AirCool Mini AC?"

# Build request payload
payload = {"query": query}

try:
    print(f"🧑 Sending query: {query}")
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        data = response.json()
        print("\n🤖 Bot reply:")
        print(data.get("answer", "No answer"))
        print("\n📄 Sources:", ", ".join(data.get("sources", [])))
    else:
        print(f"⚠️ Error {response.status_code}: {response.text}")

except requests.exceptions.ConnectionError:
    print("❌ Could not connect to Flask server. Is it running on port 5000?")
except Exception as e:
    print("❌ Unexpected error:", e)

#test commit
