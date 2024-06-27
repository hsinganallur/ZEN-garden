import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Extract relevant data for each technology
storage_technologies = ['battery', 'hydrogen_storage', 'pumped_hydro', 'vanadium_redox_flow_battery',
                        'up_redox_flow_battery_1', 'up_redox_flow_battery_2',
                        'up_redox_flow_battery_3', 'up_redox_flow_battery_4', 'up_redox_flow_battery_5']

conversion_technologies = ["DAC", "biomass_boiler", "biomass_plant", "biomass_plant_CCS", "carbon_storage",
                           "hard_coal_plant_CCS", "heat_pump", "lignite_coal_plant", "lng_terminal",
                           "natural_gas_boiler", "natural_gas_turbine", "natural_gas_turbine_CCS", "nuclear",
                           "photovoltaics", "reservoir_hydro", "run-of-river_hydro", "waste_plant", "wind_offshore",
                           "wind_onshore"]

# Define colors for each technology
colors = {
    'battery': '#00BFFF',
    'hydrogen_storage': '#FF6347',
    'pumped_hydro': '#00008B',
    'carbon_pipeline': '#00009B',
    'vanadium_redox_flow_battery': '#d62728',
    'up_redox_flow_battery_1': '#9467bd',
    'up_redox_flow_battery_2': '#8c564b',
    'up_redox_flow_battery_3': '#e377c2',
    'up_redox_flow_battery_4': '#7f7f7f',
    'up_redox_flow_battery_5': '#bcbd22',
    'DAC': '#1f77b4',
    'biomass_boiler': '#ff7f0e',
    'biomass_plant': '#2ca02c',
    'biomass_plant_CCS': '#d62728',
    'carbon_storage': '#9467bd',
    'hard_coal_plant_CCS': '#8c564b',
    'heat_pump': '#e377c2',
    'lignite_coal_plant': '#7f7f7f',
    'lng_terminal': '#bcbd22',
    'natural_gas_boiler': '#17becf',
    'natural_gas_turbine': '#9edae5',
    'natural_gas_turbine_CCS': '#dbdb8d',
    'nuclear': '#393b79',
    'photovoltaics': '#5254a3',
    'reservoir_hydro': '#6b6ecf',
    'run-of-river_hydro': '#9c9ede',
    'waste_plant': '#637939',
    'wind_offshore': '#8ca252',
    'wind_onshore': '#b5cf6b'
}

out_folder1 = "C:\\GitHub\\ZEN-garden\\data\\outputs\\Vanilla_PI_FB_No_Power_Lines_Green_3"
r = Results(out_folder1)
data_1 = r.get_total("capacity")
data_1 = data_1.reset_index()
data_1_power = data_1[data_1['capacity_type'] == 'power']
data_1_power = (data_1_power.groupby('technology').sum())#.groupby('location').sum()
data_1_power.drop(columns=['capacity_type','location'],inplace=True)
data_1_energy = data_1[data_1['capacity_type'] == 'energy']
data_1_energy = (data_1_energy.groupby('technology').sum())#.groupby('location').sum()
data_1_energy.drop(columns=['capacity_type','location'],inplace=True)
data_cycles = ((r.get_total("flow_storage_discharge").groupby('technology').sum() / r.get_total("efficiency_discharge").groupby('technology').mean()) + (r.get_total("flow_storage_charge").groupby('technology').sum() / r.get_total("efficiency_charge").groupby('technology').mean()) ) /2/ r.get_total('capacity').loc[:,'energy',:].groupby('technology').sum()
flow_storage_data = r.get_full_ts("flow_storage_discharge").groupby('technology').sum()
flow_conversion_output_data = r.get_full_ts("flow_conversion_output").groupby('technology').sum()

# Filter data greater than 1
data_1_energy_filtered = data_1_energy[data_1_energy > 1].dropna()
data_1_power_filtered = data_1_power[data_1_power > 1].dropna()
# Divide by 1000 - TWh, TW
data_1_energy_filtered /= 1000
data_1_power_filtered /= 1000

def plot_stacked_energy(data):
    num_years = len(data.columns) - 1  # Number of years is determined by the number of columns minus 1 (excluding 'technology')
    num_technologies = len(data)  # Number of technologies

    # Sort technologies based on their total energy values in the last year (or any year of choice)
    data_sorted = data.sort_values(by=data.columns[-1], axis=0, ascending=True)

    # Plot stacked bars
    fig, ax = plt.subplots(figsize=(12, 8))

    # Prepare data for plotting
    years = np.arange(num_years)  # Use integers for the x-axis
    technologies = data_sorted.index  # Technologies sorted by total energy values

    # Initialize bottom array for stacked bar plot
    bottom = np.zeros(num_years)

    # Plot each technology's data as a stacked bar
    for i, tech in enumerate(technologies):
        values = data_sorted.loc[tech].values[1:]  # Exclude the first column which is the technology name
        ax.bar(years, values, label=tech, bottom=bottom, color=colors[tech])
        bottom += values  # Update the bottom for the next technology

    # Customize the plot
    ax.set_title('Energy by Technology over Years')
    ax.set_xlabel('Years')
    ax.set_ylabel('Energy (TWh)')
    ax.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(years)  # Use integer labels on x-axis
    plt.tight_layout()
    # Show plot
    plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\plot_tests\\1_Energy")

def plot_stacked_power(data):
    num_years = len(data.columns) - 1  # Number of years is determined by the number of columns minus 1 (excluding 'technology')
    num_technologies = len(data)  # Number of technologies

    # Sort technologies based on their total energy values in the last year (or any year of choice)
    data_sorted = data.sort_values(by=data.columns[-1], axis=0, ascending=True)

    # Plot stacked bars
    fig, ax = plt.subplots(figsize=(12, 8))

    # Prepare data for plotting
    years = np.arange(num_years)  # Use integers for the x-axis
    technologies = data_sorted.index  # Technologies sorted by total energy values

    # Initialize bottom array for stacked bar plot
    bottom = np.zeros(num_years)

    # Plot each technology's data as a stacked bar
    for i, tech in enumerate(technologies):
        values = data_sorted.loc[tech].values[1:]  # Exclude the first column which is the technology name
        ax.bar(years, values, label=tech, bottom=bottom, color=colors[tech])
        bottom += values  # Update the bottom for the next technology

    # Customize the plot
    ax.set_title('Power by Technology over Years')
    ax.set_xlabel('Years')
    ax.set_ylabel('Power (TW)')
    ax.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(years)  # Use integer labels on x-axis
    plt.tight_layout()
    # Show plot
    plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\plot_tests\\1_Power")

# Plot stacked bar chart for energy data
plot_stacked_energy(data_1_energy_filtered)
plot_stacked_power(data_1_power_filtered)
