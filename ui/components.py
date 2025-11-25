# ui/components.py
import streamlit as st

def login_button():
    st.markdown("""
    <div style="position:fixed;top:10px;right:20px;z-index:9999;">
        <a href="https://instapreps.com/login" target="_blank" 
           style="background:#4CAF50;color:white;padding:10px 24px;border-radius:30px;text-decoration:none;font-weight:bold;">
           Login
        </a>
    </div>
    """, unsafe_allow_html=True)
