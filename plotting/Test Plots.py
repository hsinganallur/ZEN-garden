#Demand Supply Mismatch
import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
np.random.seed(0)
time = np.arange(0, 10, 0.1)
demand = np.sin(time) + np.random.normal(scale=0.5, size=len(time))
supply = np.sin(time + 0.5) + np.random.normal(scale=0.5, size=len(time))

# Create the plot
plt.figure(figsize=(10, 6))

# Plot supply and demand with straight lines
plt.plot(time, supply, label='Supply', color='black', drawstyle='steps-post')
plt.plot(time, demand, label='Demand', color='gray', drawstyle='steps-post')

# Fill the deficit and excess areas
plt.fill_between(time, supply, demand, where=(supply < demand), step='post', color='lightcoral', alpha=0.5, label='Deficit')
plt.fill_between(time, supply, demand, where=(supply > demand), step='post', color='lightblue', alpha=0.5, label='Excess')

# Highlight the mismatch region
mismatch_start = 50  # Index for start of mismatch (adjust as needed)
mismatch_end = 80    # Index for end of mismatch (adjust as needed)
plt.axvspan(time[mismatch_start], time[mismatch_end], color='gray', alpha=0.3, label='Mismatch')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power Supply and Demand Over Time')
plt.legend(loc='upper right')

# Save the plot to a file
plt.savefig('power_supply_demand_straight_lines.png')

# Save the plot to a file
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\power_supply_demand.png')

#Plotting_PI_No_VRFB
import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the folder if it doesn't exist
folder_path = "C:/GitHub/ZEN-garden/looper/PI_No_VRFB"
os.makedirs(folder_path, exist_ok=True)

# Load the data
file_path = "C:/GitHub/ZEN-garden/looper/PI_No_VRFB_Capacity.csv"
df = pd.read_csv(file_path)

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

    #Plotting_PI_No_VRFB_PI_VRFB
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
    plot_and_save_energy(df_no_vrfb_beu, folder_path_no_vrfb_beu)

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
    df_vrfb_bpn = pd.read_csv(file_path_vrfb_bpn)
    plot_and_save_power(df_vrfb_bpn, folder_path_vrfb_bpn)

    # Code for the twelfth data set (With VRFB)
    folder_path_vrfb_vrfbpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\VRFB_Power"
    os.makedirs(folder_path_vrfb_vrfbpn, exist_ok=True)
    file_path_vrfb_vrfbpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Power_VRFB.csv"
    df_vrfb_vrfbpn = pd.read_csv(file_path_vrfb_vrfbpn)
    plot_and_save_power(df_vrfb_vrfbpn, folder_path_vrfb_vrfbpn)

    #Plotting_PI_No_VRFB_PI_VRFB_totals
    import pandas as pd
    import matplotlib.pyplot as plt


    def generate_plots(file_path, save_path):
        # Load the data
        data = pd.read_csv(file_path)

        # Task 1: Count the number of years
        num_years = len(
            data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"
        data.iloc[:, 3:] *= 1000000

        # Task 2: Extract data for power and energy for each technology
        power_data = {}
        energy_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
            energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        # Task 3: Generate plot of installed power for each country for each technology
        for tech, power_df in power_data.items():
            fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
            for country in power_df['location'].unique():
                country_data = power_df[power_df['location'] == country]
                ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

            ax.set_xlabel('Year')
            ax.set_ylabel('Installed Power (kW)')
            ax.set_title('Installed Power Over Years')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
            ax.set_ylim(bottom=0)  # Set the lower limit of y-axis to 0
            ax.set_ylim(top=None)  # Remove the upper limit of y-axis
            plt.tight_layout()  # Adjust layout
            plt.savefig(f"{save_path}/{tech}_installed_power.png",
                        bbox_inches='tight')  # Save plot with tight bounding box

        # Task 4: Generate plot of installed energy for each country for each technology
        for tech, energy_df in energy_data.items():
            fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
            for country in energy_df['location'].unique():
                country_data = energy_df[energy_df['location'] == country]
                ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

            ax.set_xlabel('Year')
            ax.set_ylabel('Installed Energy (kWh)')
            ax.set_title('Installed Energy Over Years')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
            ax.set_ylim(bottom=0)  # Set the lower limit of y-axis to 0
            ax.set_ylim(top=None)  # Remove the upper limit of y-axis
            plt.tight_layout()  # Adjust layout
            plt.savefig(f"{save_path}/{tech}_installed_energy.png",
                        bbox_inches='tight')  # Save plot with tight bounding box


    # List of file paths and corresponding save paths
    file_save_paths = [
        ("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv",
         "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\All_Technologies_Total"),
        ("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv",
         "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\All_Technologies_Total"),
        ("C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Unsorted\\PI_No_VRFB_Capacity_Total_Unsorted.csv",
         "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\All_Technologies_Total"),
        (
        "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Unsorted\\PI_No_VRFB_Capacity_Total_Unsorted.csv",
        "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\All_Technologies_Total")]

    # Generate plots for each file
    for file_path, save_path in file_save_paths:
        generate_plots(file_path, save_path)

    """# Load the data
    data = pd.read_csv("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv")  # Replace "your_data.csv" with the path to your data file

    # Task 1: Count the number of years
    num_years = len(data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"

    # Task 2: Extract data for power and energy for each technology
    power_data = {}
    energy_data = {}
    for tech in data['technology'].unique():
        tech_data = data[data['technology'] == tech]
        power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
        energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

    # Task 3: Generate plot of installed power  for each country for each technology
    for tech, power_df in power_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in power_df['location'].unique():
            country_data = power_df[power_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Power')
        ax.set_title('Installed Power Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_power.png", bbox_inches='tight')  # Save plot with tight bounding box

    # Task 4: Generate plot of installed energy for each country for each technology
    for tech, energy_df in energy_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in energy_df['location'].unique():
            country_data = energy_df[energy_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Energy')
        ax.set_title('Installed Energy Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_energy.png", bbox_inches='tight')  # Save plot with tight bounding box

    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data
    data = pd.read_csv("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv")  # Replace "your_data.csv" with the path to your data file

    # Task 1: Count the number of years
    num_years = len(data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"

    # Task 2: Extract data for power and energy for each technology
    power_data = {}
    energy_data = {}
    for tech in data['technology'].unique():
        tech_data = data[data['technology'] == tech]
        power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
        energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

    # Task 3: Generate plot of installed power  for each country for each technology
    for tech, power_df in power_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in power_df['location'].unique():
            country_data = power_df[power_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Power')
        ax.set_title('Installed Power Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_power.png", bbox_inches='tight')  # Save plot with tight bounding box

    # Task 4: Generate plot of installed energy for each country for each technology
    for tech, energy_df in energy_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in energy_df['location'].unique():
            country_data = energy_df[energy_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Energy')
        ax.set_title('Installed Energy Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_energy.png", bbox_inches='tight')  # Save plot with tight bounding box"""

    