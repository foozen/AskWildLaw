import streamlit as st

st.set_page_config(page_title="Register Interest", layout="centered")

st.title("📄 Register Your Interest")
st.markdown(
    "Let us know if you're interested in **Ask WildLaw Pro** or the **Organisation Portal**. "
    "We’ll get in touch when we launch paid plans or early access pilots."
)

with st.form("register_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    role = st.text_input("Your Role or Organisation (optional)")
    interest = st.selectbox("Interested in:", ["Select...", "Pro Account", "Organisation Portal", "Both"])
    notes = st.text_area("Any notes or questions? (optional)")

    submitted = st.form_submit_button("📩 Submit")
    if submitted:
        if not name or not email or interest == "Select...":
            st.warning("Please complete all required fields.")
        else:
            st.success("Thank you! We'll be in touch when plans become available.")
            # In future: add backend storage/email here
