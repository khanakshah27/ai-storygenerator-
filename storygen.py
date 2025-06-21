import openai
import os
import streamlit as st  # required to use st.secrets safely

def get_openai_api_key():
    """Get OpenAI API key from Streamlit secrets or environment variables."""
    try:
        return st.secrets["OPENAI_API_KEY"]
    except (KeyError, FileNotFoundError):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("🔑 OPENAI_API_KEY not found. Please add it to your Streamlit secrets or .env file.")
            st.stop()
        return api_key

openai.api_key = get_openai_api_key()

def generate_story(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative writing assistant."},
                {"role": "user", "content": f"Write a short story based on this prompt: {prompt}"}
            ],
            max_tokens=500,
            temperature=0.8
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {e}"
