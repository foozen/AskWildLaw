import streamlit as st
import os
import openai
import zipfile
import csv

from datetime import datetime
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="Ask WildLaw", layout="centered")

st.title("🌿 Ask WildLaw")
st.markdown("Your AI assistant for UK environmental law and guidance.")

# Ensure OPENAI_API_KEY exists
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except Exception as e:
    st.error("🔐 OpenAI API key not found. Please set it in Streamlit Secrets.")
    st.stop()

# Extract vectorstore zip if not already done
if not os.path.exists("wildlaw_vectorstore"):
    if os.path.exists("wildlaw_vectorstore.zip"):
        with zipfile.ZipFile("wildlaw_vectorstore.zip", "r") as zip_ref:
            zip_ref.extractall("wildlaw_vectorstore")
        st.success("✅ Vectorstore unzipped.")
    else:
        st.error("❌ Vectorstore not found.")
        st.stop()

# Try to load vectorstore
try:
    vectorstore = FAISS.load_local(
        "wildlaw_vectorstore",
        OpenAIEmbeddings(openai_api_key=openai.api_key),
        allow_dangerous_deserialization=True
    )
except Exception as e:
    st.error(f"💥 Failed to load vectorstore: {e}")
    st.stop()

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3),
    retriever=retriever,
    return_source_documents=True
)

# Log the question, answer, timestamp, and postcode
log_path = "qa_log.csv"
log_entry = {
    "timestamp": datetime.now().isoformat(),
    "user_type": st.session_state["tier"],
    "postcode": postcode,
    "question": question,
    "answer": result["result"]
}

file_exists = os.path.exists(log_path)
with open(log_path, "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=log_entry.keys())
    if not file_exists:
        writer.writeheader()
    writer.writerow(log_entry)


# Simulated login
if "tier" not in st.session_state:
    st.session_state["tier"] = None
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

with st.expander("🔐 Log in to your account"):
    access_level = st.selectbox("Choose your access level:", ["Select...", "Free User", "Pro User"])
    if access_level != "Select...":
        st.session_state["tier"] = access_level.lower().replace(" ", "_")

# Redirect if not logged in
if not st.session_state["tier"]:
    st.info("Please log in to begin.")
    st.stop()

# User input section
question = st.text_input("What would you like to ask?")
postcode = st.text_input("Enter your postcode (optional)")

legal_check = False
if st.session_state["tier"] == "pro_user":
    legal_check = st.checkbox("🔍 Legal Check Mode (Quote exact law when possible)")

if st.button("Submit your question"):
    if not question.strip():
        st.warning("Please enter a question.")
    elif st.session_state["tier"] == "free_user" and st.session_state["submitted"]:
        st.error("🚫 Free users can only ask one question per day. Upgrade to Pro for full access.")
    else:
        with st.spinner("Searching the law and guidance..."):
            try:
                system_prompt = (
                    f"You are a legal assistant for Natural England. A landowner has asked: '{question}' "
                    f"with postcode '{postcode}'. Use only the official guidance and law provided to answer. "
                )
                if legal_check:
                    system_prompt += (
                        "Quote directly from the documents whenever possible. "
                        "Use clear, formal language and avoid making assumptions beyond the source content. "
                        "If unsure, state that clearly and suggest who to contact."
                    )
                else:
                    system_prompt += (
                        "Summarise the key points clearly and helpfully. Provide practical next steps, and if unclear, "
                        "suggest what the user should ask or check with the local authority or Natural England."
                    )

                result = qa_chain(system_prompt)
                st.session_state["submitted"] = True

                st.markdown("### 🧾 Answer:")
                st.markdown(result["result"])

                st.markdown("### 👍 Was this answer helpful?")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👍 Yes"):
                        st.success("Thanks for your feedback!")
                with col2:
                    if st.button("👎 No"):
                        st.warning("Thanks — we’ll use this to improve future answers.")

                st.markdown("### 📚 Sources used:")
                used_sources = set()
                for doc in result["source_documents"]:
                    src = doc.metadata.get("source", "Unknown")
                    if src not in used_sources:
                        st.markdown(f"- `{src}`")
                        used_sources.add(src)

            except Exception as e:
                st.error(f"❌ An error occurred while processing your question: {e}")
