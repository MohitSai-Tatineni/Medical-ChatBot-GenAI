from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Pinecone API Key and Environment
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
print(f"Connected to Pinecone API KEY: {PINECONE_API_KEY}")

embeddings = download_hugging_face_embeddings()
print(f"Downloaded the Embedding model..")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Define the index name
index_name = "medicalbot" 

# Connect to an existing index
index = pc.Index(index_name)
print(f"Connected to Pinecone index: {index_name}")

docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
print(f"Docsearch is ready!")

# Create a PromptTemplate object
PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)
print(f"Created a PromptTemplate object..")

# Step 3: Create an LLMChain
chain_type_kwargs = {"prompt" : PROMPT}

# Initialize LLM with CTransformers
llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",  # Path to the Llama 2 model file
    model_type="llama",  # Specify model type
    config={
        "max_new_tokens": 512,  # Maximum tokens to generate
        "temperature": 0.8      # Sampling temperature
    }
)
print(f"Loaded the Llama 2 model..")

retriever = docsearch.as_retriever(search_kwargs={"k": 3, "namespace": "medical-data"})
print(f"Retriever Function is ready..")

# Initialize the RetrievalQA object
retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,  # Your initialized Llama 2 model
    retriever=retriever,  # The retriever from docsearch
    return_source_documents=True,  # Optional: include source documents in the output
    chain_type="stuff",  # Default chain type for combining retrieved data
    chain_type_kwargs={"prompt": PROMPT},  # Custom prompt template
)
print(f"RAG Pipeline sucessfully set!!")

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = retrieval_qa({"query": input})
    print("Response : ", response["result"])
    return str(response["result"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)