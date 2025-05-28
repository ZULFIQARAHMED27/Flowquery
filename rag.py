# rag.py
"""
Retrieval Augmented Generation components
"""
from typing import List, Dict, Any, Optional
from langchain.schema import Document
from vectorstore_utils import load_vectorstore, similarity_search

class DocumentRetriever:
    """Class for retrieving relevant documents from a vector store"""
    
    def __init__(self, index_name: str = "faiss_index", model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the retriever
        
        Args:
            index_name: Path to the FAISS index
            model_name: SentenceTransformer model to use
        """
        self.index_name = index_name
        self.model_name = model_name
        self.vectorstore = None
        
    def load(self) -> bool:
        """
        Load the vector store
        
        Returns:
            True if loaded successfully, False otherwise
        """
        self.vectorstore = load_vectorstore(self.index_name)
        return self.vectorstore is not None
        
    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        """
        Retrieve relevant documents for a query
        
        Args:
            query: The user's query string
            k: Number of documents to retrieve
            
        Returns:
            List of relevant Document objects
        """
        if not self.vectorstore:
            if not self.load():
                print("Error: Vector store not loaded")
                return []
                
        return similarity_search(query, self.vectorstore, k, self.model_name)
        
    def format_retrieval_results(self, docs: List[Document]) -> str:
        """
        Format retrieved documents for display
        
        Args:
            docs: List of retrieved Document objects
            
        Returns:
            Formatted string with document contents
        """
        if not docs:
            return "No relevant information found."
            
        result = []
        for i, doc in enumerate(docs):
            # Extract metadata if available
            metadata = ""
            if hasattr(doc, 'metadata') and doc.metadata:
                metadata = f" [Source: {doc.metadata.get('source', 'Unknown')}]"
                
            result.append(f"Document {i+1}{metadata}:\n{doc.page_content}\n")
            
        return "\n".join(result)
        
class RAGSystem:
    """Complete RAG system with retrieval and optional answer generation"""
    
    def __init__(self, index_name: str = "faiss_index", llm=None):
        """
        Initialize the RAG system
        
        Args:
            index_name: Path to the FAISS index
            llm: Optional language model for answer generation
        """
        self.retriever = DocumentRetriever(index_name)
        self.llm = llm  # Can be None for retrieval-only mode
        
    def query(self, user_query: str, k: int = 5) -> Dict[str, Any]:
        """
        Process a user query through the RAG pipeline
        
        Args:
            user_query: The user's question
            k: Number of documents to retrieve
            
        Returns:
            Dictionary with retrieved documents and generated answer (if LLM is available)
        """
        # Retrieve relevant documents
        docs = self.retriever.retrieve(user_query, k)
        
        result = {
            "query": user_query,
            "retrieved_docs": docs,
            "formatted_docs": self.retriever.format_retrieval_results(docs),
            "answer": None
        }
        
        # Generate answer if LLM is available
        if self.llm and docs:
            # This is where you would integrate with a local LLM
            # For now, we'll leave this as a placeholder
            context = "\n\n".join([doc.page_content for doc in docs])
            # result["answer"] = self.llm.generate_answer(user_query, context)
            # For now, just note that generation is not implemented
            result["answer"] = "(Answer generation requires an LLM integration)"
            
        return result