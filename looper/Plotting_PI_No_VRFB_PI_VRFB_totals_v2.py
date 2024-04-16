import pandas as pd
import matplotlib.pyplot as plt

def generate_plots(file_path, save_path):
    # Load the data
    data = pd.read_csv(file_path)

    # Task 1: Count the number of years
    num_years = len(data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"
    data.iloc[:, 3:] *= 1000000

    # Task 2: Extract data for power and energy for each technology
    power_data = {}
    energy_data = {}
    for tech in data['technology'].unique():
        tech_data = data[data['technology'] == tech]
        power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
        energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

    # Task 3: Sum up installed power for each country and each year for all technologies
    stacked_power_data = pd.DataFrame(index=data['location'].unique(), columns=range(1, num_years + 1), dtype=float)
    for country in data['location'].unique():
        country_data = data[data['location'] == country]
        for year in range(1, num_years + 1):
            stacked_power_data.loc[country, year] = country_data.iloc[:, 3:].sum(axis=0).loc[year]

    # Task 4: Generate stacked bar plots for installed power for each year
    for year in range(1, num_years + 1):
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        bottom = None
        for tech, power_df in power_data.items():
            country_data = power_df[power_df['location'].isin(stacked_power_data.index)]
            country_power = country_data.iloc[:, 3:].sum(axis=0).loc[year]
            if bottom is None:
                bottom = country_power
            else:
                ax.bar(stacked_power_data.index, country_power, bottom=bottom, label=tech)
                bottom += country_power

        ax.set_xlabel('Country')
        ax.set_ylabel('Installed Power (kW)')
        ax.set_title(f'Installed Power Over Countries - Year {year}')
        ax.legend(loc='upper right')  # Place legend
        plt.xticks(rotation=45)  # Rotate country labels for better visibility
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"{save_path}/stacked_power_year_{year}.png")  # Save plot

    # Task 5: Sum up installed energy for each country and each year for all technologies
    stacked_energy_data = pd.DataFrame(index=data['location'].unique(), columns=range(1, num_years + 1), dtype=float)
    for country in data['location'].unique():
        country_data = data[data['location'] == country]
        for year in range(1, num_years + 1):
            stacked_energy_data.loc[country, year] = country_data.iloc[:, 3:].sum(axis=0).loc[year]

    # Task 6: Generate stacked bar plots for installed energy for each year
    for year in range(1, num_years + 1):
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        bottom = None
        for tech, energy_df in energy_data.items():
            country_data = energy_df[energy_df['location'].isin(stacked_energy_data.index)]
            country_energy = country_data.iloc[:, 3:].sum(axis=0).loc[year]
            if bottom is None:
                bottom = country_energy
            else:
                ax.bar(stacked_energy_data.index, country_energy, bottom=bottom, label=tech)
                bottom += country_energy

        ax.set_xlabel('Country')
        ax.set_ylabel('Installed Energy (kWh)')
        ax.set_title(f'Installed Energy Over Countries - Year {year}')
        ax.legend(loc='upper right')  # Place legend
        plt.xticks(rotation=45)  # Rotate country labels for better visibility
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"{save_path}/stacked_energy_year_{year}.png")  # Save plot

# List of file paths and corresponding save paths
file_save_paths = [("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv",
                    "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\All_Technologies_Total"),
                   ("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv",
                    "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\All_Technologies_Total"),
                   ("C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Unsorted\\PI_No_VRFB_Capacity_Total_Unsorted.csv",
                   "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\All_Technologies_Total"),
                   ("C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Unsorted\\PI_No_VRFB_Capacity_Total_Unsorted.csv",
                   "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\All_Technologies_Total")]

# Generate plots for each file
for file_path, save_path in file_save_paths:
    generate_plots(file_path, save_path)

