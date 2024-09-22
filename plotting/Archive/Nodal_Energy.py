import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_20\\Results"

# Change this variable to the desired folder name
folder_name = "VPI_2025_25_4380"
out_folder1 = f"{base_folder}\\{folder_name}"
r = Results(out_folder1)

# Define colors for each technology category
color_map = {
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

# Prepare data for each location ('DE', 'AT', 'CH')
locations = ["AT", "CH", "DE","BG",
    "NL","LU","FR"]

# Create a single figure with subplots for each location
fig, axes = plt.subplots(nrows=1, ncols=len(locations), figsize=(18, 6), sharey=True)

plot_output_paths = []
handles = []
labels = []

for idx, location in enumerate(locations):
    data_location = data_1[(data_1['capacity_type'] == 'energy') &
                           (data_1['location'] == location)]

    # Filter data greater than 1
    data_location_filtered = data_location[(data_location[columns_to_check] > 1).any(axis=1)].dropna()
    # Convert units to TWh
    data_location_filtered[columns_to_check] /= 1000
    # Group by technology and sum
    data_location_filtered = data_location_filtered.groupby('technology').sum()
    # Drop unnecessary columns
    data_location_filtered.drop(columns=['capacity_type', 'location'], inplace=True)
    data_location_filtered.drop(labels=['natural_gas_storage'], axis=0, inplace=True, errors='ignore')
    # Sum columns and add result as a new column
    data_location_filtered['total'] = data_location_filtered[columns_to_check].sum(axis=1)
    # Sort the data by the summed value in ascending order
    data_location_filtered_sorted = data_location_filtered.sort_values(by='total', ascending=True)

    # Plotting the stacked bar plot for the current location
    bottom_values = np.zeros(len(data_location_filtered_sorted))
    x = [location]

    for tech in data_location_filtered_sorted.index:
        bars = axes[idx].bar(x, data_location_filtered_sorted.loc[tech, 'total'], bottom=bottom_values, label=tech,
                             color=color_map.get(tech, 'gray'))
        bottom_values += data_location_filtered_sorted.loc[tech, 'total']
        handles.append(bars)
        labels.append(tech)

    # Add labels and title to each subplot
    axes[idx].set_xlabel('Location')
    axes[idx].set_title(f'Stacked Bar Plot of Installed Energy by Technology in {location}')

# Add common y-axis label
axes[0].set_ylabel('Installed Energy (TWh)')

# Create a single legend for the entire figure outside the plot
fig.legend(handles, labels, loc='upper left', bbox_to_anchor=(1.1, 1))

# Adjust layout
plt.tight_layout()

# Save the combined plot
output_path = out_folder1 + "\\Combined_installed_energy_stacked_bar_plot.png"
plt.savefig(output_path, bbox_inches='tight')

# Show the combined plot
plt.show()
