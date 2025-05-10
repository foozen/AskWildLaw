import streamlit as st
import os
import zipfile

# Extract the vectorstore archive if not already extracted
if not os.path.exists("wildlaw_vectorstore"):
    with zipfile.ZipFile("wildlaw_vectorstore.zip", "r") as zip_ref:
        zip_ref.extractall("wildlaw_vectorstore")

st.set_page_config(page_title="Ask WildLaw", layout="centered")
st.title("🌿 Ask WildLaw")
st.info("✅ Loading prebuilt vectorstore for cloud use...")

# Load FAISS vectorstore
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

vectorstore = FAISS.load_local(
    "wildlaw_vectorstore",
    OpenAIEmbeddings(openai_api_key=st.secrets["OPENAI_API_KEY"]),
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3),
    retriever=retriever,
    return_source_documents=True
)

# ───────────────────────────── UI ─────────────────────────────
question = st.text_input("What would you like to ask?")
if st.button("Submit your question") and question:
    with st.spinner("Thinking..."):
        result = qa_chain.run(question)
        st.markdown("### 🧾 Answer:")
        st.write(result)
