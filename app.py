import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from utils import load_and_split_pdfs, create_vectorstore

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyANOeZ9l8pymAcgYgpewPA1Z-eCd2MrWyE"))

st.set_page_config(page_title="Gemini PDF Chatbot", layout="wide")
st.title("📄 Gemini PDF ChatBot")
st.markdown("Ask anything from your uploaded PDFs!")

if "db" not in st.session_state:
    with st.spinner("Processing PDFs..."):
        pdfs = ["doc1.pdf", "doc2.pdf"]
        docs = load_and_split_pdfs(pdfs)
        db = create_vectorstore(docs)
        st.session_state.db = db
        st.session_state.chat_history = []

query = st.text_input("Your question:")

if query:
    with st.spinner("Thinking..."):
        retriever = st.session_state.db.as_retriever()
        relevant_docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        prompt = f"""You are an AI assistant. Use the context below to answer the user's question.

Context:
{context}

Question:
{query}
"""

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        st.write("🤖 " + response.text)
        st.session_state.chat_history.append((query, response.text))
