import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#Seeting Warnings False
st.set_option('deprecation.showPyplotGlobalUse', False)

# Define a function to plot and display the data
def plot_and_display(df):
    # Create a sidebar for user input
    selected_location = st.sidebar.selectbox('Select Location', df['location'].unique())

    # Filter data based on user selection
    filtered_df = df[df['location'] == selected_location]

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_df['year'], filtered_df['Capacity in kW'], color='skyblue')
    plt.title(f"Capacity vs Year for {selected_location}")
    plt.xlabel("Year")
    plt.ylabel("Capacity (kW)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(filtered_df['year'])  # Ensure all years are shown on x-axis

    # Display the plot
    st.pyplot()

# Load the data based on user selection
selected_dataset = st.sidebar.selectbox('Select Dataset', ['No VRFB', 'With VRFB - Battery', 'With VRFB - VRFB'])
if selected_dataset == 'No VRFB':
    file_path = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\PI_No_VRFB_Capacity.csv"
elif selected_dataset == 'With VRFB - Battery':
    file_path = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Capacity_Battery.csv"
else:
    file_path = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Capacity_VRFB.csv"
df = pd.read_csv(file_path)

# Run the Streamlit app
st.title('Installed Capacity Dashboard')
plot_and_display(df)

