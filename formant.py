import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa
import parselmouth  # For formant extraction using Praat
from parselmouth.praat import call

def extract_formants(audio_path):
    """Extracts the first two formants (F1, F2) for each word."""
    sound = parselmouth.Sound(audio_path)
    formants = []
    
    # Parameters for extracting formants - adjust as needed
    max_formant = 5500
    formant_object = call(sound, "To Formant (burg)", 0.025, 5, max_formant, 0.03, 50)
    
    # Extract formants for each 1-second slice (assuming each word is isolated and 1-second)
    for i in range(9):
        time = i  # Adjust timing if needed
        f1 = call(formant_object, "Get value at time", 1, time, 'Hertz', 'Linear')
        f2 = call(formant_object, "Get value at time", 2, time, 'Hertz', 'Linear')
        formants.append((f1, f2))
    return formants

def plot_formants(formants):
    """Plot formants in a 2D space."""
    f1_values = [f[0] for f in formants]
    f2_values = [f[1] for f in formants]

    # Create plot with inverted axes for F1 and F2
    plt.figure(figsize=(6, 6))
    plt.scatter(f2_values, f1_values)
    
    # Number each formant point from 1 to 9
    for i, (f2, f1) in enumerate(formants):
        plt.text(f2, f1, str(i + 1), ha='center', va='center', color='red', fontsize=12)
    
    plt.gca().invert_yaxis()  # Invert y-axis for F1
    plt.gca().invert_xaxis()  # Invert x-axis for F2
    plt.xlabel("F2 Frequency (Hz)")
    plt.ylabel("F1 Frequency (Hz)")
    plt.title("Formant Plot of Recorded Words")
    st.pyplot(plt)

# Streamlit UI
st.title("Formant Extraction for Recorded Words")

st.write("Record and upload 9 one-syllable words to analyze their formants.")

# File uploader for 9 recordings
uploaded_files = st.file_uploader("Upload 9 audio files (one per word)", type=["wav", "mp3"], accept_multiple_files=True)

if len(uploaded_files) == 9:
    formants = []
    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())
        word_formants = extract_formants(file.name)
        formants.extend(word_formants)
    
    if formants:
        st.success("Formants extracted successfully!")
        plot_formants(formants)
else:
    st.warning("Please upload exactly 9 audio files.")
