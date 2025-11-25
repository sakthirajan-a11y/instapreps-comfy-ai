# rag.py
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

@st.cache_resource
def get_retriever():
    if not os.path.exists("data"):
        os.makedirs("data")
        return None
    
    loader = PyPDFDirectoryLoader("data")
    docs = loader.load()
    if not docs:
        return None

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings, collection_name="comfy_kb")
    return vectorstore.as_retriever(search_kwargs={"k": 4})
