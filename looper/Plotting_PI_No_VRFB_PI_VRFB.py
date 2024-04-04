import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_and_save_power(df, folder_path):
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
        plt.ylabel("Installed Power (kW)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

        # Save the plot
        plot_filename = os.path.join(folder_path, f"{location}_capacity_bar_plot.png")
        plt.savefig(plot_filename)
        plt.close()

        print(f"Bar plot saved for {location} at: {plot_filename}")

def plot_and_save_energy(df, folder_path):
    # Iterate over unique locations
    locations = df['location'].unique()
    for location in locations:
        # Filter data for the current location
        location_df = df[df['location'] == location]

        # Create a bar plot
        plt.figure(figsize=(10, 6))
        plt.bar(location_df['year'], location_df['Capacity in kWh'], color='skyblue')
        plt.title(f"Capacity vs Year for {location}")
        plt.xlabel("Year")
        plt.ylabel("Installed Energy (kWh)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

        # Save the plot
        plot_filename = os.path.join(folder_path, f"{location}_capacity_bar_plot.png")
        plt.savefig(plot_filename)
        plt.close()

        print(f"Bar plot saved for {location} at: {plot_filename}")

# Code for the first data set (No VRFB)
folder_path_no_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Battery_Energy"
os.makedirs(folder_path_no_vrfb_beu, exist_ok=True)
file_path_no_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\PI_No_VRFB_Energy.csv"
df_no_vrfb_beu = pd.read_csv(file_path_no_vrfb_beu)
plot_and_save_energy(df_no_vrfb_beu,folder_path_no_vrfb_beu)

# Code for the second data set (With VRFB)
folder_path_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Battery_Energy"
os.makedirs(folder_path_vrfb_beu, exist_ok=True)
file_path_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Energy_Battery.csv"
df_vrfb_beu = pd.read_csv(file_path_vrfb_beu)
plot_and_save_energy(df_vrfb_beu, folder_path_vrfb_beu)

# Code for the third data set (With VRFB)
folder_path_vrfb_vrfbeu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\VRFB_Energy"
os.makedirs(folder_path_vrfb_vrfbeu, exist_ok=True)
file_path_vrfb_vrfbeu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Energy_VRFB.csv"
df_vrfb_vrfbeu = pd.read_csv(file_path_vrfb_vrfbeu)
plot_and_save_energy(df_vrfb_vrfbeu, folder_path_vrfb_vrfbeu)

# Code for the fourth data set (No VRFB)
folder_path_no_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Battery_Energy"
os.makedirs(folder_path_no_vrfb_ben, exist_ok=True)
file_path_no_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\PI_No_VRFB_Energy.csv"
df_no_vrfb_ben = pd.read_csv(file_path_no_vrfb_ben)
plot_and_save_energy(df_no_vrfb_ben, folder_path_no_vrfb_ben)

# Code for the fifth data set (With VRFB)
folder_path_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Battery_Energy"
os.makedirs(folder_path_vrfb_ben, exist_ok=True)
file_path_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Energy_Battery.csv"
df_vrfb_ben = pd.read_csv(file_path_vrfb_ben)
plot_and_save_energy(df_vrfb_ben, folder_path_vrfb_ben)

# Code for the sixth data set (With VRFB)
folder_path_vrfb_vrfben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\VRFB_Energy"
os.makedirs(folder_path_vrfb_vrfben, exist_ok=True)
file_path_vrfb_vrfben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Energy_VRFB.csv"
df_vrfb_vrfben = pd.read_csv(file_path_vrfb_vrfben)
plot_and_save_energy(df_vrfb_vrfben, folder_path_vrfb_vrfben)

# Code for the seventh data set (No VRFB)
folder_path_no_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Battery_Power"
os.makedirs(folder_path_no_vrfb_bpu, exist_ok=True)
file_path_no_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\PI_No_VRFB_Power.csv"
df_no_vrfb_bpu = pd.read_csv(file_path_no_vrfb_bpu)
plot_and_save_power(df_no_vrfb_bpu, folder_path_no_vrfb_bpu)

# Code for the eighth data set (With VRFB)
folder_path_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Battery_Power"
os.makedirs(folder_path_vrfb_bpu, exist_ok=True)
file_path_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Power_Battery.csv"
df_vrfb_bpu = pd.read_csv(file_path_vrfb_bpu)
plot_and_save_power(df_vrfb_bpu, folder_path_vrfb_bpu)

# Code for the ninth data set (With VRFB)
folder_path_vrfb_vrfbpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\VRFB_Power"
os.makedirs(folder_path_vrfb_vrfbpu, exist_ok=True)
file_path_vrfb_vrfbpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Power_VRFB.csv"
df_vrfb_vrfbpu = pd.read_csv(file_path_vrfb_vrfbpu)
plot_and_save_power(df_vrfb_vrfbpu, folder_path_vrfb_vrfbpu)

# Code for the tenth data set (No VRFB)
folder_path_no_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Battery_Power"
os.makedirs(folder_path_no_vrfb_bpn, exist_ok=True)
file_path_no_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\PI_No_VRFB_Power.csv"
df_no_vrfb_bpn = pd.read_csv(file_path_no_vrfb_bpn)
plot_and_save_power(df_no_vrfb_bpn, folder_path_no_vrfb_bpn)

# Code for the eleventh data set (With VRFB)
folder_path_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Battery_Power"
os.makedirs(folder_path_vrfb_bpn, exist_ok=True)
file_path_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Power_Battery.csv"
df_vrfb_bpn= pd.read_csv(file_path_vrfb_bpn)
plot_and_save_power(df_vrfb_bpn, folder_path_vrfb_bpn)

# Code for the twelfth data set (With VRFB)
folder_path_vrfb_vrfbpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\VRFB_Power"
os.makedirs(folder_path_vrfb_vrfbpn, exist_ok=True)
file_path_vrfb_vrfbpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Power_VRFB.csv"
df_vrfb_vrfbpn = pd.read_csv(file_path_vrfb_vrfbpn)
plot_and_save_power(df_vrfb_vrfbpn, folder_path_vrfb_vrfbpn)