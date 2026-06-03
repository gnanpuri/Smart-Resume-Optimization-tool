# Smart-Resume-Optimization-tool
AI-powered resume optimizer that matches your resume to job descriptions using RAG pipeline, ChromaDB, Groq LLaMA and Streamlit.
# Smart Resume Optimization Tool

An AI-powered resume optimization tool that analyzes your resume against a job description and provides a match score, missing keywords, and actionable improvement suggestions — all powered by a RAG (Retrieval-Augmented Generation) pipeline.


## 🧠 How It Works

```
Resume File (PDF/DOCX)
        ↓
Extract Text (python-docx / PyPDF2)
        ↓
Split into Chunks (LangChain Text Splitter)
        ↓
Convert to Vector Embeddings (Sentence Transformers)
        ↓
Store in ChromaDB (Local Vector Database)
        ↓
Job Description → Semantic Search → Retrieve Relevant Chunks
        ↓
Send to Groq LLaMA 3.3-70B for Analysis
        ↓
Display Results in Streamlit UI
```

---

## Features

-  Upload resume as **PDF or DOCX** file
-  Paste any **job description**
-  Get a **match score** (0-100%)
-  See your **strong points** that match the job
-  Identify **missing keywords** from the job description
-  Get **improved bullet point suggestions**
-  Receive **overall application advice**
- 📥 **Download** the full analysis report

---

## 🏗 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Vector Database | ChromaDB (local) |
| LLM | Groq LLaMA 3.3-70B (free) |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| RAG Pipeline | LangChain |
| Resume Parsing | python-docx, PyPDF2 |
| Environment | Python, python-dotenv |

---

##  Project Structure

```
smart-resume-tool/
├── app.py                  # Main Streamlit frontend
├── resume_parser.py        # PDF/DOCX text extraction
├── vector_store.py         # ChromaDB vector storage and search
├── analyzer.py             # Groq LLM analysis
├── .env                    # API keys (not committed to GitHub)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/smart-resume-tool.git
cd smart-resume-tool
```

### Step 2: Create a virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up environment variables
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your-groq-api-key-here
```

### Step 5: Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

##  Requirements

Create a `requirements.txt` file with:
```
streamlit
chromadb
langchain
langchain-groq
langchain-community
langchain-text-splitters
python-docx
PyPDF2
sentence-transformers
groq
python-dotenv
```

---

##  Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Click **API Keys** → **Create API Key**
4. Copy the key and paste it in your `.env` file

---

##  Key Concepts

### RAG (Retrieval-Augmented Generation)
Instead of sending the entire resume to the AI at once, the tool splits it into chunks, stores them in ChromaDB, and retrieves only the most relevant sections based on the job description. This improves accuracy and reduces token usage.

### Vector Embeddings
Text is converted into numerical vectors that represent meaning. Similar texts have similar vectors, enabling semantic search that finds relevant content even when exact keywords don't match.

### Semantic Search
ChromaDB finds the most relevant resume sections by comparing vector similarity with the job description — going beyond simple keyword matching to understand meaning.

---

##  Usage

1. Run the app with `streamlit run app.py`
2. Upload your resume (PDF or DOCX)
3. Paste the job description you are applying for
4. Click **Analyze My Resume**
5. Review your match score, missing keywords and improvement suggestions
6. Download the analysis report

---

##  Screenshots

> Add screenshots of your app here after running it locally.

---

##  Future Improvements

- [ ] Support for multiple resume versions
- [ ] ATS (Applicant Tracking System) score simulation
- [ ] Cover letter generation based on job description
- [ ] Resume scoring history and tracking
- [ ] Integration with LinkedIn job postings

---

##  Author

**Gnan Sai Konda**
- 📧 Gnansaikonda23@gmail.com
- 🎓 Master of Science in Information Systems — Saint Louis University

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
