import streamlit as st
from process_audio import reduce_noise
import os

st.set_page_config(page_title="Audio Class Clarity Booster", layout="centered")
st.title("🎧 Audio Class Clarity Booster")
st.markdown("Upload a noisy audio file and get a clearer version for lectures, bhajans, or talks.")

uploaded_file = st.file_uploader("Upload your audio file (.mp3, .wav)", type=["mp3", "wav"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/mp3")

    with open("temp_input.wav", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing..."):
        cleaned_path = reduce_noise("temp_input.wav")

    st.success("✅ Audio cleaned successfully!")
    st.audio(cleaned_path, format="audio/wav")

    with open(cleaned_path, "rb") as f:
        st.download_button("⬇️ Download Cleaned Audio", f, file_name="cleaned_audio.wav")

    os.remove("temp_input.wav")
    os.remove(cleaned_path)
