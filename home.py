import streamlit as st
from PIL import Image

def app():
    st.markdown("# Emotion Classification using Deep Learning and NLP")

    # Image 1
    image_path_1 = 'text_images/nlp_home.png'
    image_1 = Image.open(image_path_1)
    st.image(image_1, caption='', use_column_width=True)

    st.markdown("""
    Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.
    """)

    # Image 2 (Centered)
    image_path_2 = 'text_images/abcd.png'
    image_2 = Image.open(image_path_2)

    col1, col2, col3 = st.columns(3)
    col2.image(image_2, caption='', use_column_width=True)

    st.markdown("## Project Phase - 1")
    st.markdown("### Emotion Video Classification")

    image_path_3 = 'text_images/video_emotions.png'
    image_3 = Image.open(image_path_3)
    st.image(image_3, caption='', use_column_width=True)

    st.markdown("## Project Phase - 2")
    st.markdown("### Emotion Text Classification")

    st.markdown("## Project Phase - 3")
    st.markdown("### Text To Speech")

    image_path_4 = 'text_images/text-to-speech.png'
    image_4 = Image.open(image_path_4)
    st.image(image_4, caption='', use_column_width=True)

    st.markdown("## Project Phase - 4")
    st.markdown("### Speech To Text")

    image_path_5 = 'text_images/speech-text.png'
    image_5 = Image.open(image_path_5)
    st.image(image_5, caption='', use_column_width=True)

if __name__ == "__main__":
    app()
