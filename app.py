import streamlit as st
import google.generativeai as genai
import os

# ========== CONFIG ==========
ALLOWED_EMAILS = [
    "user1@gmail.com",
    "user2@gmail.com"
]

# ========== AUTH ==========
email = st.text_input("Masukkan email")

if email not in ALLOWED_EMAILS:
    st.warning("Akses ditolak")
    st.stop()

# ========== GEMINI ==========
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
    <<< PROMPT RAHASIA ANDA DI SINI >>>
    """
)

st.title("Aplikasi AI Anda")

user_input = st.text_area("Input")

if st.button("Kirim"):
    response = model.generate_content(user_input)
    st.write(response.text)
