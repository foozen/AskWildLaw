import streamlit as st

st.set_page_config(page_title="What is Ask WildLaw?", layout="centered")

st.title("🌿 What is Ask WildLaw?")
st.markdown("**Your intelligent legal assistant for UK environmental law.**")

st.markdown("""
Ask WildLaw helps landowners, advisers, NGOs and public bodies understand and apply UK environmental law with confidence — starting with the Wildlife and Countryside Act 1981.

No more digging through PDFs or waiting for replies. Just ask a question and get a useful answer — backed by legislation, guidance, and Natural England procedures.
""")

st.subheader("🧠 What It Does")
st.markdown("""
- 🤖 Understands natural language questions  
- 📍 Uses your postcode to tailor advice  
- 🔍 Legal Check Mode for quoted sections  
- 📚 References law and NE guidance  
- 🧾 Suggests next steps, forms, and contacts  
""")

st.subheader("🌿 Pro Tools for Real-World Use")

st.markdown("""
- ✅ **Interactive SSSI Consent Guidance**  
  Know when and how to submit a Section 28E notice.

- ✅ **Consent Application Tracker**  
  Track deadlines and application stages.

- ✅ **Landowner Education Hub**  
  Learn what you’re responsible for — in plain English.

- ✅ **Public Body Compliance Checklist**  
  Quickly assess if your organisation is meeting its legal duties under the WCA.
""")

st.subheader("⚙️ Coming Soon")
st.markdown("""
- Licensing assistant  
- Habitat restoration support  
- Organisation portal with custom ingestion  
""")

st.page_link("pages/Pricing.py", label="💸 View Pricing Plans", icon="💸")
st.page_link("pages/Register.py", label="📬 Register Interest", icon="📝")
