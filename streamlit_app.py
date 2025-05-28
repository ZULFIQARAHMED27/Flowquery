# streamlit_app.py
import streamlit as st
import tempfile
import os
import sys
import traceback

# Add current directory to path for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Page configuration
st.set_page_config(page_title="🔥 FlowQuery", layout="wide")

# Debug information (remove in production)
with st.expander("🔧 Debug Info", expanded=False):
    st.write(f"Current working directory: {os.getcwd()}")
    st.write(f"Python path: {sys.path[:3]}...")  # Show first 3 paths
    st.write(f"Files in current directory: {[f for f in os.listdir('.') if f.endswith('.py')]}")

# Import modules with error handling
try:
    from rag import RAGSystem
    from ingest import process_documents
    st.success("✅ Modules imported successfully!", icon="✅")
except ImportError as e:
    st.error(f"❌ Import Error: {str(e)}")
    st.error("Make sure 'rag.py' and 'ingest.py' are in the same directory as this file.")
    st.stop()
except Exception as e:
    st.error(f"❌ Unexpected error during imports: {str(e)}")
    st.error(f"Traceback: {traceback.format_exc()}")
    st.stop()

# Main title and description
st.title("🔥 FlowQuery - AI Document Assistant")
st.caption("Experience seamless document conversations with intelligent search and AI-powered insights.")

# Sidebar for document upload and processing
st.sidebar.header("📄 Upload Document Chunks")
st.sidebar.caption("Supported formats: JSON, PDF, DOCX, TXT")

uploaded_file = st.sidebar.file_uploader(
    "Choose a document file", 
    type=["json", "pdf", "docx", "txt"],
    help="Upload a document to create a searchable index"
)

# Configuration options
index_name = st.sidebar.text_input(
    "Index Name", 
    value="faiss_index",
    help="Name for your document index"
)

embed_model = st.sidebar.text_input(
    "Embedding Model", 
    value="all-MiniLM-L6-v2",
    help="Sentence transformer model for embeddings"
)

# Document processing section
if uploaded_file:
    st.sidebar.info(f"📄 File loaded: {uploaded_file.name}")
    
    if st.sidebar.button("🚀 Ingest & Index", type="primary"):
        # Validate file extension
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        supported_extensions = [".json", ".pdf", ".docx", ".txt"]
        
        if ext not in supported_extensions:
            st.sidebar.error(f"❌ Unsupported file type: {ext}")
            st.sidebar.error(f"Supported types: {', '.join(supported_extensions)}")
        else:
            tmp_path = None
            try:
                # Create temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                
                st.sidebar.info(f"📁 Temporary file created: {os.path.basename(tmp_path)}")
                
                # Process documents with progress indicator
                with st.spinner("🔄 Processing and indexing documents..."):
                    success = process_documents(tmp_path, index_name, embed_model)
                
                if success:
                    st.sidebar.success("✅ Documents indexed successfully!")
                    st.sidebar.balloons()
                else:
                    st.sidebar.error("❌ Failed to index documents.")
                    
            except Exception as e:
                st.sidebar.error(f"❌ Error during processing: {str(e)}")
                st.sidebar.error(f"Traceback: {traceback.format_exc()}")
            finally:
                # Clean up temporary file
                if tmp_path and os.path.exists(tmp_path):
                    try:
                        os.unlink(tmp_path)
                        st.sidebar.info("🗑️ Temporary file cleaned up")
                    except Exception as e:
                        st.sidebar.warning(f"⚠️ Could not clean up temp file: {str(e)}")

# Main interface for querying
st.header("🔍 Ask a Question")
st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_input(
        "Enter your question:", 
        placeholder="What would you like to know about your documents?",
        help="Ask any question about the uploaded documents"
    )

with col2:
    num_results = st.slider(
        "Results to retrieve", 
        min_value=1, 
        max_value=10, 
        value=5,
        help="Number of relevant documents to retrieve"
    )

# Search functionality
if st.button("🔍 Search", type="primary", disabled=not query.strip()):
    if not query.strip():
        st.warning("⚠️ Please enter a question to search.")
    else:
        try:
            with st.spinner("🔄 Retrieving relevant documents..."):
                # Initialize RAG system
                rag = RAGSystem(index_name)
                results = rag.query(query, k=num_results)
            
            # Display results
            st.markdown("### 📄 Retrieved Documents")
            
            if results and "formatted_docs" in results:
                # Create expandable section for documents
                with st.expander("📋 View Retrieved Documents", expanded=True):
                    st.code(results["formatted_docs"], language="text")
                
                # Display generated answer if available
                if results.get("answer"):
                    st.markdown("### 🤖 Generated Answer")
                    st.success(results["answer"])
                else:
                    st.info("ℹ️ No generated answer available. Showing retrieved documents only.")
            else:
                st.warning("⚠️ No relevant documents found for your query.")
                
        except FileNotFoundError:
            st.error(f"❌ Index '{index_name}' not found. Please upload and index documents first.")
        except Exception as e:
            st.error(f"❌ Error during search: {str(e)}")
            st.error(f"Traceback: {traceback.format_exc()}")

# Sidebar status information
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Status")

# Check if index exists
index_path = f"{index_name}.faiss" if not index_name.endswith('.faiss') else index_name
if os.path.exists(index_path):
    st.sidebar.success(f"✅ Index '{index_name}' is ready")
else:
    st.sidebar.warning(f"⚠️ Index '{index_name}' not found")
    st.sidebar.info("Upload a document to create an index")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>🔥 FlowQuery - Where Documents Meet Intelligence</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Additional CSS for better styling and fixing input visibility
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
    }
    
    /* Fix text input visibility */
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #cccccc !important;
    }
    
    /* Fix text input focus state */
    .stTextInput > div > div > input:focus {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #ff6b6b !important;
        box-shadow: 0 0 0 0.2rem rgba(255, 107, 107, 0.25) !important;
    }
    
    /* Fix selectbox visibility */
    .stSelectbox > div > div > select {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #cccccc !important;
    }
    
    /* Fix number input visibility */
    .stNumberInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #cccccc !important;
    }
    
    /* Fix slider text */
    .stSlider > div > div > div > div {
        color: #000000 !important;
    }
    
    /* Ensure placeholder text is visible */
    .stTextInput > div > div > input::placeholder {
        color: #888888 !important;
        opacity: 1 !important;
    }
    
    /* Fix sidebar inputs */
    .css-1d391kg .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Alternative sidebar selector */
    div[data-testid="stSidebar"] .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)