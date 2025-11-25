# ui/mood_screen.py
import streamlit as st

def render_mood_screen():
    st.markdown("<h1 style='text-align:center;margin-top:80px;'>Hi, I am Comfy</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;color:#666;'>your AI companion</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#888;margin:40px 0;'>How do you feel today?</p>", unsafe_allow_html=True)

    cols = st.columns(5)
    moods = [("Excited", "excited"), ("Chill", "chill"), ("Focused", "focused"), ("Tired", "tired"), ("Curious", "curious")]
    for col, (label, mood) in zip(cols, moods):
        with col:
            if st.button(label, use_container_width=True):
                from memory import start_new_chat
                start_new_chat(mood=mood)
                st.rerun()

    st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)

    if prompt := st.chat_input("Or just ask me anything..."):
        from memory import start_new_chat
        start_new_chat(mood="curious")
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()
