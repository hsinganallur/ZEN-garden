import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the folder if it doesn't exist
folder_path_1 = "C:/GitHub/ZEN-garden/looper/PI_VRFB/Battery"
os.makedirs(folder_path_1, exist_ok=True)

# Load the data
file_path_1 = "C:/GitHub/ZEN-garden/looper/PI_VRFB_Capacity_Battery.csv"
df = pd.read_csv(file_path_1)

# Iterate over unique locations
locations = df['location'].unique()
for location in locations:
    # Filter data for the current location
    location_df = df[df['location'] == location]

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(location_df['year'], location_df['Capacity in kW'], color='skyblue')
    plt.title(f"Capacity vs Year for {location}")
    plt.xlabel("Year")
    plt.ylabel("Capacity (kW)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

    # Save the plot
    plot_filename = os.path.join(folder_path_1, f"{location}_capacity_bar_plot.png")
    plt.savefig(plot_filename)
    plt.close()

    print(f"Bar plot saved for {location} at: {plot_filename}")

# Create the folder if it doesn't exist
folder_path_2 = "C:/GitHub/ZEN-garden/looper/PI_VRFB/VRFB"
os.makedirs(folder_path_2, exist_ok=True)

# Load the data
file_path_2 = "C:/GitHub/ZEN-garden/looper/PI_VRFB_Capacity_VRFB.csv"
df = pd.read_csv(file_path_2)

# Iterate over unique locations
locations = df['location'].unique()
for location in locations:
    # Filter data for the current location
    location_df = df[df['location'] == location]

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(location_df['year'], location_df['Capacity in kW'], color='skyblue')
    plt.title(f"Capacity vs Year for {location}")
    plt.xlabel("Year")
    plt.ylabel("Capacity (kW)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

    # Save the plot
    plot_filename = os.path.join(folder_path_2, f"{location}_capacity_bar_plot.png")
    plt.savefig(plot_filename)
    plt.close()

    print(f"Bar plot saved for {location} at: {plot_filename}")