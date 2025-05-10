import streamlit as st

st.set_page_config(page_title="Pricing Plans", layout="centered")

st.title("💼 Ask WildLaw Pricing Plans")
st.markdown("**Built for landowners, public bodies, and professionals working with environmental law.**")

st.subheader("Choose the plan that's right for you")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔓 Free Plan")
    st.markdown("""
    - 1 question per day  
    - Natural language search  
    - Public guidance summaries  
    - Basic source links  
    """)
    st.button("Start Free", key="free")

with col2:
    st.markdown("### 🌿 Pro Plan\n£10 / month")
    st.markdown("""
    - Unlimited questions  
    - Postcode-specific advice  
    - Legal Check Mode (quoted law)  
    - Interactive SSSI Consent Guidance  
    - Consent Application Tracker  
    - Landowner Education Hub  
    - Public Body Compliance Checklist  
    - Priority access & smart follow-ups  
    """)
    st.button("Upgrade to Pro", key="pro")

with col3:
    st.markdown("### 🏢 Organisation Portal")
    st.markdown("""
    - Team dashboard & usage analytics  
    - Custom branding  
    - Internal policy ingestion  
    - Dedicated support & onboarding  
    - Invoice billing  
    - NE & DEFRA integration support  
    """)
    st.button("Register Interest", key="org")

st.markdown("---")

st.subheader("What others are saying")
st.markdown("""
> “It’s screening questions so people can spend time where it matters most.”  
> — Adviser, Natural England

> “Our biggest legal risk is confusion. Ask WildLaw helps make the law usable.”  
> — SSSI landowner

> “If this saves just 10 minutes per adviser per day, it could save NE hundreds of thousands.”  
> — DEFRA-linked project lead
""")

st.markdown("📬 **Interested in Pro or Organisation access?**")
st.page_link("pages/Register.py", label="🔗 Register your interest now", icon="📄")

st.markdown("🤔 Not sure yet? [Learn what Ask WildLaw does](./Product)")
