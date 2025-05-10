import streamlit as st
import os
import zipfile
import openai
st.info("✅ home.py is using prebuilt vectorstore only.")

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# ─────────────────────────────────────
# 1. Load vectorstore (prebuilt only)
# ─────────────────────────────────────
if not os.path.exists("wildlaw_vectorstore"):
    with zipfile.ZipFile("wildlaw_vectorstore.zip", "r") as zip_ref:
        zip_ref.extractall("wildlaw_vectorstore")

embedding = OpenAIEmbeddings(openai_api_key=st.secrets["OPENAI_API_KEY"])

vectorstore = FAISS.load_local(
    "wildlaw_vectorstore",
    embedding,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3),
    retriever=retriever,
    return_source_documents=True
)

# ─────────────────────────────────────
# 2. Streamlit UI setup
# ─────────────────────────────────────
st.set_page_config(page_title="Ask WildLaw", layout="centered")

if "tier" not in st.session_state:
    st.session_state["tier"] = None
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

st.title("🌿 Ask WildLaw")
st.markdown("Your AI assistant for UK environmental law and guidance.")

# Simulated login
with st.expander("🔐 Log in to your account"):
    access_level = st.selectbox("Choose your access level:", ["Select...", "Free User", "Pro User"])
    if access_level != "Select...":
        st.session_state["tier"] = access_level.lower().replace(" ", "_")

st.markdown(
    "<small>New here? <a href='./Product' target='_self'>Learn what Ask WildLaw does</a> | "
    "<a href='./Pricing' target='_self'>View plans and pricing</a></small>",
    unsafe_allow_html=True
)

if not st.session_state["tier"]:
    st.info("Please log in to begin.")
    st.stop()

# ─────────────────────────────────────
# 3. Question input
# ─────────────────────────────────────
question = st.text_input("What would you like to ask?")
postcode = st.text_input("Enter your postcode (optional)")

legal_check = False
if st.session_state["tier"] == "pro_user":
    legal_check = st.checkbox("🔍 Legal Check Mode (Quote exact law when possible)")

if st.button("Submit your question"):
    if not question.strip():
        st.warning("Please enter a question.")
    elif st.session_state["tier"] == "free_user" and st.session_state["submitted"]:
        st.error("🚫 Free users can only ask one question per day. Upgrade to Pro for full access. [View plans](./Pricing)", icon="🚫")
    else:
        with st.spinner("Searching the law and guidance..."):
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

            try:
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
                st.error(f"Something went wrong: {e}")
