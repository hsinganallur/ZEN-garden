import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define the regions and their corresponding country codes
regions = {
    'Western Europe': ['AT', 'BE', 'FR', 'DE', 'LU', 'NL', 'CH', 'UK'],
    'Northern Europe': ['DK', 'EE', 'FI', 'IE', 'LV', 'LT', 'NO', 'SE'],
    'Southern Europe': ['HR', 'EL', 'IT', 'PT', 'SI', 'ES'],
    'Eastern Europe': ['BG', 'CZ', 'HU', 'PL', 'RO', 'SK']
}

out_folder1 = "C:\\GitHub\\ZEN-garden\\data\\outputs\\Vanilla_PI_FB_No_Power_Lines_Green_3"
r1 = Results(out_folder1)
data_1 = r1.get_total("capacity")
data_1 = data_1.reset_index()

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

# Function to plot storage levels over time
def plot_storage_levels_all_regions(storage_data, regions, storage_technologies):
    plt.figure(figsize=(14, 8))
    aggregated_storage_data = pd.DataFrame(columns=storage_data.columns)

    for region in regions:
        region_storage_data = storage_data[storage_data['node'].isin(regions[region])]
        if not region_storage_data.empty:
            aggregated_storage_data = pd.concat([aggregated_storage_data, region_storage_data], ignore_index=True)

    for tech in storage_technologies:
        tech_storage_data = aggregated_storage_data[aggregated_storage_data['technology'] == tech]
        if not tech_storage_data.empty:
            time_steps = tech_storage_data.columns[2:]
            storage_values = tech_storage_data.iloc[:, 2:].sum(axis=0).values / 1000
            if np.any(storage_values > 0.0001):
                plt.plot(time_steps, storage_values, label=f"{tech}", color=colors[tech])

    plt.xlabel('Time Steps', fontsize=15)
    plt.ylabel('Energy Capacity Level (TWh)', fontsize=15)
    plt.title('Energy Over Time', fontsize=15)
    plt.grid(True)

# Function to plot conversion levels over time
def plot_conversion_levels_all_regions(conversion_data, regions, conversion_technologies):
    # Filter rows where "carrier" column contains the word "electricity"
    conversion_data = conversion_data[conversion_data['carrier'].str.contains('electricity', na=False)]
    conversion_data = conversion_data.drop(columns=['carrier'])

    aggregated_conversion_data = pd.DataFrame(columns=conversion_data.columns)

    for region in regions:
        region_conversion_data = conversion_data[conversion_data['node'].isin(regions[region])]
        if not region_conversion_data.empty:
            aggregated_conversion_data = pd.concat([aggregated_conversion_data, region_conversion_data], ignore_index=True)

    for tech in conversion_technologies:
        tech_conversion_data = aggregated_conversion_data[aggregated_conversion_data['technology'] == tech]
        if not tech_conversion_data.empty:
            time_steps = tech_conversion_data.columns[2:]
            conversion_values = tech_conversion_data.iloc[:, 2:].sum(axis=0).values / 1000
            if np.any(conversion_values > 0.0001):
                plt.plot(time_steps, conversion_values, label=f"{tech} (Europe)", linestyle='--', color=colors[tech])

    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Storage_and_Conversion_Levels_Over_Time_Europe.png", format='png', bbox_inches='tight')

storage_data = r1.get_full_ts("storage_level")
storage_data = storage_data.reset_index()

conversion_data = r1.get_full_ts("flow_conversion_output")
conversion_data = conversion_data.reset_index()

plt.figure(figsize=(14, 8))
plot_storage_levels_all_regions(storage_data, regions, storage_technologies)
plot_conversion_levels_all_regions(conversion_data, regions, conversion_technologies)
