import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_and_save(df, folder_path):
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
        plot_filename = os.path.join(folder_path, f"{location}_capacity_bar_plot.png")
        plt.savefig(plot_filename)
        plt.close()

        print(f"Bar plot saved for {location} at: {plot_filename}")

# Code for the first data set (No VRFB)
folder_path_no_vrfb = "C:/GitHub/ZEN-garden/looper/PI_No_VRFB"
os.makedirs(folder_path_no_vrfb, exist_ok=True)
file_path_no_vrfb = "C:/GitHub/ZEN-garden/looper/PI_No_VRFB_Capacity.csv"
df_no_vrfb = pd.read_csv(file_path_no_vrfb)
plot_and_save(df_no_vrfb, folder_path_no_vrfb)

# Code for the second data set (With VRFB)
folder_path_vrfb_battery = "C:/GitHub/ZEN-garden/looper/PI_VRFB/Battery"
os.makedirs(folder_path_vrfb_battery, exist_ok=True)
file_path_vrfb_battery = "C:/GitHub/ZEN-garden/looper/PI_VRFB_Capacity_Battery.csv"
df_vrfb_battery = pd.read_csv(file_path_vrfb_battery)
plot_and_save(df_vrfb_battery, folder_path_vrfb_battery)

# Code for the third data set (With VRFB)
folder_path_vrfb_vrfb = "C:/GitHub/ZEN-garden/looper/PI_VRFB/VRFB"
os.makedirs(folder_path_vrfb_vrfb, exist_ok=True)
file_path_vrfb_vrfb = "C:/GitHub/ZEN-garden/looper/PI_VRFB_Capacity_VRFB.csv"
df_vrfb_vrfb = pd.read_csv(file_path_vrfb_vrfb)
plot_and_save(df_vrfb_vrfb, folder_path_vrfb_vrfb)
