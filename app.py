# app.py
"""
Main application with command-line interface
"""
import os
import argparse
from rag import RAGSystem

def print_header():
    """Print application header"""
    print("\n" + "="*50)
    print("📚 Document Q&A Bot 📚".center(50))
    print("="*50)
    print("Type 'exit', 'quit', or Ctrl+C to end the session")
    print("Type 'help' for usage information")
    print("-"*50 + "\n")

def print_help():
    """Print help information"""
    print("\nUsage:")
    print("  - Ask any question about your documents")
    print("  - Type 'exit' or 'quit' to end the session")
    print("  - Type 'help' to see this message")
    print("  - Type 'source' to change the index source")
    print("\nExamples:")
    print("  > What topics are covered in the documentation?")
    print("  > How do I implement feature X?")
    print("  > Find information about error handling")
    print()

def interactive_mode(rag_system, show_docs=True):
    """
    Run interactive query mode
    
    Args:
        rag_system: Initialized RAG system
        show_docs: Whether to show retrieved documents
    """
    print_header()
    
    try:
        while True:
            # Get user query
            query = input("\n🔍 Ask me about your documents: ")
            query = query.strip()
            
            # Handle special commands
            if query.lower() in ['exit', 'quit']:
                print("\nExiting. Thank you for using Document Q&A Bot!")
                break
            elif query.lower() == 'help':
                print_help()
                continue
            elif query.lower() == 'source':
                new_index = input("Enter path to index folder: ")
                if os.path.exists(new_index):
                    rag_system = RAGSystem(new_index)
                    print(f"Now using index from: {new_index}")
                else:
                    print(f"Error: Index not found at {new_index}")
                continue
            elif not query:
                continue
                
            # Process query
            print("\nSearching for relevant information...")
            result = rag_system.query(query)
            
            # Display results
            if show_docs:
                print("\n📄 RETRIEVED DOCUMENTS:")
                print(result["formatted_docs"])
                
            # If we had an LLM integration, we would show the generated answer here
            if result["answer"]:
                print("\n🤖 ANSWER:")
                print(result["answer"])
            
    except KeyboardInterrupt:
        print("\n\nExiting. Thank you for using Document Q&A Bot!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Document Q&A Bot")
    parser.add_argument("--index", "-i", default="faiss_index",
                      help="Path to the FAISS index folder")
    parser.add_argument("--hide-docs", action="store_true",
                      help="Hide retrieved documents and show only answers")
    
    args = parser.parse_args()
    
    # Initialize RAG system
    rag_system = RAGSystem(args.index)
    
    # Start interactive mode
    interactive_mode(rag_system, not args.hide_docs)

if __name__ == "__main__":
    main()