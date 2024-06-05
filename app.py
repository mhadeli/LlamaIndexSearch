import os
from dotenv import load_dotenv
import streamlit as st
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.response.pprint_utils import pprint_response

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Define persistence directory
PERSIST_DIR = "./storage"

# Function to load or create index
def get_index():
    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index

# Load or create the index
index = get_index()

# Set up retriever and query engine
retriever = VectorIndexRetriever(index=index, similarity_top_k=4)
postprocessor = SimilarityPostprocessor(similarity_cutoff=0.80)
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    node_postprocessors=[postprocessor]
)

# Streamlit interface
st.title("Document Query Interface")

query = st.text_input("Enter your query:", "")

if st.button("Submit"):
    if query:
        response = query_engine.query(query)
        st.write("### Response")
        st.write(response)
        st.write("### Sources")
        st.write(pprint_response(response, show_source=True))
    else:
        st.error("Please enter a query.")