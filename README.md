# 🧠 DocMind AI

### Enterprise Retrieval-Augmented Generation (RAG) Assistant

> An enterprise-grade AI assistant that enables intelligent question answering over PDF documents using **Google Gemini**, **LangChain**, **FAISS**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-success?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-blueviolet?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)

---

# 📖 Overview

**DocMind AI** is an enterprise-style Retrieval-Augmented Generation (RAG) application that allows users to ask natural language questions about PDF documents.

Instead of relying only on the language model's knowledge, the application retrieves relevant information from uploaded documents using semantic search before generating accurate, context-aware responses with Google Gemini.

---

# ✨ Features

- 📄 Chat with PDF documents
- 🤖 Google Gemini integration
- 🔍 Semantic search using FAISS
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast vector-based retrieval
- 🌐 Interactive Streamlit web interface
- 📚 Modular project architecture
- 🔐 Secure API key management using environment variables

---

# 🏗️ Architecture

```text
                     User
                       │
                       ▼
              Streamlit Web UI
                       │
                       ▼
                 LangChain Pipeline
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Google Gemini API             FAISS Vector Store
                                      │
                                      ▼
                           Employee Handbook PDF
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Google Gemini |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | Hugging Face |
| UI | Streamlit |
| Environment | Python Virtual Environment |

---

# 📂 Project Structure

```text
Enterprise-RAG-PDF-Assistant/

│── app.py
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
│── .env.example

├── data/
│   └── EMPLOYEE HANDBOOK.pdf

├── utils/
│   ├── embeddings.py
│   ├── loader.py
│   ├── qa_chain.py
│   ├── retriever.py
│   ├── splitter.py
│   └── vectorstore.py

├── assets/
│   └── screenshots/

└── docs/
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SkySentinel-AI/Enterprise-RAG-PDF-Assistant.git
```

Move into the project directory:

```bash
cd Enterprise-RAG-PDF-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE

Run the application:

```bash
streamlit run app.py
```

---

# 🚀 How It Works

1. Load the PDF document.
2. Split the document into smaller chunks.
3. Generate embeddings for each chunk.
4. Store embeddings in the FAISS vector database.
5. User asks a question.
6. Relevant chunks are retrieved using semantic search.
7. LangChain combines the retrieved context with the user query.
8. Google Gemini generates a context-aware response.
9. The answer is displayed through the Streamlit interface.

---

# 🎯 Skills Demonstrated

- Generative AI
- Retrieval-Augmented Generation (RAG)
- LangChain
- Google Gemini API
- Prompt Engineering
- Semantic Search
- FAISS Vector Database
- Hugging Face Embeddings
- Streamlit
- Python Application Development

---

# 🗺️ Roadmap

- ✅ PDF Question Answering
- ✅ Google Gemini Integration
- ✅ FAISS Vector Search
- ✅ Streamlit UI
- ⬜ Multi-PDF Support
- ⬜ Conversation Memory
- ⬜ Authentication
- ⬜ Docker Support
- ⬜ REST API
- ⬜ AWS Deployment
- ⬜ CI/CD Pipeline

---

# 📸 Screenshots

> Screenshots will be added soon.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Rishikesh Jogdand**

Cloud Engineer | Generative AI | DevSecOps | AI Infrastructure

- 💼 LinkedIn: https://linkedin.com/in/j-r-306ba635b
- 📧 Email: jogdandrishikesh05@gmail.com
- 🐙 GitHub: https://github.com/SkySentinel-AI

---

⭐ If you found this project useful, consider giving it a Star.
