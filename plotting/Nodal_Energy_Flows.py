import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_18\\Results"

# Change this variable to the desired folder name
folder_name = "VPI_2024_25_8760"
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
#Positive Half of Axis
#Storage discharge
flow_storage_data = r.get_full_ts("flow_storage_discharge")
flow_storage_data.reset_index(inplace=True)
flow_storage_data = flow_storage_data[flow_storage_data['node'] == 'AT']
flow_storage_data = flow_storage_data[flow_storage_data['technology'] != 'natural_gas_storage']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fs = flow_storage_data.columns.difference(['technology', 'carrier', 'node'])
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
#flow_storage_data = flow_storage_data [~flow_storage_data [value_columns_fs].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
#flow_storage_data[value_columns_fs] = flow_storage_data[value_columns_fs] / 1000
flow_storage_data = flow_storage_data.groupby('technology').sum()
flow_storage_data.drop(columns=['node'], inplace=True)
#Conversion output
flow_conversion_output_data = r.get_full_ts("flow_conversion_output")
flow_conversion_output_data.reset_index(inplace=True)
# Filter rows where carrier is "electricity"
flow_conversion_output_data = flow_conversion_output_data[flow_conversion_output_data['carrier'] == 'electricity']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fc = flow_conversion_output_data.columns.difference(['technology', 'carrier', 'node'])
#flow_conversion_output_data = flow_conversion_output_data [~flow_conversion_output_data [value_columns_fc].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
#flow_conversion_output_data[value_columns_fs] = flow_conversion_output_data[value_columns_fc] / 1000
flow_conversion_output_data = flow_conversion_output_data.groupby('technology').sum()
flow_conversion_output_data.drop(columns=['carrier', 'node'], inplace=True)
#Flow transport minus losses
flow_transport_input = r.get_full_ts("flow_transport")
flow_transport_input.reset_index(inplace=True)
flow_transport_input_data = flow_transport_input[
    ((flow_transport_input['edge'] == 'CH-AT') | (flow_transport_input['edge'] == 'DE-AT')) &
    (flow_transport_input['technology'] == 'power_line')
]
flow_transport_input_loss = r.get_full_ts("flow_transport_loss")
flow_transport_input_loss.reset_index(inplace=True)
flow_transport_input_loss = flow_transport_input_loss[((flow_transport_input_loss['edge'] == 'DE-AT') |
                                          (flow_transport_input_loss['edge'] == 'CH-AT')) &
                                         (flow_transport_input_loss['technology'] == 'power_line')]
value_columns_ft = flow_transport_input_data.columns.difference(['technology', 'edge'])
flow_transport_input_data.loc[:,value_columns_ft] -= flow_transport_input_loss[value_columns_ft]
flow_transport_input_data.drop(columns=['edge'], inplace=True)
flow_transport_input_data = flow_transport_input_data.drop(columns=flow_transport_input_data.columns[0])
#flow_transport_input_data = flow_transport_input_data [~flow_transport_input_data [value_columns_ft].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
#flow_transport_input_data[value_columns_ft] = flow_transport_input_data[value_columns_ft] / 1000
# Drop the 'index' column (which contains the old indices)
flow_transport_input_data.drop(columns=['index'], inplace=True)

#Flow Import
flow_import = r.get_full_ts("flow_import")
flow_import = flow_import.reset_index()
flow_import = flow_import[flow_import['carrier'] == 'electricity']
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
#flow_import = flow_import [~flow_import [flow_import].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Concatenate dataframes
all_data_p = pd.concat([flow_storage_data, flow_conversion_output_data, flow_transport_input_data], axis=0)
# Transpose the data to have time steps as rows and technologies as columns
all_data_p = all_data_p.T
# Calculate the cumulative sum along the columns to stack the lines
cumulative_data_p = all_data_p.cumsum(axis=1)

#Negative Half of Axis
#Storage charge
flow_storage_data_n = r.get_full_ts("flow_storage_charge")
flow_storage_data_n.reset_index(inplace=True)
flow_storage_data_n = flow_storage_data_n[flow_storage_data['node'] == 'AT']
flow_storage_data_n.drop(labels=['natural_gas_storage'], axis=0, inplace=True)
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fsn = flow_storage_data_n.columns.difference(['technology', 'carrier', 'node'])
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
#flow_storage_data_n = flow_storage_data_n [~flow_storage_data_n [value_columns_fsn].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
#flow_storage_data_n[value_columns_fsn] = flow_storage_data_n[value_columns_fsn] / 1000
flow_storage_data_n = flow_storage_data_n.groupby('technology').sum()
#Conversion output
flow_conversion_input_data = r.get_full_ts("flow_conversion_input")
flow_conversion_input_data.reset_index(inplace=True)
# Filter rows where carrier is "electricity"
flow_conversion_input_data = flow_conversion_input_data[flow_conversion_input_data['carrier'] == 'electricity']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fcn = flow_conversion_input_data.columns.difference(['technology', 'carrier', 'node'])
#flow_conversion_input_data = flow_conversion_input_data [~flow_conversion_input_data [value_columns_fcn].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
#flow_conversion_input_data[value_columns_fsn] = flow_conversion_input_data[value_columns_fcn] / 1000
flow_conversion_input_data = flow_conversion_input_data.groupby('technology').sum()
flow_conversion_input_data.drop(columns=['carrier', 'node'], inplace=True)

#Flow transport minus losses
flow_transport_output = r.get_full_ts("flow_transport")
flow_transport_output.reset_index(inplace=True)
flow_transport_output_data = flow_transport_output[
    ((flow_transport_output['edge'] == 'AT-CH') | (flow_transport_output['edge'] == 'AT-DE')) &
    (flow_transport_output['technology'] == 'power_line')
]

#flow_transport_output_data = flow_transport_output_data [~flow_transport_output_data [value_columns_ft].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
#flow_transport_output_data[value_columns_ft] = flow_transport_output_data[value_columns_ft] / 1000

#Flow Export
flow_export = r.get_full_ts("flow_export")
flow_export = flow_export.reset_index()
flow_export = flow_export[flow_export['carrier'] == 'electricity']
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
#flow_export = flow_export [~flow_export [flow_export].apply(lambda row: row.between(0, 1).all(), axis=1)]

# Concatenate dataframes
all_data_n = pd.concat([flow_storage_data_n, flow_conversion_input_data, flow_transport_output_data], axis=0)
# Transpose the data to have time steps as rows and technologies as columns
all_data_n = all_data_n.T
# Calculate the cumulative sum along the columns to stack the lines
cumulative_data_n = all_data_n.cumsum(axis=1)

# Plot the stacked area plots
fig, ax = plt.subplots(figsize=(20, 8))

# Plot positive cumulative data
cumulative_data_p.plot(kind='area', ax=ax, linewidth=2, color=[color_map.get(x, 'gray') for x in cumulative_data_p.columns])
# Plot negative cumulative data
(-cumulative_data_n).plot(kind='area', ax=ax, linewidth=2, color=[color_map.get(x, 'gray') for x in cumulative_data_n.columns], alpha=0.5)
# Adjusting Y-axis limits
ax.set_ylim(-500, 1500)
# Set plot labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Power (TW)')
ax.set_title('Stacked Line Plots of Power Flows for All Technologies Over Time')
ax.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = out_folder1 + "\\Electricity_Flows_plot_Nodal.png"
plt.savefig(output_path)
