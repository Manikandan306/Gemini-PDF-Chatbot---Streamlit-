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
### ✅ Step 3: Get Gemini API Key
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click Create API Key
4. Copy the key and create a file named .env in the project folder with this content:

```base
GOOGLE_API_KEY=your_api_key_here
```
Replace your_api_key_here with your real Gemini API key.

### ✅ Step 4: Add PDF Files
Make sure you have at least two PDF files placed in the same folder as the app:
```base
doc1.pdf
doc2.pdf
```
You can rename or replace these files with your own.

### ✅ Step 5: Start the Chatbot App
Run the following command to launch the app:
```base
streamlit run app.py
```

### 🧪 How to Use the ChatBot
1. Type any question in the input box
2. The system will read the PDFs, extract the most relevant sections using vector search, and respond using Gemini
3. Sample questions you can ask:
"What is the main idea of doc1?"

"Compare the introduction and conclusion"

"Summarize the second document"

"What are the key terms used in section 2?"

📌 Notes
-Gemini API has usage limits for free accounts

-No internet-based search is used — everything is based only on the uploaded PDFs

-You can change the number or name of the PDFs, but remember to update the filenames in the code if needed

## 🙋 Author Info
Name: Manikandan

Course: B.Tech Artificial Intelligence and Data Science

### 🎯 Objective of the Project
To build an intelligent chatbot capable of understanding, indexing, and answering queries from uploaded PDF files using Google's Gemini AI, with a simple and interactive frontend.

### 🏁 Outcome
Successfully created an end-to-end AI chatbot for PDFs

Integrated Gemini's Embedding and Flash model effectively

Built a user-friendly web app with real-time question answering from documents

Let me know if you also want:
- 🎞️ Demo script for viva or presentation
- 📄 Abstract file in Word format
- 📌 Tamil or bilingual version for local submission
