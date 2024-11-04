import streamlit as st
import parselmouth
from parselmouth.praat import call
import matplotlib.pyplot as plt
import numpy as np

st.title("Formant Analysis App")
st.write("Upload an audio file to analyze the first two formants (F1 and F2).")

# Step 1: Function to Extract Formants
def extract_formants(audio_path):
    sound = parselmouth.Sound(audio_path)
    formant = call(sound, "To Formant (burg)", 0.0, 5.0, 5500, 0.025, 50)
    
    # Extract the first two formants at the midpoint of the sound
    f1 = call(formant, "Get value at time", 1, 0.5, "Hertz", "Linear")
    f2 = call(formant, "Get value at time", 2, 0.5, "Hertz", "Linear")
    
    return f1, f2

# Step 2: Formant Plotting Function
def plot_formants(formants):
    plt.figure(figsize=(6, 6))
    plt.xlim(200, 2000)  # Typical F1 range
    plt.ylim(500, 3000)  # Typical F2 range
    plt.xlabel("F1 (Hz)")
    plt.ylabel("F2 (Hz)")
    plt.gca().invert_yaxis()  # Invert y-axis for phonetic visualization

    # Plot each formant with numbering 1-9
    for idx, (f1, f2) in enumerate(formants, start=1):
        plt.plot(f1, f2, 'bo')
        plt.text(f1, f2, str(idx), fontsize=12, ha='center', color="red")
    
    st.pyplot(plt)

# Step 3: Upload and Process Audio File
uploaded_files = st.file_uploader("Upload your audio files (9 words)", accept_multiple_files=True, type=["wav", "mp3"])

if uploaded_files and len(uploaded_files) == 9:
    st.success("9 audio files uploaded successfully! Processing...")
    
    # Extract and store formants for each file
    formants = []
    for file in uploaded_files:
        f1, f2 = extract_formants(file)
        formants.append((f1, f2))
    
    # Step 4: Plot Formants
    plot_formants(formants)
else:
    st.warning("Please upload exactly 9 audio files.")
