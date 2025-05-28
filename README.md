# Document Q&A Bot

A lightweight document question-answering system using vector embeddings and semantic search.

## Overview

This system allows you to:

1. Ingest documents into a vector database (FAISS)
2. Query the documents using natural language 
3. Retrieve the most semantically relevant document chunks
4. (Optional) Generate coherent answers using a local LLM

## Project Structure

```
├── app.py                 # Main application with CLI
├── embedding_utils.py     # Utilities for embedding operations
├── ingest.py              # Document ingestion and processing
├── llm_integration.py     # Optional local LLM integration 
├── rag.py                 # Retrieval Augmented Generation components
├── requirements.txt       # Project dependencies
└── vectorstore_utils.py   # Vector store management utilities
└── streamlit_app.py       # Streamlit UI
```

## Installation

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### 1. Data Preparation

Prepare your documents as a JSON file with the following structure:
```json
[
  {
    "page_content": "Your document text here...",
    "metadata": {"source": "optional-source-info.txt", "page": 1}
  },
  {
    "page_content": "More document text...",
    "metadata": {"source": "optional-source-info.txt", "page": 2}
  }
]
```

### 2. Ingest Documents

Process your documents into a vector database:
```
python ingest.py --input your_documents.json --output your_index_name
```

### 3. Query Documents

Start the interactive query interface:
```
python app.py --index your_index_name
```

## Extending with LLM Integration

The system is designed to work with or without a local LLM for answer generation:

1. By default, it works in "retrieval-only" mode, showing relevant document chunks
2. To enable answer generation, modify `rag.py` to use the LLM integration

Example LLM integration with Ollama:
```python
from llm_integration import OllamaLLM

# In app.py:
llm = OllamaLLM(model_name="mistral")
rag_system = RAGSystem(args.index, llm)
```

## Customization

- **Change embedding model**: Edit the model name parameter in the relevant functions
- **Adjust retrieval parameters**: Modify the `k` parameter in retrieval functions
- **Add document processing**: Expand `ingest.py` with custom document loaders

## Performance Considerations

- The default embedding model (all-MiniLM-L6-v2) offers a good balance of speed and quality
- For production use with larger document sets, consider:
  - Using a database with HNSW indexes for faster retrieval
  - Implementing filtering and metadata search
  - Adding document re-ranking