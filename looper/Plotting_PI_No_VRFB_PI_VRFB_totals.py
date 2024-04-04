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
    plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_energy.png", bbox_inches='tight')  # Save plot with tight bounding box

