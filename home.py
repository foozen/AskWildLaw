import streamlit as st
import zipfile
import os
import openai

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# ───────────────────────────────
# Setup: unzip prebuilt vectorstore if needed
# ───────────────────────────────
VECTORSTORE_DIR = "wildlaw_vectorstore"
VECTORSTORE_ZIP = "wildlaw_vectorstore.zip"
REQUIRED_FILES = ["index.faiss", "index.pkl"]

if not os.path.exists(VECTORSTORE_DIR) or not all(os.path.exists(os.path.join(VECTORSTORE_DIR, f)) for f in REQUIRED_FILES):
    if os.path.exists(VECTORSTORE_ZIP):
        with zipfile.ZipFile(VECTORSTORE_ZIP, "r") as zip_ref:
            zip_ref.extractall(VECTORSTORE_DIR)
        st.info("✅ Vectorstore unzipped.")
    else:
        st.error("❌ vectorstore zip not found.")
        st.stop()

# ───────────────────────────────
# Load OpenAI API Key
# ───────────────────────────────
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ───────────────────────────────
# Load vectorstore (no cloud embedding!)
# ───────────────────────────────
vectorstore = FAISS.load_local(
    VECTORSTORE_DIR,
    OpenAIEmbeddings(openai_api_key=openai.api_key),
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3),
    retriever=retriever,
    return_source_documents=True
)

# ... (the rest of your Streamlit UI follows — unchanged)
