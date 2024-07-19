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

# Flow_Storage and Flow_Conversion
# Positive Half of Axis
# Storage discharge
flow_storage_data = r.get_full_ts("flow_storage_discharge")
flow_storage_data.drop(labels=['natural_gas_storage'], axis=0, inplace=True)
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fs = flow_storage_data.columns.difference(['technology', 'carrier', 'node'])
# Create a mask for the rows where all specified columns have values between 0 and 1
mask_fs = (flow_storage_data[value_columns_fs] >= 0) & (flow_storage_data[value_columns_fs] <= 1)
# Identify rows where all specified columns have values between 0 and 1
mask_all_within_range_fs = mask_fs.all(axis=1)
# Filter out the rows where all specified columns have values between 0 and 1
flow_storage_data = flow_storage_data[~mask_all_within_range_fs]
# Group by technology and sum
flow_storage_data = flow_storage_data.groupby('technology').sum()
# Conversion output
flow_conversion_output_data = r.get_full_ts("flow_conversion_output")
flow_conversion_output_data.reset_index(inplace=True)
# Filter rows where carrier is "electricity"
flow_conversion_output_data = flow_conversion_output_data[flow_conversion_output_data['carrier'] == 'electricity']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fc = flow_conversion_output_data.columns.difference(['technology', 'carrier', 'node'])
# Create a mask for the rows where all specified columns have values between 0 and 1
mask_fc = (flow_conversion_output_data[value_columns_fc] >= 0) & (flow_conversion_output_data[value_columns_fc] <= 1)
# Identify rows where all specified columns have values between 0 and 1
mask_all_within_range_fc = mask_fc.all(axis=1)
# Filter out the rows where all specified columns have values between 0 and 1
flow_conversion_output_data = flow_conversion_output_data[~mask_all_within_range_fc]
# Group by technology and sum
flow_conversion_output_data = flow_conversion_output_data.groupby('technology').sum()
flow_conversion_output_data.drop(columns=['carrier', 'node'], inplace=True)

# Concatenate dataframes for positive flows
all_data_p = pd.concat([flow_storage_data, flow_conversion_output_data], axis=0)
# Transpose the data to have time steps as rows and technologies as columns
all_data_p = all_data_p.T
all_data_p = all_data_p / 1000
# Calculate the cumulative sum along the columns to stack the lines
cumulative_data_p = all_data_p.cumsum(axis=1)

# Negative Half of Axis
# Storage charge
flow_storage_data_n = r.get_full_ts("flow_storage_charge")
flow_storage_data_n.drop(labels=['natural_gas_storage'], axis=0, inplace=True)
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fsn = flow_storage_data_n.columns.difference(['technology', 'carrier', 'node'])
# Create a mask for the rows where all specified columns have values between 0 and 1
mask_fsn = (flow_storage_data_n[value_columns_fsn] >= 0) & (flow_storage_data_n[value_columns_fsn] <= 1)
# Identify rows where all specified columns have values between 0 and 1
mask_all_within_range_fsn = mask_fsn.all(axis=1)
# Filter out the rows where all specified columns have values between 0 and 1
flow_storage_data_n = flow_storage_data_n[~mask_all_within_range_fsn]
# Group by technology and sum
flow_storage_data_n = flow_storage_data_n.groupby('technology').sum()
# Conversion input
flow_conversion_input_data = r.get_full_ts("flow_conversion_input")
flow_conversion_input_data.reset_index(inplace=True)
# Filter rows where carrier is "electricity"
flow_conversion_input_data = flow_conversion_input_data[flow_conversion_input_data['carrier'] == 'electricity']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fcn = flow_conversion_input_data.columns.difference(['technology', 'carrier', 'node'])
# Create a mask for the rows where all specified columns have values between 0 and 1
mask_fcn = (flow_conversion_input_data[value_columns_fcn] >= 0) & (flow_conversion_input_data[value_columns_fcn] <= 1)
# Identify rows where all specified columns have values between 0 and 1
mask_all_within_range_fcn = mask_fcn.all(axis=1)
# Filter out the rows where all specified columns have values between 0 and 1
flow_conversion_input_data = flow_conversion_input_data[~mask_all_within_range_fcn]
# Group by technology and sum
flow_conversion_input_data = flow_conversion_input_data.groupby('technology').sum()
flow_conversion_input_data.drop(columns=['carrier', 'node'], inplace=True)

# Concatenate dataframes for negative flows
all_data_n = pd.concat([flow_storage_data_n, flow_conversion_input_data], axis=0)
# Transpose the data to have time steps as rows and technologies as columns
all_data_n = all_data_n.T
all_data_n = all_data_n / 1000
# Calculate the cumulative sum along the columns to stack the lines
cumulative_data_n = all_data_n.cumsum(axis=1)

# Load demand data
demand_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_21\\Results\\demand.csv'  # Update this path as needed
demand_data = pd.read_csv(demand_path)

# Extract the "Demand(TWh)" column
demand_twh = demand_data["Demand(TWh)"]

# Plot the stacked area plots
fig, ax = plt.subplots(figsize=(20, 8))

# Plot positive cumulative data
cumulative_data_p.plot(kind='area', ax=ax, linewidth=2, color=[color_map.get(x, 'gray') for x in cumulative_data_p.columns])
# Plot negative cumulative data
(-cumulative_data_n).plot(kind='area', ax=ax, linewidth=2, color=[color_map.get(x, 'gray') for x in cumulative_data_n.columns], alpha=0.5)

# Plot demand data
ax.plot(demand_twh.index, demand_twh, color='black', linewidth=2, label='Demand')

# Adjusting Y-axis limits
ax.set_ylim(-5, 10)

# Set plot labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Power (TW)')
ax.set_title('Stacked Line Plots of Power Flows for All Technologies Over Time')
ax.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = out_folder1 + "\\Electricity_Flows_plot.png"
plt.savefig(output_path)
