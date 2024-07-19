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
data_1_power_filtered.columns = [str(year) for year in range(2024, 2049)]
# Sort the data by the summed value in ascending order
# Define the list of columns to sort by
columns_to_sort_by_p = [str(year) for year in range(2024, 2049)]
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
# Rename the second column to 'summed_value'
data_1_energy_filtered.columns = [str(year) for year in range(2024, 2049)]
# Sort the data by the summed value in ascending order
# Define the list of columns to sort by
columns_to_sort_by_e = [str(year) for year in range(2024, 2049)]
# Sort the DataFrame by these columns in ascending order
data_1_energy_filtered_sorted = [col for col in columns_to_sort_by_e if col in data_1_energy_filtered.columns]
data_1_energy_filtered_sorted = data_1_energy_filtered.apply(lambda x: sorted(x) if x.name in columns_to_sort_by_e else x)
# Plotting installed energy over years
ax = data_1_energy_filtered_sorted.T.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis', color=[color_map.get(x, 'gray') for x in data_1_energy_filtered_sorted.index])
ax.set_xlabel("Year")
ax.set_ylabel("Installed Energy (TWh)")
ax.set_title("Installed Energy Technology Over Years")
plt.legend(title="Technology")
plt.xticks(rotation=0)
plt.tight_layout()
# Save the plot
output_path = out_folder1 + "\\Installed_energy_stacked_bar_plot.png"
plt.savefig(output_path)

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

# Flow_Storage and Flow_Conversion
#Positive Half of Axis
#Storage discharge
flow_storage_data = r.get_full_ts("flow_storage_discharge")
flow_storage_data.drop(labels=['natural_gas_storage'], axis=0, inplace=True)
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fs = flow_storage_data.columns.difference(['technology', 'carrier', 'node'])
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
flow_storage_data = flow_storage_data [~flow_storage_data [value_columns_fs].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
flow_storage_data[value_columns_fs] = flow_storage_data[value_columns_fs] / 1000
flow_storage_data = flow_storage_data.groupby('technology').sum()
#Conversion output
flow_conversion_output_data = r.get_full_ts("flow_conversion_output")
flow_conversion_output_data.reset_index(inplace=True)
# Filter rows where carrier is "electricity"
flow_conversion_output_data = flow_conversion_output_data[flow_conversion_output_data['carrier'] == 'electricity']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fc = flow_conversion_output_data.columns.difference(['technology', 'carrier', 'node'])
flow_conversion_output_data = flow_conversion_output_data [~flow_conversion_output_data [value_columns_fc].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
flow_conversion_output_data[value_columns_fs] = flow_conversion_output_data[value_columns_fc] / 1000
flow_conversion_output_data = flow_conversion_output_data.groupby('technology').sum()
flow_conversion_output_data.drop(columns=['carrier', 'node'], inplace=True)
#Flow transport minus losses
flow_transport_output = r.get_full_ts("flow_transport")
flow_transport_output_loss = r.get_full_ts("flow_transport_loss")
flow_transport_output_data = flow_transport_output - flow_transport_output_loss
value_columns_ft = flow_transport_output_data.columns.difference(['technology', 'edge'])
flow_transport_output_data = flow_transport_output_data [~flow_transport_output_data [value_columns_ft].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
flow_transport_output_data[value_columns_ft] = flow_transport_output_data[value_columns_ft] / 1000
#Flow Import
flow_import = r.get_full_ts("flow_import")
flow_import = flow_import.reset_index()
flow_import = flow_import[flow_import['carrier'] == 'electricity']
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
flow_import = flow_import [~flow_import [flow_import].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Concatenate dataframes
all_data_p = pd.concat([flow_storage_data, flow_conversion_output_data], axis=0)
# Transpose the data to have time steps as rows and technologies as columns
all_data_p = all_data_p.T
# Calculate the cumulative sum along the columns to stack the lines
cumulative_data_p = all_data_p.cumsum(axis=1)

#Negative Half of Axis
#Storage charge
flow_storage_data_n = r.get_full_ts("flow_storage_charge")
flow_storage_data_n.drop(labels=['natural_gas_storage'], axis=0, inplace=True)
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fsn = flow_storage_data_n.columns.difference(['technology', 'carrier', 'node'])
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
flow_storage_data_n = flow_storage_data_n [~flow_storage_data_n [value_columns_fsn].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
flow_storage_data_n[value_columns_fsn] = flow_storage_data_n[value_columns_fsn] / 1000
flow_storage_data_n = flow_storage_data_n.groupby('technology').sum()
#Conversion output
flow_conversion_input_data = r.get_full_ts("flow_conversion_input")
flow_conversion_input_data.reset_index(inplace=True)
# Filter rows where carrier is "electricity"
flow_conversion_input_data = flow_conversion_input_data[flow_conversion_input_data['carrier'] == 'electricity']
# Identify the columns that contain the values to check (excluding the 'technology', 'carrier', and 'node' columns)
value_columns_fcn = flow_conversion_input_data.columns.difference(['technology', 'carrier', 'node'])
flow_conversion_input_data = flow_conversion_input_data [~flow_conversion_input_data [value_columns_fcn].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
flow_conversion_input_data[value_columns_fsn] = flow_conversion_input_data[value_columns_fcn] / 1000
flow_conversion_input_data = flow_conversion_input_data.groupby('technology').sum()
flow_conversion_input_data.drop(columns=['carrier', 'node'], inplace=True)
#Flow transport minus losses
flow_transport_output_n = r.get_full_ts("flow_transport")
flow_transport_output_data_n = flow_transport_output_n
value_columns_ftn = flow_transport_output_data_n.columns.difference(['technology', 'edge'])
flow_transport_output_data_n = flow_transport_output_data_n [~flow_transport_output_data_n [value_columns_ftn].apply(lambda row: row.between(0, 1).all(), axis=1)]
# Divide the specified columns by 1000
flow_transport_output_data_n[value_columns_ftn] = flow_transport_output_data_n[value_columns_ftn] / 1000
#Flow Export
flow_export = r.get_full_ts("flow_export")
flow_export = flow_export.reset_index()
flow_export = flow_export[flow_export['carrier'] == 'electricity']
# Filter the DataFrame to drop rows where all values in `value_columns` are between 0 and 1
flow_export = flow_export [~flow_export [flow_export].apply(lambda row: row.between(0, 1).all(), axis=1)]

# Concatenate dataframes
all_data_n = pd.concat([flow_storage_data_n, flow_conversion_input_data], axis=0)
# Transpose the data to have time steps as rows and technologies as columns
all_data_n = all_data_n.T
# Calculate the cumulative sum along the columns to stack the lines
cumulative_data_n = all_data_n.cumsum(axis=1)

# Plot positive cumulative data
cumulative_data_p.plot(kind='area', ax=ax, linewidth=2, color=[color_map.get(x, 'gray') for x in cumulative_data_p.columns])
# Plot negative cumulative data
(-cumulative_data_n).plot(kind='area', ax=ax, linewidth=2, color=[color_map.get(x, 'gray') for x in cumulative_data_n.columns], alpha=0.5)
# Adjusting Y-axis limits
ax.set_ylim(-0.8, 0.8)
# Set plot labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Power (TW)')
ax.set_title('Stacked Line Plots of Power Flows for All Technologies Over Time')
ax.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = out_folder1 + "\\Flow_conversion_storage_plot.png"
plt.savefig(output_path)



# Storage Levels
storage_levels = r.get_full_ts("storage_level").groupby('technology').sum()
# Drop rows where all columns after the first one are zero
storage_levels = storage_levels[~(storage_levels.iloc[:, 1:] < 1).all(axis=1)]
storage_levels.drop(labels=['natural_gas_storage'], axis=0, inplace=True)
# Divide the specified columns by 1000
value_columns_sl = storage_levels.columns.difference(['technology'])
storage_levels[value_columns_sl] = storage_levels[value_columns_sl] / 1000
# Transpose the data to have time steps as rows and technologies as columns
storage_levels = storage_levels.T
storage_levels.plot(kind='line', figsize=(14, 8), linewidth=2, color=[color_map.get(x, 'gray') for x in storage_levels.columns])

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Storage Levels (TWh)')
plt.title('Stacked Line Plots of Storage Levels for All Technologies Over Time')
plt.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
# Save the plot
output_path = out_folder1 + "\\Storage_level_plot.png"
plt.savefig(output_path)

# Costs
data_capex = r.get_df("cost_capex_total")
data_opex = r.get_df("cost_opex_total")
data_carbon_emissions = r.get_df("cost_carbon_emissions_total")
data_carrier = r.get_df("cost_carrier_total")
data_total_costs = r.get_df("cost_total")

# Shed Demand
data_shed_demand = r.get_total("cost_shed_demand").groupby('carrier').sum()
print(data_shed_demand)
