# 🤖 Gemini PDF ChatBot

The Gemini PDF ChatBot is an AI-powered document assistant that allows users to upload PDF files and ask questions based on their content. It uses **Google’s Gemini Embeddings** for understanding the documents and **Gemini 1.5 Flash** to answer user questions in natural language.

---

## 📘 Project Overview

This chatbot is built to simulate how an AI can understand and respond based on custom PDF documents. It is useful for:

- Students reading research papers
- Professionals reviewing large reports
- Automating document summaries
- Creating question-answering tools for manuals, books, or guides

---

## ⚙️ Technologies Used

| Technology         | Purpose                                |
|--------------------|----------------------------------------|
| Google Gemini API  | For both Embeddings and LLM responses  |
| LangChain          | Document loading, chunking, RAG flow   |
| FAISS              | Vector database for similarity search  |
| Streamlit          | Frontend to interact with the chatbot  |
| dotenv             | Environment variable handling           |
| PyPDF              | PDF parsing and text extraction        |

---

## 🚀 How to Run This Project

Follow these steps carefully to run the Gemini PDF ChatBot on your local system.

---

### ✅ Step 1: Install Python

Make sure Python 3.9 or above is installed.  
You can download it from: https://www.python.org/downloads/

---

### ✅ Step 2: Install Required Libraries
Use the following command to install all dependencies:
```base
pip install -r requirements.txt
```
### ✅ Step 3: Run The Project
Use the following command to Run:
```base
streamlit run app.py
