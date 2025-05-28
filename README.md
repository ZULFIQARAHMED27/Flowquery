# 🔥 FlowQuery - AI Document Assistant

> **Where Documents Meet Intelligence**

A powerful and lightweight document question-answering system that transforms your static documents into dynamic, conversational experiences using advanced vector embeddings and semantic search.

## 🌟 Overview

FlowQuery empowers you to:
1. **🚀 Ingest documents** into a high-performance vector database (FAISS)
2. **🔍 Query documents** using natural language with intelligent semantic search
3. **📊 Retrieve** the most contextually relevant document chunks instantly
4. **🤖 Generate answers** using optional local LLM integration for coherent responses
5. **💻 Interactive UI** with a beautiful Streamlit web interface

## 📁 Project Structure

```
flowquery/
├── app.py                 # Main CLI application
├── embedding_utils.py     # Advanced embedding operations
├── ingest.py              # Document processing & indexing
├── llm_integration.py     # Optional local LLM integration 
├── rag.py                 # Retrieval Augmented Generation core
├── requirements.txt       # Project dependencies
├── vectorstore_utils.py   # Vector store management
└── streamlit_app.py       # 🔥 Modern Streamlit web interface
```

## ⚡ Quick Installation

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Usage Options

### Option 1: Web Interface (Recommended)
Launch the modern Streamlit interface:
```bash
streamlit run streamlit_app.py
```
Then navigate to `http://localhost:8501` for the full FlowQuery experience!

### Option 2: Command Line Interface

**1. Data Preparation**
Prepare your documents as a JSON file:
```json
[
  {
    "page_content": "Your document text here...",
    "metadata": {"source": "document.pdf", "page": 1}
  },
  {
    "page_content": "More document text...",
    "metadata": {"source": "document.pdf", "page": 2}
  }
]
```

**2. Ingest Documents**
Process documents into FlowQuery's vector database:
```bash
python ingest.py --input your_documents.json --output your_index_name
```

**3. Query Documents**
Start the interactive CLI:
```bash
python app.py --index your_index_name
```

## 🎯 Supported Document Formats

- **📄 PDF** - Extract and process PDF documents
- **📝 DOCX** - Microsoft Word documents
- **📋 TXT** - Plain text files  
- **🔧 JSON** - Structured document chunks

## 🧠 LLM Integration & Extensibility

FlowQuery is designed for flexibility:

**🔍 Retrieval-Only Mode** (Default)
- Fast semantic search with relevant document chunks
- Perfect for quick information retrieval

**🤖 AI-Powered Mode** (Optional)
Enable intelligent answer generation:
```python
from llm_integration import OllamaLLM

# Enhanced RAG with local LLM
llm = OllamaLLM(model_name="mistral")
rag_system = RAGSystem(args.index, llm)
```

### Supported LLM Integrations:
- **Ollama** - Local models (Mistral, Llama, etc.)
- **OpenAI API** - GPT models
- **Hugging Face** - Open-source transformers
- **Custom** - Easy to extend with your preferred LLM

## ⚙️ Customization & Configuration

### 🎛️ Embedding Models
```python
# High-quality options:
"all-MiniLM-L6-v2"          # Fast & balanced (default)
"all-mpnet-base-v2"         # Higher quality
"multi-qa-MiniLM-L6-cos-v1" # Optimized for Q&A
```

### 🔧 Retrieval Parameters
```python
# Adjust search sensitivity
k=5                    # Number of results
similarity_threshold=0.7   # Minimum relevance score
```

### 📚 Document Processing
Extend `ingest.py` with custom loaders:
- PDF text extraction
- OCR for scanned documents  
- Web scraping capabilities
- Database integrations

## Great Test Questions to Try:
HR/Policy Questions:

"How many vacation days do I get?"
"What is the remote work policy?"
"How much is the training budget?"

Technical Questions:

"How do I configure the database?"
"What are the authentication requirements?"
"How do I troubleshoot startup issues?"

Process Questions:

"What is the deployment process?"
"How long should code reviews take?"
"What happens during an incident?"

Security Questions:

"What are the password requirements?"
"How should sensitive data be encrypted?"

Infrastructure Questions:

"What cloud platform do we use?"
"How is monitoring implemented?"

Semantic Search Tests:

Ask "How to fix problems?" (should find troubleshooting content)
Ask "What breaks often?" (should find incident/troubleshooting info)
Ask "Time off rules" (should find vacation policy)

This sample file will let you thoroughly test your docubot's semantic understanding and retrieval capabilities across different domains and question types!

## 🚄 Performance & Scaling

### ⚡ Optimized for Speed
- **Fast indexing** with FAISS vector database
- **Efficient retrieval** using approximate nearest neighbors
- **Memory optimized** for both small and large document collections
- **Parallel processing** for document ingestion

### 🏗️ Production Considerations
For enterprise deployments:
- **HNSW indexes** for sub-second retrieval on millions of documents
- **Metadata filtering** for targeted search within document subsets
- **Document re-ranking** with cross-encoders for precision
- **Horizontal scaling** with distributed vector databases
- **Caching layers** for frequently accessed documents

## 🎨 Features Highlights

- **🔥 Modern UI** - Sleek Streamlit interface with real-time feedback
- **📱 Responsive Design** - Works seamlessly on desktop and mobile
- **🛠️ Zero Setup Complexity** - Upload and query in under 2 minutes
- **🔒 Privacy First** - All processing happens locally
- **🎯 High Precision** - Advanced semantic matching algorithms
- **⚡ Real-time Processing** - Instant document indexing and search
- **📊 Progress Tracking** - Visual feedback for all operations

## 🤝 Contributing

We welcome contributions to make FlowQuery even better!

- 🐛 **Bug Reports** - Help us identify and fix issues
- 💡 **Feature Requests** - Suggest new capabilities
- 🔧 **Code Contributions** - Submit pull requests
- 📚 **Documentation** - Improve guides and examples
- 🎨 **UI/UX** - Enhance the user experience

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

FlowQuery is built with ❤️ using powerful open-source technologies:

- **[Streamlit](https://streamlit.io/)** - For the incredible web framework
- **[FAISS](https://github.com/facebookresearch/faiss)** - Facebook's efficient vector search
- **[Sentence Transformers](https://www.sbert.net/)** - State-of-the-art semantic embeddings
- **[Hugging Face](https://huggingface.co/)** - Transformer model ecosystem

---

⭐ **Star this repo if FlowQuery transforms how you work with documents!**

🔥 **Experience the future of document intelligence - try FlowQuery today!**
