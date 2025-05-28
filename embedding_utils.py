# embedding_utils.py
"""
Centralized utilities for embedding operations
"""
from typing import List, Optional
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model(model_name: str = "all-MiniLM-L6-v2"):
    """
    Returns a consistent embedding model using LangChain's wrapper
    
    Args:
        model_name: The name of the SentenceTransformer model to use
        
    Returns:
        A LangChain embedding model instance
    """
    try:
        return SentenceTransformerEmbeddings(model_name=model_name)
    except Exception as e:
        print(f"Error loading embedding model: {e}")
        raise
        
def encode_query(query: str, model_name: str = "all-MiniLM-L6-v2") -> List[float]:
    """
    Encode a query string directly using SentenceTransformer for vector search
    
    Args:
        query: The query string to encode
        model_name: The name of the SentenceTransformer model to use
        
    Returns:
        Query embedding as a list of floats
    """
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(model_name)
        return model.encode(query)
    except Exception as e:
        print(f"Error encoding query: {e}")
        raise