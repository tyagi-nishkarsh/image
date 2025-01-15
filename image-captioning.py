import torch
import streamlit as st
from PIL import Image
import scipy.io.wavfile as wavfile
from transformers import pipeline

device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize the pipelines
caption_image = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large", device=device)
narrator = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")

def generate_audio(text):
    """Generate audio from text."""
    narrated_text = narrator(text)
    audio_file_path = "output.wav"
    wavfile.write(audio_file_path, rate=narrated_text["sampling_rate"], data=narrated_text["audio"][0])
    return audio_file_path

def caption_my_image(pil_image):
    """Generate caption and audio from image."""
    semantics = caption_image(images=pil_image)[0]['generated_text']
    audio_file = generate_audio(semantics)
    return semantics, audio_file

# Streamlit UI
st.title("@GenAILearniverse Project 8: Image Captioning")
st.write("This application will generate captions and audio descriptions for the uploaded image.")

# Upload image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
if uploaded_image:
    # Open image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate caption and audio
    if st.button("Generate Caption and Audio"):
        with st.spinner("Processing..."):
            caption, audio_path = caption_my_image(image)

            # Display caption and audio
            st.subheader("Generated Caption:")
            st.write(caption)
            st.audio(audio_path)

