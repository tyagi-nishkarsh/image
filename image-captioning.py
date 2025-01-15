import torch
import streamlit as st
from PIL import Image
from TTS.api import TTS  # Import Coqui TTS
import os

# Initialize Coqui TTS model (English model example)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def generate_audio(text):
    """Generate audio from text using Coqui TTS."""
    audio_file_path = "output.wav"
    tts.save_wav(text, path=audio_file_path)
    return audio_file_path

def caption_my_image(pil_image):
    """Generate caption and audio from image."""
    # Here you can integrate a captioning model, like BLIP
    # For simplicity, let's assume a placeholder caption for now
    semantics = "This is a placeholder caption for the uploaded image."
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
