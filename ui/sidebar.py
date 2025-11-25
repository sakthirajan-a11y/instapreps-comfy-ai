# ui/sidebar.py
import streamlit as st
from config import QUICK_LINKS

def render_sidebar():
    with st.sidebar:
        st.image("https://em-content.zobj.net/source/telegram/358/smiling-face-with-hearts_1f970.webp", width=80)
        st.title("Comfy")

        if st.button("New Chat", use_container_width=True, type="primary"):
            from memory import start_new_chat
            start_new_chat()

        st.markdown("### Your Chats")
        if st.session_state.chat_history:
            for i, chat in enumerate(reversed(st.session_state.chat_history)):
                idx = len(st.session_state.chat_history) - 1 - i
                title = chat["title"]
                preview = chat["messages"][0]["content"][:40] + "..." if chat["messages"] else "New"
                if st.button(f"**{title}**\n_{preview}_", key=f"chat_{idx}", use_container_width=True):
                    from memory import load_chat
                    load_chat(idx)

        st.markdown("---")
        st.markdown("### Quick Tools")
        for name, url in QUICK_LINKS:
            st.markdown(f'<div style="margin:8px 0;padding:10px;background:#f0f2f6;border-radius:10px;text-align:center;"><a href="https://instapreps.com/{url}" target="_blank">{name}</a></div>', unsafe_allow_html=True)
        
        st.caption("Made with love by Sakthi @ Instapreps")
