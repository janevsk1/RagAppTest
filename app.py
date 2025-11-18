# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

# --- Configuration ---
CHROMA_DIR = "chroma_store"

# --- Initialize components ---
print("🔄 Loading Chroma database and embedding model...")
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

# Retriever pulls top-matching chunks from your manual database
retriever = db.as_retriever(search_kwargs={"k": 3})

# Local LLM via Ollama (make sure 'ollama serve' is running and you have 'llama3' model)
llm = OllamaLLM(model="llama3")

# Build a simple Retrieval-Augmented Generation (RAG) chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# --- Flask App ---
app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    """Chat endpoint: send {"query": "..."} and get AI response."""
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "Missing query field"}), 400

    print(f"💬 Received query: {query}")
    result = qa_chain.invoke({"query": query})

    # Format response
    answer = result["result"]
    sources = [doc.metadata.get("source", "unknown") for doc in result["source_documents"]]

    print(f"✅ Responding with: {answer[:100]}...")  # preview of response
    return jsonify({
        "answer": answer,
        "sources": sources
    })

# --- Run the server ---
if __name__ == "__main__":
    print("🚀 RAG Chatbot API running on http://127.0.0.1:5000/chat")
    app.run(port=5000, debug=True)
