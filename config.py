from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found! Add it in Streamlit Cloud → Manage app → Secrets")
    st.stop()

MOOD_GREETINGS = {
    "excited": "YAY! I'm super excited too! Let's make today amazing!",
    "chill": "Ahh, chill vibes only. I'm here, relaxed and ready to help.",
    "focused": "Locked in! I'm focused and ready to crush your doubts.",
    "tired": "I feel you. Let's take it easy — I'm here when you need me.",
    "curious": "Ooh, curiosity is my favorite! Ask me anything — I'm all ears!"
}

QUICK_LINKS = [
    ("Confidence Test", "confidencetest"),
    ("Startup Power", "startuppower"),
    ("Feed", "feed")
]
