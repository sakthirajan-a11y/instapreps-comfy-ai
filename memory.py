# memory.py
import streamlit as st
from datetime import datetime
from config import MOOD_GREETINGS

def start_new_chat(mood=None):
    greeting = MOOD_GREETINGS.get(mood, "Hey there! I'm Comfy, your AI buddy. How can I help?")
    
    new_chat = {
        "title": f"{mood.capitalize()} Chat" if mood else "New Chat",
        "mood": mood or "curious",
        "messages": [{"role": "assistant", "content": greeting}],
        "created": datetime.now(),
        "last_updated": datetime.now()
    }
    
    st.session_state.chat_history.append(new_chat)
    st.session_state.current_chat = len(st.session_state.chat_history) - 1
    st.session_state.messages = new_chat["messages"]

def load_chat(index):
    chat = st.session_state.chat_history[index]
    st.session_state.current_chat = index
    st.session_state.messages = chat["messages"].copy()

def initialize_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "current_chat" not in st.session_state:
        st.session_state.current_chat = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
