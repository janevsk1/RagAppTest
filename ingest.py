# ingest.py
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DATA_DIR = "data"
CHROMA_DIR = "chroma_store"

# Load all text files
docs = []
for file in os.listdir(DATA_DIR):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(DATA_DIR, file), encoding="utf-8")
        docs.extend(loader.load())

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Embed using modern langchain-huggingface class
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store locally in Chroma
db = Chroma.from_documents(chunks, embedding, persist_directory=CHROMA_DIR)
db.persist()

print(f"✅ Ingested {len(chunks)} chunks from {len(docs)} docs into {CHROMA_DIR}")
