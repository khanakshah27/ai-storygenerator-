import os
import streamlit as st
import google.generativeai as genai

def get_gemini_api_key():
    """Get Gemini API key from Streamlit secrets or environment variables."""
    try:
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            st.error("🔑 GEMINI_API_KEY not found. Please add it to your Streamlit secrets or .env file.")
            st.stop()
        return api_key

# Configure Gemini
genai.configure(api_key=get_gemini_api_key())
model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_story(prompt):
    try:
        response = model.generate_content(f"Write a short story based on this prompt: {prompt}")
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
