# vectorstore_utils.py
"""
Utilities for managing vector stores
"""
from typing import List, Optional
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from embedding_utils import get_embedding_model, encode_query

def create_vectorstore(documents: List[Document], 
                      index_name: str = "faiss_index",
                      model_name: str = "all-MiniLM-L6-v2") -> FAISS:
    """
    Create and save a FAISS vector store from documents
    
    Args:
        documents: List of Document objects to embed
        index_name: Name/path to save the index
        model_name: The embedding model to use
        
    Returns:
        The created FAISS vectorstore
    """
    try:
        texts = [doc.page_content for doc in documents]
        embedding_model = get_embedding_model(model_name)
        
        vectorstore = FAISS.from_texts(texts, embedding_model)
        vectorstore.save_local(index_name)
        
        return vectorstore
    except Exception as e:
        print(f"Error creating vectorstore: {e}")
        raise

def load_vectorstore(index_name: str = "faiss_index") -> Optional[FAISS]:
    """
    Load a FAISS vectorstore from disk
    
    Args:
        index_name: Path to the saved index
        
    Returns:
        The loaded FAISS vectorstore or None if loading fails
    """
    try:
        embedding_model = get_embedding_model()
        return FAISS.load_local(
            index_name, 
            embedding_model, 
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        print(f"Error loading vectorstore from {index_name}: {e}")
        return None

def similarity_search(query: str, 
                     vectorstore: FAISS, 
                     k: int = 5, 
                     model_name: str = "all-MiniLM-L6-v2") -> List[Document]:
    """
    Perform similarity search using embeddings
    
    Args:
        query: The query string
        vectorstore: The FAISS vectorstore to search in
        k: Number of results to return
        model_name: The embedding model to use
        
    Returns:
        List of Document objects sorted by relevance
    """
    try:
        # Get query embedding 
        query_embedding = encode_query(query, model_name)
        
        # Search by vector
        results = vectorstore.similarity_search_by_vector(query_embedding, k=k)
        return results
    except Exception as e:
        print(f"Error during similarity search: {e}")
        return []