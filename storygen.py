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
            st.error("🔑 GEMINI_API_KEY not found. Please add it to secrets.toml or .env.")
            st.stop()
        return api_key

# Configure Gemini API
genai.configure(api_key=get_gemini_api_key())
model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_story(prompt):
    """Generate story from user prompt using Gemini."""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def generate_moral_or_summary(story_text):
    """Generate summary or moral of the story using Gemini."""
    try:
        prompt = f"Give a concise summary or moral of this short story:\n\n{story_text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
