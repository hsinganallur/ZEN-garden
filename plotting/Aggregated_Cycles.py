import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_28\\Results"

# Change this variable to the desired folder name
folder_name = "PI_HSP_FB_EP"
out_folder1 = f"{base_folder}\\{folder_name}"
r = Results(out_folder1)

# Define colors for each technology category
color_map= {
    "DAC": 'aqua',
    "biomass_boiler": 'darkseagreen',
    "biomass_boiler_DH": 'lightseagreen',
    "biomass_plant": 'springgreen',
    "biomass_plant_CCS": 'mediumseagreen',
    "carbon_storage": 'limegreen',
    "district_heating_grid": 'lime',
    "electrode_boiler": 'mediumspringgreen',
    "electrode_boiler_DH": 'darkgreen',
    "hard_coal_boiler": 'brown',
    "hard_coal_boiler_DH": 'darkred',
    "hard_coal_plant": 'firebrick',
    "hard_coal_plant_CCS": 'maroon',
    "heat_pump": 'yellowgreen',
    "heat_pump_DH": 'olive',
    "lignite_coal_plant": 'chocolate',
    "lng_terminal": 'peru',
    "natural_gas_boiler": 'darkgoldenrod',
    "natural_gas_boiler_DH": 'goldenrod',
    "natural_gas_turbine": 'khaki',
    "natural_gas_turbine_CCS": 'gold',
    "nuclear": 'slateblue',
    "oil_boiler": 'orangered',
    "oil_boiler_DH": 'coral',
    "oil_plant": 'tomato',
    "photovoltaics": 'orange',
    "reservoir_hydro": 'skyblue',
    "run-of-river_hydro": 'deepskyblue',
    "waste_boiler_DH": 'lightblue',
    "waste_plant": 'powderblue',
    "wind_offshore": 'aquamarine',
    "wind_onshore": 'deeppink',
    "battery": 'darkslategray',
    "hydrogen_storage": 'teal',
    "natural_gas_storage": 'darkturquoise',
    "pumped_hydro": 'cadetblue',
    "carbon_pipeline": 'lightsteelblue',
    "natural_gas_pipeline": 'steelblue',
    "power_line": 'darkslateblue',
    "vanadium_redox_flow_battery": 'mediumblue',
    "up_redox_flow_battery_1": 'blue',
    "up_redox_flow_battery_2": 'royalblue',
    "up_redox_flow_battery_3": 'cornflowerblue',
    "up_redox_flow_battery_4": 'lightblue',
    "up_redox_flow_battery_5": 'powderblue'
}

# Capacities
data_1 = r.get_total("capacity")
data_1 = data_1.reset_index()
columns_to_check = data_1.columns.difference(['year', 'technology', 'capacity_type', 'location'])

# Energy_Totals
# Filter data_1 for energy capacity type
data_1_energy = data_1[data_1['capacity_type'] == 'energy']
# Filter data greater than 1
data_1_energy_filtered = data_1_energy[(data_1_energy[columns_to_check] > 1).any(axis=1)].dropna()
# Convert units to TWh
data_1_energy_filtered[columns_to_check] /= 1000
# Group by technology and sum
data_1_energy_filtered = data_1_energy_filtered.groupby('technology').sum()
data_1_energy_filtered.drop(columns=['capacity_type', 'location'], inplace=True)
data_1_energy_filtered.drop(labels=['natural_gas_storage'], axis=0, inplace=True)

# Calculate cycles of operation
data_cycles = ((r.get_total("flow_storage_discharge").groupby('technology').sum() / r.get_total("efficiency_discharge").groupby('technology').mean()) + (r.get_total("flow_storage_charge").groupby('technology').sum() / r.get_total("efficiency_charge").groupby('technology').mean())) / 2 / r.get_total('capacity').loc[:, 'energy', :].groupby('technology').sum()
# Reset index to access the 'technology' column
data_cycles_reset = data_cycles.reset_index()
# Filter data_cycles to keep only technologies present in data_1_energy_filtered
technologies_in_energy = data_1_energy_filtered.index
data_cycles_filtered = data_cycles_reset[data_cycles_reset['technology'].isin(technologies_in_energy)]
# Plotting cycles of operation by technology
fig, ax = plt.subplots(figsize=(14, 8))
technologies = data_cycles_filtered['technology']
cycles = data_cycles_filtered.iloc[:, 1:].values.flatten()  # exclude the 'technology' column
# Creating a bar plot
ax.bar(technologies, cycles, color=[color_map.get(x, 'gray') for x in technologies])
# Adding labels and title
ax.set_xlabel("Technology")
ax.set_ylabel("Cycles of Operation")
ax.set_title("Cycles of Operation by Technology")
plt.xticks(rotation=0)
plt.tight_layout()
# Save the plot
output_path = out_folder1 + "\\Cycles_of_operation_bar_plot.png"
plt.savefig(output_path)