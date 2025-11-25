from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found! Add it in Streamlit Cloud → Manage app → Secrets")
    st.stop()
