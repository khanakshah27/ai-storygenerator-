import streamlit as st
from storygen import generate_story, generate_moral_or_summary

st.set_page_config(page_title="Your AI Story Crafter")
st.title("Your AI Story Crafter")

st.markdown("Generate unique short stories with genre, tone, and moral!")

genre = st.selectbox("Choose a genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Adventure"])
tone = st.selectbox("Select a tone", ["Wholesome", "Dark", "Humorous", "Emotional", "Inspirational"])

user_prompt = st.text_area("Your story idea", placeholder="e.g., A robot learns to paint...")

if st.button("✨ Generate Story"):
    with st.spinner("Spinning up your story..."):
        full_prompt = f"Write a {tone.lower()} short story in the {genre.lower()} genre based on this idea: {user_prompt}"
        story = generate_story(full_prompt)
        st.markdown("### 📖 Your Story")
        st.write(story)

        if st.button("💡 Show Moral or Summary"):
            with st.spinner("Extracting insight..."):
                moral = generate_moral_or_summary(story)
                st.markdown("### 🌟 Moral / Summary")
                st.write(moral)
