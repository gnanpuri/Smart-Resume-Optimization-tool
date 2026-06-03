import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Initialize ChromaDB client (runs locally on your PC)
client = chromadb.Client()

# Initialize the embedding model (converts text to vectors)
embeddings = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def store_resume(resume_text, collection_name="resume"):
    """Split resume into chunks and store in ChromaDB"""
    
    # Step 1: Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,      # Each chunk is 500 characters
        chunk_overlap=50     # Chunks overlap by 50 characters
    )
    chunks = text_splitter.split_text(resume_text)
    
    # Step 2: Convert chunks to vectors
    vectors = embeddings.embed_documents(chunks)
    
    # Step 3: Store in ChromaDB
    collection = client.get_or_create_collection(collection_name)
    collection.add(
        documents=chunks,
        embeddings=vectors,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    
    return collection, chunks

def search_resume(query, collection, top_k=5):
    """Search for most relevant resume chunks for a given query"""
    
    # Convert query to vector
    query_vector = embeddings.embed_query(query)
    
    # Search ChromaDB for similar chunks
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )
    
    return results["documents"][0]