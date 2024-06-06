import matplotlib.pyplot as plt
import numpy as np

# Time values
time = np.linspace(0, 24, 1000)

# Simulating energy demand and supply curves
demand = 50 + 20 * np.sin(2 * np.pi * time / 24)  # Simulated demand curve
supply = 40 + 10 * np.sin(2 * np.pi * (time / 24 + 0.5))  # Simulated supply curve shifted

# Plotting
plt.figure(figsize=(10, 6))

# Plot demand and supply
plt.plot(time, demand, label='Demand', color='brown', linewidth=2)
plt.plot(time, supply, label='Supply', color='black', linewidth=2)

# Fill areas of deficit and excess
plt.fill_between(time, supply, demand, where=(demand > supply), facecolor='pink', alpha=0.5, interpolate=True, label='Deficit')
plt.fill_between(time, supply, demand, where=(demand < supply), facecolor='red', alpha=0.5, interpolate=True, label='Excess')

# Adjusting x-axis limits to touch the left and right edges
plt.xlim(time.min(), time.max())

# Remove numerical values from both X and Y axes
plt.xticks([])
plt.yticks([])

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy Demand and Supply Mismatch')
plt.legend()

# SaVE Plot
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\power_supply_demand.png')

"""#Demand Supply Mismatch
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
"""
"""#Plotting_PI_No_VRFB
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

"""#Plotting_PI_No_VRFB_PI_VRFB_totals_V2
import os
import pandas as pd
import matplotlib.pyplot as plt

import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_stacked_bar_plots(data, num_years, file_name, save_path, ylabel, title, unit, scenario_info, y_axis_limit=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = None
    for tech in data.columns:
        if bottom is None:
            ax.bar(data.index, data[tech], label=f"{tech} ({data[tech].sum():.0f} {unit})", alpha=0.7)
            bottom = data[tech]
        else:
            ax.bar(data.index, data[tech], bottom=bottom, label=f"{tech} ({data[tech].sum():.0f} {unit})", alpha=0.7)
            bottom += data[tech]

    ax.set_xlabel('Year')
    ax.set_ylabel(ylabel)
    ax.set_title(f"{title} - {scenario_info}")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xticks(range(1, num_years + 1))
    ax.tick_params(axis='x', rotation=0)

    if y_axis_limit is not None:
        ax.set_ylim(y_axis_limit)

    plt.tight_layout()
    plt.savefig(f"{save_path}/{file_name}.png", dpi=300, bbox_inches='tight')
    plt.close()

def generate_power_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000

        power_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_power_data = pd.DataFrame(index=range(1, num_years + 1), columns=power_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in power_data.items():
                stacked_power_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_power_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000

        power_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_power_data = pd.DataFrame(index=range(1, num_years + 1), columns=power_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in power_data.items():
                stacked_power_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_power_data, num_years, f"stacked_power_{file_name}", save_path,
                                   'Installed Power(GW)', 'Installed Power Over Technologies', 'GW', scenario_info, y_axis_limit)

def generate_energy_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000000

        energy_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=energy_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in energy_data.items():
                stacked_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_energy_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000000

        energy_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=energy_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in energy_data.items():
                stacked_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_energy_data, num_years, f"stacked_energy_{file_name}", save_path,
                                   'Installed Energy(GWh)', 'Installed Energy Over Technologies', 'GWh', scenario_info, y_axis_limit)

def generate_specific_tech_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3

        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_specific_tech_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_tech_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_specific_tech_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3

        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_specific_tech_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_tech_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_specific_tech_data, num_years, f"stacked_specific_tech_{file_name}", save_path,
                                   'Installed Power(GW)', 'Installed Power for Specific Technologies', 'GW', scenario_info, y_axis_limit)


def generate_specific_energy_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3


        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_specific_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_specific_energy_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3

        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_specific_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_specific_energy_data, num_years, f"stacked_specific_energy_{file_name}", save_path,
                                   'Installed Energy(GWh)', 'Installed Energy for Specific Technologies', 'GWh', scenario_info, y_axis_limit)


file_paths = [
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_No_VRFB_Imports_0_capacity_total.csv",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_No_VRFB_Imports_capacity_total.csv",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_VRFB_Imports_0_capacity_total.csv",
    #"C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_VRFB_Imports_capacity_total.csv"
    ]

save_paths = [
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14",
    #"C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14"
    ]

scenarios = [
    "PI folder without VRFBs and Imports",
    "PI folder without VRFBs and Imports permitted",
    "PI folder with VRFBs No Imports",
    #"PI folder with VRFBs and Imports permitted"
    ]

generate_power_plots(file_paths, save_paths, scenarios)
generate_energy_plots(file_paths, save_paths, scenarios)
generate_specific_tech_plots(file_paths, save_paths, scenarios)
generate_specific_energy_plots(file_paths, save_paths, scenarios)

#Plotting_Configurations_25_04_2024

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies=None, log_scale=False):
    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        data = pd.read_csv(file_path)
        num_ts = len(data.columns) - 2
        data.iloc[:, 2:] /= 1000

        # Adjust column indices
        new_indices = np.linspace(0, 12, num=num_ts)
        data.columns = data.columns[:2].tolist() + new_indices.tolist()

        if selected_technologies:
            data = data[data['technology'].isin(selected_technologies)]

        if data.empty:
            print(f"No data available for the specified technologies in {file_path}. Skipping...")
            continue

        storage_level_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            storage_level_data[tech] = tech_data.iloc[:, 2:].sum(axis=0)  # Sum capacity across countries

        plt.figure(figsize=(10, 6))
        for tech, tech_data in storage_level_data.items():
            plt.plot(new_indices, tech_data, label=tech)

        plt.xlabel('Time Steps (Months)')
        plt.ylabel('Storage Level (TWh)')
        plt.title('Storage Level Over Time for Different Technologies' + f" ({scenario_info})")
        plt.grid(True)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        if log_scale:
            plt.yscale('log')  # Set Y-axis to log scale
            plt.savefig(os.path.join(save_path, f"stacked_storage_level_{scenario_info}_log.png"), bbox_inches='tight')
        else:
            plt.savefig(os.path.join(save_path, f"stacked_storage_level_{scenario_info}_linear.png"), bbox_inches='tight')

file_paths = [
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_VRFB_Imports_storage_level_fullts.csv",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_VRFB_Imports_storage_level_fullts.csv",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_VRFB_Imports_storage_level_fullts.csv",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_VRFB_Imports_storage_level_fullts.csv"
]

save_paths = [
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots"
]

scenarios = [
    "PI folder without VRFBs and No Imports",
    "PI folder without VRFBs and Imports",
    "PI folder with VRFBs and No Imports",
    "PI folder with VRFBs and Imports"
]

# List of selected technologies (None if you want to plot all)
selected_technologies = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]

# Generate plot with linear scale
generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies, log_scale=False)

# Generate plot with log scale
generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies, log_scale=True)"""
