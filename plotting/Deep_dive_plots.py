import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

out_folder1 = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_8760"
r = Results(out_folder1)

#Capacities
data_1 = r.get_total("capacity")
data_1 = data_1.reset_index()
columns_to_check = data_1.columns[3:]

#Power_Totals
data_1_power = data_1[data_1['capacity_type'] == 'power']
# Filter data greater than 1
data_1_power_filtered = data_1_power[(data_1_power[columns_to_check] > 1).any(axis=1)].dropna()
# Divide by 1000 - TW
data_1_power_filtered[columns_to_check] /= 1000
data_1_power_filtered = (data_1_power_filtered.groupby('technology').sum())
data_1_power_filtered.drop(columns=['capacity_type','location'],inplace=True)

#Plotting_Power
ax = data_1_power_filtered.T.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis')
ax.set_xlabel("Year")
ax.set_ylabel("Installed Power (TW)")
ax.set_title("Installed Power by Technology Over Years")
plt.legend(title="Technology")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\installed_power_stacked_bar_plot.png"
plt.savefig(output_path)

#Energy_Totals
# Step 1: Filter data_1 for energy capacity type
data_1_energy = data_1[data_1['capacity_type'] == 'energy']

# Step 2: Filter data greater than 1
data_1_energy_filtered = data_1_energy[(data_1_energy[columns_to_check] > 1).any(axis=1)].dropna()

# Step 3: Convert units to TWh
data_1_energy_filtered[columns_to_check] /= 1000

# Step 4: Group by technology and sum
data_1_energy_filtered = data_1_energy_filtered.groupby('technology').sum()
data_1_energy_filtered.drop(columns=['capacity_type', 'location'], inplace=True)

# Step 5: Plotting installed energy over years
ax = data_1_energy_filtered.T.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis')
ax.set_xlabel("Year")
ax.set_ylabel("Installed Energy (TWh)")
ax.set_title("Installed Energy Technology Over Years")
plt.legend(title="Technology")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\installed_energy_stacked_bar_plot.png"
plt.savefig(output_path)

# Step 6: Calculate cycles of operation
data_cycles = ((r.get_total("flow_storage_discharge").groupby('technology').sum() / r.get_total("efficiency_discharge").groupby('technology').mean()) + (r.get_total("flow_storage_charge").groupby('technology').sum() / r.get_total("efficiency_charge").groupby('technology').mean())) / 2 / r.get_total('capacity').loc[:, 'energy', :].groupby('technology').sum()

# Step 7: Reset index to access the 'technology' column
data_cycles_reset = data_cycles.reset_index()

# Step 8: Filter data_cycles to keep only technologies present in data_1_energy_filtered
technologies_in_energy = data_1_energy_filtered.index
data_cycles_filtered = data_cycles_reset[data_cycles_reset['technology'].isin(technologies_in_energy)]

# Step 9: Plotting cycles of operation by technology
fig, ax = plt.subplots(figsize=(14, 8))
technologies = data_cycles_filtered['technology']
cycles = data_cycles_filtered.iloc[:, 1:].values.flatten()  # exclude the 'technology' column

# Creating a bar plot
ax.bar(technologies, cycles, color='skyblue')

# Adding labels and title
ax.set_xlabel("Technology")
ax.set_ylabel("Cycles of Operation")
ax.set_title("Cycles of Operation by Technology")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\cycles_of_operation_bar_plot.png"
plt.savefig(output_path)

#Flow_Storage and Flow_Conversion
flow_storage_data = r.get_full_ts("flow_storage_discharge").groupby('technology').sum()
flow_conversion_output_data = r.get_full_ts("flow_conversion_output").groupby('technology').sum()

# Concatenate both dataframes
all_data = pd.concat([flow_storage_data, flow_conversion_output_data], axis=0)

# Drop rows where all columns after the first one are zero
all_data = all_data[~(all_data.iloc[:, 1:] < 1).all(axis=1)]

# Transpose the data to have time steps as rows and technologies as columns
all_data = all_data.T

# Calculate the cumulative sum along the columns to stack the lines
cumulative_data = all_data.cumsum(axis=1)

# Plot the stacked line plots
cumulative_data.plot(kind='line', figsize=(14, 8), linewidth=2)

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Cumulative Energy')
plt.title('Stacked Line Plots of Energy for All Technologies Over Time')
plt.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\Flow_conversion_storage_plot.png"
plt.savefig(output_path)

#Storage Levels
storage_levels = r.get_full_ts("storage_level").groupby('technology').sum()
# Drop rows where all columns after the first one are zero
storage_levels = storage_levels[~(storage_levels.iloc[:, 1:] < 1).all(axis=1)]

# Transpose the data to have time steps as rows and technologies as columns
storage_levels = storage_levels.T

storage_levels.plot(kind='line', figsize=(14, 8), linewidth=2)

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Storage Levels (TWh)')
plt.title('Stacked Line Plots of Storage Levels for All Technologies Over Time')
plt.legend(title='Technology', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\Storage_level_plot.png"
plt.savefig(output_path)


#Costs
data_capex = r.get_total("cost_capex_total")
data_opex = r.get_total("cost_opex_total")
data_carbon_emissions = r.get_total("cost_carbon_emissions_total")
data_carrier = r.get_total("cost_carrier_total")
data_total_costs = r.get_total("cost_total")

# Ensure each element is a scalar value
costs = [
    float(data_capex) if hasattr(data_capex, 'iloc') else data_capex,
    float(data_opex) if hasattr(data_opex, 'iloc') else data_opex,
    float(data_carbon_emissions) if hasattr(data_carbon_emissions, 'iloc') else data_carbon_emissions,
    float(data_carrier) if hasattr(data_carrier, 'iloc') else data_carrier,
    float(data_total_costs) if hasattr(data_total_costs, 'iloc') else data_total_costs
]

# Data for plotting
categories = ['Capex', 'Opex', 'Carbon Emissions', 'Carrier', 'Total Costs']

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(categories, costs, color=['blue', 'green', 'red', 'purple', 'grey'])
plt.xlabel('Cost Categories')
plt.ylabel('Costs')
plt.title('Costs Breakdown')
plt.grid(True)

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\Costs_plot.png"
plt.savefig(output_path)

#Shed Demand
data_shed_demand = r.get_total("cost_shed_demand").groupby('carrier').sum()

# Assuming 'carrier' is either the index or a column in data_shed_demand
carriers = data_shed_demand.index  # If carrier is the index

costs = data_shed_demand.sum(axis=1)  # Summing costs across all years

# Plotting
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(carriers, costs, color='skyblue')
plt.xlabel('Carriers')
plt.ylabel('Total Cost')
plt.title('Total Cost by Carrier')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()

# Save the plot
output_path = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\VPI_FB_G4_80\\Shed_Demand_plot.png"
plt.savefig(output_path)