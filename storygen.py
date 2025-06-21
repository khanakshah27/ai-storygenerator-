import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable

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
