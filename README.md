# RAG App Test — Local Retrieval Augmented Generation Chatbot

- A fully local, offline-capable RAG (Retrieval-Augmented Generation) application using:
- Flask (REST API backend)
- ChromaDB (vector database)
- LangChain (RAG pipeline)
- Ollama (local LLM runtime)
- HuggingFace embeddings
- HTML/CSS/JS front-end

This app allows you to upload manuals or text documents, embed them into Chroma, and query them via a chatbot-like web UI using local LLMs.

## ⚡ Features

✔ 100% local — no cloud, no API keys, no cost
✔ Uses Ollama to run Llama/Mistral/Phi models locally
✔ Provides semantic search using Chroma vector database
✔ Modern browser UI with chat bubbles
✔ “Bot is typing…” animation
✔ Easy to run on any Windows/macOS/Linux system
✔ Highly extensible, beginner-friendly architecture

## 📁 Project Structure
RagAppTest/
│
├── app.py                     # Flask backend (RAG API)
├── ingest.py                  # Embedding & indexing pipeline
├── requirements.txt           # Python dependencies
├── data/                      # Your documents (manuals, text files)
│     ├── manual1.txt
│     ├── manual2.txt
│
├── chroma_store/              # Auto-generated vector DB (after ingest)
│
├── static_chat/               # Front-end UI
│     ├── index.html
│     ├── style.css
│     ├── app.js
│
├── test_chat.py               # (Optional) simple local testing script
└── test_chat_interactive.py   # (Optional) console chatbot

## 🧩 Requirements

To run this project locally, you need:

# 1️⃣ Python

Download from:
https://www.python.org/downloads/

Version recommended: Python 3.10 – 3.12

# 2️⃣ Ollama (Local LLM Engine)

Download from:
https://ollama.com/download

After installation, open a terminal and pull a model:

ollama pull llama3

Verify Ollama is running:

http://127.0.0.1:11434

# 3️⃣ Git (optional, for cloning)

https://git-scm.com/downloads

## 🚀 Setup Instructions (Works on Any Local PC)

Follow these steps on ANY compututer (Windows/macOS/Linux):

# 1️⃣ Clone the repository
git clone https://github.com/janevsk1/RagAppTest.git
cd RagAppTest

Or download ZIP from GitHub.

# 2️⃣ Create a virtual environment
Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

This installs:

- Flask
- ChromaDB
- LangChain
- LangChain-HuggingFace
- LangChain-Ollama
- HuggingFace Hub
- Streamlit (optional)

# 4️⃣ Add your documents

Place your .txt manuals or text documents into:

/data

Example:

data/manual1.txt
data/manual2.txt

# 5️⃣ Run ingestion (build vector database)
python ingest.py

This will:

- Load your text files
- Chunk them
- Create embeddings
- Store vectors into chroma_store/

You should see:

✅ Ingested X chunks from Y docs into chroma_store

# 6️⃣ Start the backend (Flask API)
python app.py

if you have this error: ImportError: cannot import name 'CORS' from 'flask_cors'

pip install flask-cors

now is added into requirements and will be tested: flask-cors==4.0.0

You should see:

## 🚀 RAG Chatbot API running on http://127.0.0.1:5000/chat

Keep this terminal open — your backend must stay running.

# 7️⃣ Start the Chat UI (Browser)

Navigate to static_chat/:

cd static_chat
python -m http.server 8000


Open browser:
## 👉 http://localhost:8000/index.html

You now have a modern web-based chatbot UI connected to your local RAG engine!

## 🧠 Architecture Overview
               ┌───────────────┐
               │   User / UI   │
               │ index.html     │
               │ app.js         │
               └──────┬────────┘
                      │ (POST /chat)
                      ▼
             ┌────────────────────┐
             │       Flask        │
             │     app.py         │
             └──────┬─────────────┘
                    │
                    ▼
             ┌────────────────────┐
             │  RAG Pipeline      │
             │ RetrievalQA        │
             │ LangChain          │
             └──────┬─────────────┘
                    │
                    ▼
     ┌──────────────────────────────┐
     │        Vector Store          │
     │         ChromaDB             │
     │ (semantic search: top K)     │
     └───────────────┬──────────────┘
                     │
                     ▼
      ┌─────────────────────────────┐
      │        Local LLM            │
      │     Ollama (Llama3)         │
      │      http://localhost:11434 │
      └─────────────────────────────┘

🛠 Troubleshooting
❌ UI gives “Failed to fetch”

Cause: Opening index.html with file:// instead of HTTP

Fix:

python -m http.server 8000

❌ CORS error

Install:

pip install flask-cors


Add to app.py:

from flask_cors import CORS
CORS(app)

❌ Ollama port already in use
Error: bind: Only one usage of each socket address


Fix:

tasklist | findstr ollama
taskkill /PID xxx /F

🌟 Future Enhancements (coming soon)

File upload from UI → automatic re-index

Chat history persistence

Multiple collections in Chroma

LLM selection dropdown (Llama/Mistral/Phi)

Dark mode toggle

Typing speed simulation

Built-in logging panel

👍 License

MIT — free for personal and commercial use.