import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_21\\Results"

# Change this variable to the desired folder name
folder_name = "VPI_2025_25_4380_All_Cost_Variations_Conversions"
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

# Power_Totals
# Filter rows where capacity_type is 'power' and technology is in a specified list
technologies_to_keep = ['biomass_plant_CCS', 'biomass_plant', 'hard_coal_plant','hard_coal_plant_CCS',
                        'lignite_coal_plant', 'natural_gas_turbine', 'natural_gas_turbine_CCS', 'nuclear',
                        'oil_plant', 'photovoltaics','reservoir_hydro', 'run-of-river_hydro',
                        'waste_plant', 'wind_offshore', 'wind_onshore', 'battery',
                        'hydrogen_storage', 'pumped_hydro', 'vanadium_redox_flow_battery', "up_redox_flow_battery_1",
                        "up_redox_flow_battery_2", "up_redox_flow_battery_3", "up_redox_flow_battery_4", "up_redox_flow_battery_5"]
data_1_power = data_1[(data_1['capacity_type'] == 'power') & (data_1['technology'].isin(technologies_to_keep))]
# Filter data greater than 1
data_1_power_filtered = data_1_power[(data_1_power[columns_to_check] > 1).any(axis=1)].dropna()
# Divide by 1000 - TW
data_1_power_filtered[columns_to_check] /= 1000
data_1_power_filtered = data_1_power_filtered.groupby('technology').sum()
data_1_power_filtered.drop(columns=['capacity_type', 'location'], inplace=True)
# Rename the second column to 'summed_value'
data_1_power_filtered.columns = [str(year) for year in range(2025, 2051)]
# Sort the data by the summed value in ascending order
# Define the list of columns to sort by
columns_to_sort_by_p = [str(year) for year in range(2025, 2051)]
# Ensure the columns exist in the DataFrame
existing_columns_to_sort_by = [col for col in columns_to_sort_by_p if col in data_1_power_filtered.columns]
# Sort each column in ascending order
data_1_power_filtered_sorted = data_1_power_filtered.apply(lambda x: sorted(x) if x.name in existing_columns_to_sort_by else x)
# Plotting_Power
ax = data_1_power_filtered_sorted.T.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis', color=[color_map.get(x, 'gray') for x in data_1_power_filtered_sorted.index])
ax.set_xlabel("Year")
ax.set_ylabel("Installed Power (TW)")
ax.set_title("Installed Power by Technology Over Years")
plt.legend(title="Technology")
plt.xticks(rotation=0)
plt.tight_layout()
# Save the plot
output_path = out_folder1 + "\\Installed_power_stacked_bar_plot.png"
plt.savefig(output_path)