import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame with the formant values from the image
data = {
    "Vowel": ["i", "ɪ", "ɛ", "æ", "ɑ", "ɔ", "ʊ", "u", "ʌ", "ɝ"],
    "Men_F1": [270, 400, 530, 660, 730, 570, 440, 300, 640, 490],
    "Men_F2": [2300, 2000, 1850, 1700, 1100, 850, 1000, 850, 1200, 1350],
    "Men_F3": [3000, 2550, 2500, 2400, 2450, 2500, 2250, 2250, 2400, 1700],
    "Women_F1": [300, 430, 600, 860, 850, 590, 470, 370, 760, 500],
    "Women_F2": [2800, 2500, 2350, 2050, 1200, 850, 1150, 950, 1400, 1650],
    "Women_F3": [3300, 3100, 3000, 2850, 1200, 2700, 2650, 2450, 2600, 1950],
    "Children_F1": [370, 530, 700, 1000, 1030, 680, 560, 430, 850, 560],
    "Children_F2": [3200, 2750, 2600, 2300, 1350, 950, 1400, 1150, 1600, 1650],
    "Children_F3": [3700, 3600, 3550, 3300, 3200, 3050, 3250, 3250, 3350, 2150]
}

df = pd.DataFrame(data)

# Function to plot vowel chart for selected data with consistent axes
def plot_vowel_chart(df, gender):
    F1 = df[f"{gender}_F1"]
    F2 = df[f"{gender}_F2"]
    vowels = df["Vowel"]

    # Create plot
    plt.figure(figsize=(8, 6))
    plt.scatter(F2, F1, color='blue', s=100)
    for i, vowel in enumerate(vowels):
        plt.text(F2[i] + 30, F1[i] + 30, vowel, fontsize=12, ha='center')

    # Set consistent axes limits for all plots
    plt.xlim(800, 3300)  # F2 range (right-to-left for vowel plots)
    plt.ylim(200, 1100)  # F1 range (top-to-bottom for vowel plots)

    # Reverse axes as per common vowel chart convention
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.xlabel("F2")
    plt.ylabel("F1")
    plt.title(f"Vowel Chart for {gender}")
    st.pyplot(plt)

# Streamlit app layout
st.title("Interactive Vowel Chart")

st.write("Select a gender to view the corresponding vowel formant chart.")

# Buttons for each gender
if st.button("Men"):
    st.subheader("Vowel Chart for Men")
    plot_vowel_chart(df, "Men")

if st.button("Women"):
    st.subheader("Vowel Chart for Women")
    plot_vowel_chart(df, "Women")

if st.button("Children"):
    st.subheader("Vowel Chart for Children")
    plot_vowel_chart(df, "Children")
