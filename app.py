import streamlit as st
from storygen import generate_story

st.set_page_config(page_title="AI Story Generator", page_icon="📖")
st.title("📖 AI Story Generator")

prompt = st.text_input("Enter your story prompt", "A time traveler visits ancient Egypt")

if st.button("Generate Story"):
    with st.spinner("Crafting your story..."):
        story = generate_story(prompt)
        st.markdown("### ✨ Generated Story")
        st.write(story)
