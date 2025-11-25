# app.py — Main app (now clean and readable!)
import streamlit as st
from langchain_groq import ChatGroq

# Local imports
from config import GROQ_API_KEY
from memory import initialize_session, start_new_chat
from rag import get_retriever
from ui.components import login_button
from ui.sidebar import render_sidebar
from ui.mood_screen import render_mood_screen

# === App Setup ===
st.set_page_config(page_title="Comfy • Instapreps AI", page_icon="sparkles", layout="centered")
login_button()
initialize_session()

# === Main Logic ===
render_sidebar()

if st.session_state.current_chat is None:
    render_mood_screen()
else:
    idx = st.session_state.current_chat
    mood = st.session_state.chat_history[idx].get("mood", "curious")
    st.title("Comfy")
    st.caption(f"Feeling {mood.capitalize()} today")

    # Show messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Talk to Comfy..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                retriever = get_retriever()
                context = "\n\n".join([d.page_content for d in retriever.invoke(prompt)]) if retriever else ""
                history = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[:-1]])
                full_prompt = f"Context: {context}\nHistory: {history}\nHuman: {prompt}\nComfy:"

                reply = ChatGroq(model="llama-3.3-70b-versatile").invoke(full_prompt).content

                st.write(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})

                if len(st.session_state.messages) <= 3:
                    title = prompt[:30] + ("..." if len(prompt)>30 else "")
                    st.session_state.chat_history[idx]["title"] = title
                    st.rerun()
