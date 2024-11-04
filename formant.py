import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tab names
tab1, tab2 = st.tabs(["Upload CSV", "F1 vs F2 Plot"])

# Tab 1 - Upload CSV file
with tab1:
    st.header("Upload CSV File")
    st.write("Please upload a CSV file with three columns: `F1`, `F2`, and `word`.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Load and display the data if a file is uploaded
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Ensure the CSV contains 'F1', 'F2', and 'word' columns
        if {"F1", "F2", "word"}.issubset(data.columns):
            st.success("File successfully uploaded.")
            st.dataframe(data)  # Display the data for verification
            st.session_state['data'] = data  # Store the data in session state
        else:
            st.error("The uploaded CSV file must contain columns `F1`, `F2`, and `word`.")

# Tab 2 - Plot F1 vs F2
with tab2:
    st.header("Dot Plot of F1 vs F2 with Word Labels")

    # Check if data is available in session state
    if 'data' in st.session_state:
        data = st.session_state['data']

        # Create the dot plot
        plt.figure(figsize=(10, 8))
        plt.scatter(data["F2"], data["F1"], color='blue', s=100)  # Increased size of dots for better visibility

        # Reverse axes as specified
        plt.gca().invert_xaxis()  # F2 increases from right to left
        plt.gca().invert_yaxis()  # F1 increases from top to bottom

        # Add labels and title
        plt.xlabel("F2")
        plt.ylabel("F1")
        plt.ylim(900,0)
        plt.title("Dot Plot of F1 vs F2 with Word Labels")

        # Display the word labels with offset and increased font size
        for i, row in data.iterrows():
            plt.text(row["F2"] + 30, row["F1"] + 30, row["word"], fontsize=12, ha='left', color='black')  # Offset and font size adjustment

        # Display the plot in Streamlit
        st.pyplot(plt)
    else:
        st.write("Please upload a CSV file in the 'Upload CSV' tab.")
