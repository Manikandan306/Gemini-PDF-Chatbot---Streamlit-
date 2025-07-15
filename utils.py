import os
from dotenv import load_dotenv
import google.generativeai as genai

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings

load_dotenv()
genai.configure(api_key=os.getenv("YOUR_API_KEY"))

# ✅ Custom Gemini Embeddings wrapper
class GeminiEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [
            genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="retrieval_document"
            )["embedding"] for text in texts
        ]

    def embed_query(self, text):
        return genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_query"
        )["embedding"]

def load_and_split_pdfs(pdf_paths):
    all_pages = []
    for path in pdf_paths:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"❌ File not found: {path}")
        loader = PyPDFLoader(path)
        all_pages.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(all_pages)
    return docs

def create_vectorstore(docs):
    embeddings = GeminiEmbeddings()
    db = FAISS.from_documents(docs, embedding=embeddings)
    return db
