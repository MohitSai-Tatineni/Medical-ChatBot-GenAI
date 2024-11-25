from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


# Load and process data
extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Define the index name
index_name = "medicalbot"

# Create Pinecone index (if not already created)
pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

# Function to embed documents
def embed_documents(chunks, embedding_model):
    return [
        {
            "id": str(i),
            "values": embedding_model.embed_query(chunk.page_content),
            "metadata": {"text": chunk.page_content}
        }
        for i, chunk in enumerate(chunks)
    ]

# Embed the text chunks
embedded_data = embed_documents(text_chunks, embeddings)

# Function to chunk data into batches
def chunk_data(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Function to upsert data in batches
def upsert_batches(index, data, batch_size, namespace=""):
    for batch in chunk_data(data, batch_size):
        index.upsert(vectors=batch, namespace=namespace)
    print(f"Uploaded data in batches of {batch_size}.")

# Connect to the Pinecone index
index = pc.Index(index_name)

# Upsert data to Pinecone in batches
batch_size = 100  # Adjust the batch size as needed
namespace = "medical-data"  # Optional namespace for organizing data
upsert_batches(index, embedded_data, batch_size, namespace)

# Initialize docsearch using PineconeVectorStore
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

print("docsearch is ready for use!")
