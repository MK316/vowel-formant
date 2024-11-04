import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame with the formant values from the image
data = {
    "Vowel": ["i", "ɪ", "ɛ", "æ", "ɑ", "ɔ", "ʊ", "u", "ʌ", "ɝ"],
    "Men_F1": [270, 400, 530, 660, 730, 570, 440, 300, 640, 490],
    "Men_F2": [2300, 2000, 1850, 1700, 1100, 850, 1000, 850, 1200, 1350],
    "Women_F1": [300, 430, 600, 860, 850, 590, 470, 370, 760, 500],
    "Women_F2": [2800, 2500, 2350, 2050, 1200, 850, 1150, 950, 1400, 1650],
    "Children_F1": [370, 530, 700, 1000, 1030, 680, 560, 430, 850, 560],
    "Children_F2": [3200, 2750, 2600, 2300, 1350, 950, 1400, 1150, 1600, 1650]
}

df = pd.DataFrame(data)

# Initialize session state to keep track of displayed genders
if 'show_men' not in st.session_state:
    st.session_state['show_men'] = False
if 'show_women' not in st.session_state:
    st.session_state['show_women'] = False
if 'show_children' not in st.session_state:
    st.session_state['show_children'] = False

# Function to plot vowel chart with overlays for selected genders
def plot_vowel_chart(df):
    plt.figure(figsize=(8, 6))

    # Plot for Men if selected
    if st.session_state['show_men']:
        plt.scatter(df["Men_F2"], df["Men_F1"], color='blue', s=100, label='Men')
        for i, vowel in enumerate(df["Vowel"]):
            plt.text(df["Men_F2"][i] + 30, df["Men_F1"][i] + 30, vowel, color='blue', fontsize=10, ha='center')

    # Plot for Women if selected
    if st.session_state['show_women']:
        plt.scatter(df["Women_F2"], df["Women_F1"], color='green', s=100, label='Women')
        for i, vowel in enumerate(df["Vowel"]):
            plt.text(df["Women_F2"][i] + 30, df["Women_F1"][i] + 30, vowel, color='green', fontsize=10, ha='center')

    # Plot for Children if selected
    if st.session_state['show_children']:
        plt.scatter(df["Children_F2"], df["Children_F1"], color='red', s=100, label='Children')
        for i, vowel in enumerate(df["Vowel"]):
            plt.text(df["Children_F2"][i] + 30, df["Children_F1"][i] + 30, vowel, color='red', fontsize=10, ha='center')

    # Set consistent axes limits for all plots
    plt.xlim(800, 3300)  # F2 range (right-to-left for vowel plots)
    plt.ylim(200, 1100)  # F1 range (top-to-bottom for vowel plots)

    # Reverse axes as per common vowel chart convention
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.xlabel("F2")
    plt.ylabel("F1")
    plt.title("Overlay Vowel Chart")
    plt.legend()
    st.pyplot(plt)

# Streamlit app layout
st.title("Overlay Vowel Chart Comparison")

st.write("Click the buttons below to add each group's vowel data to the plot.")

# Buttons to add each group's vowel data to the plot
if st.button("Add Men's Data"):
    st.session_state['show_men'] = True

if st.button("Add Women's Data"):
    st.session_state['show_women'] = True

if st.button("Add Children's Data"):
    st.session_state['show_children'] = True

# Display the vowel chart with the selected overlays
plot_vowel_chart(df)
