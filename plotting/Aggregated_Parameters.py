import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results
import os

# List of base folder paths
base_folders = [
    "C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Simulations\\00_Extreme_Pessimistic\\Results"
]

# List of folder names to process
folder_names = [
    "PI_HSP_FB_100PE_U1", "PI_HSP_FB_50PE_U1",
    "PI_HSP_FB_100PE_U2", "PI_HSP_FB_50PE_U2",
    "PI_HSP_FB_100PE_U3", "PI_HSP_FB_50PE_U3",
    "PI_HSP_FB_100PE_U4", "PI_HSP_FB_50PE_U4",
    "PI_HSP_FB_100PE_U5", "PI_HSP_FB_50PE_U5",
    "PI_HSP_FB_100PE_U6", "PI_HSP_FB_50PE_U6",
    "PI_HSP_FB_100PE_U7", "PI_HSP_FB_50PE_U7",
    "PI_HSP_FB_100PE_U8", "PI_HSP_FB_50PE_U8"
]


def process_and_save_capacity_data(data, capacity_type, threshold, out_folder, file_name, columns_to_check):
    # Filter data by capacity type
    data_filtered = data[data['capacity_type'] == capacity_type]

    # Filter data greater than the threshold
    data_filtered = data_filtered[(data_filtered[columns_to_check] > threshold).any(axis=1)].dropna()

    # Convert units to TW for power and TWh for energy
    data_filtered[columns_to_check] /= 1000

    # Group by technology and sum
    data_filtered = data_filtered.groupby('technology').sum()
    data_filtered.drop(columns=['capacity_type', 'location'], inplace=True)

    # Drop specific technologies if needed
    if 'natural_gas_storage' in data_filtered.index:
        data_filtered.drop(labels=['natural_gas_storage'], axis=0, inplace=True)

    # Save to CSV without the suffix
    data_filtered.to_csv(f"{out_folder}\\{file_name}.csv")

    return data_filtered


def process_and_save_cost_data(cost_dict, out_folder, file_name, filter_technologies=None):
    df = pd.DataFrame(cost_dict).reset_index()

    # Apply filter for specific technologies if provided
    if filter_technologies:
        df = df[df['technology'].isin(filter_technologies)]

    # Save to CSV without the suffix
    df.to_csv(f"{out_folder}\\{file_name}.csv", index=False)
    return df


# Loop over each folder name and process the data
for base_folder in base_folders:
    for folder_name in folder_names:
        out_folder1 = f"{base_folder}\\{folder_name}"

        # Ensure the output folder exists
        os.makedirs(out_folder1, exist_ok=True)

        r = Results(out_folder1)

        # Process and save energy capacities without suffix
        data_1 = r.get_total("capacity").reset_index()
        columns_to_check = data_1.columns.difference(['year', 'technology', 'capacity_type', 'location'])

        data_1_energy_filtered = process_and_save_capacity_data(data_1, 'energy', 1, out_folder1,
                                                                "data_1_energy_filtered", columns_to_check)

        # Process and save power capacities without suffix
        data_1_power_filtered = process_and_save_capacity_data(data_1, 'power', 0.001, out_folder1,
                                                               "data_1_power_filtered", columns_to_check)

        # Extract technologies present in the filtered data
        technologies_filter = list(set(data_1_energy_filtered.index).union(set(data_1_power_filtered.index)))

        # Process and save costs without suffix
        data_capex_total = r.get_total("cost_capex_total")
        data_opex_total = r.get_total("cost_opex_total")
        data_carrier_total = r.get_total("cost_carrier_total")
        data_carbon_emissions = r.get_df("cost_carbon_emissions_total")

        data_capex_total.to_csv(f"{out_folder1}\\data_capex_total.csv")
        data_opex_total.to_csv(f"{out_folder1}\\data_opex_total.csv")
        data_carrier_total.to_csv(f"{out_folder1}\\data_carrier_total.csv")

        # Convert dictionaries to DataFrames, filter for specific technologies, and save as CSV without suffix
        data_capex_split = process_and_save_cost_data(r.get_df("cost_capex"), out_folder1, "data_capex_split",
                                                      filter_technologies=technologies_filter)
        data_opex_split = process_and_save_cost_data(r.get_df("cost_opex"), out_folder1, "data_opex_split",
                                                     filter_technologies=technologies_filter)
        data_carrier_split = process_and_save_cost_data(r.get_df("cost_carrier"), out_folder1, "data_carrier_split")

        # Calculate cycles of operation
        data_cycles = (
                              (r.get_total("flow_storage_discharge").groupby('technology').sum() / r.get_total(
                                  "efficiency_discharge").groupby('technology').mean()) +
                              (r.get_total("flow_storage_charge").groupby('technology').sum() / r.get_total(
                                  "efficiency_charge").groupby('technology').mean())
                      ) / 2 / r.get_total('capacity').loc[:, 'energy', :].groupby('technology').sum()

        # Save the calculated cycles to a CSV file without the suffix
        data_cycles.to_csv(f"{out_folder1}\\data_cycles.csv")

        print(f"Processed folder: {folder_name} in base folder {base_folder}")

"""
import pandas as pd

# Load the data from the Excel file
file_path = 'C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Simulations\\00_Baseline\\Results\\Power_TW_Summary.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Define function to calculate totals
def calculate_totals(df, column, percentages, discharge_times):
    return df[(df['Percentage_of_total_costs_(%)'].isin(percentages)) &
              (df['Discharge_Time_(h)'].isin(discharge_times))][column].sum()

# Define parameters
percentages_100 = [100]
percentages_50 = [50]
discharge_times_2_4_8_16 = [2, 4, 8, 16]
discharge_times_20_50 = [20, 50]
discharge_times_100_150 = [100, 150]

# Perform calculations for 'battery'
battery_total_100_2_4_8_16 = calculate_totals(df, 'battery', percentages_100, discharge_times_2_4_8_16)
battery_total_50_2_4_8_16 = calculate_totals(df, 'battery', percentages_50, discharge_times_2_4_8_16)
battery_total_100_20_50 = calculate_totals(df, 'battery', percentages_100, discharge_times_20_50)
battery_total_50_20_50 = calculate_totals(df, 'battery', percentages_50, discharge_times_20_50)
battery_total_100_100_150 = calculate_totals(df, 'battery', percentages_100, discharge_times_100_150)
battery_total_50_100_150 = calculate_totals(df, 'battery', percentages_50, discharge_times_100_150)

# Perform calculations for 'up_devices'
up_devices_total_100_2_4_8_16 = calculate_totals(df, 'up_devices', percentages_100, discharge_times_2_4_8_16)
up_devices_total_50_2_4_8_16 = calculate_totals(df, 'up_devices', percentages_50, discharge_times_2_4_8_16)
up_devices_total_100_20_50 = calculate_totals(df, 'up_devices', percentages_100, discharge_times_20_50)
up_devices_total_50_20_50 = calculate_totals(df, 'up_devices', percentages_50, discharge_times_20_50)
up_devices_total_100_100_150 = calculate_totals(df, 'up_devices', percentages_100, discharge_times_100_150)
up_devices_total_50_100_150 = calculate_totals(df, 'up_devices', percentages_50, discharge_times_100_150)

# Perform calculations for 'hydrogen_storage'
hydrogen_storage_total_100_2_4_8_16 = calculate_totals(df, 'hydrogen_storage', percentages_100, discharge_times_2_4_8_16)
hydrogen_storage_total_50_2_4_8_16 = calculate_totals(df, 'hydrogen_storage', percentages_50, discharge_times_2_4_8_16)
hydrogen_storage_total_100_20_50 = calculate_totals(df, 'hydrogen_storage', percentages_100, discharge_times_20_50)
hydrogen_storage_total_50_20_50 = calculate_totals(df, 'hydrogen_storage', percentages_50, discharge_times_20_50)
hydrogen_storage_total_100_100_150 = calculate_totals(df, 'hydrogen_storage', percentages_100, discharge_times_100_150)
hydrogen_storage_total_50_100_150 = calculate_totals(df, 'hydrogen_storage', percentages_50, discharge_times_100_150)

# Print results
print("Battery Totals:")
print(battery_total_100_2_4_8_16, battery_total_50_2_4_8_16, battery_total_100_20_50, battery_total_50_20_50, battery_total_100_100_150, battery_total_50_100_150)

print("\nUp Devices Totals:")
print(up_devices_total_100_2_4_8_16, up_devices_total_50_2_4_8_16, up_devices_total_100_20_50, up_devices_total_50_20_50, up_devices_total_100_100_150, up_devices_total_50_100_150)

print("\nHydrogen Storage Totals:")
print(hydrogen_storage_total_100_2_4_8_16, hydrogen_storage_total_50_2_4_8_16, hydrogen_storage_total_100_20_50, hydrogen_storage_total_50_20_50, hydrogen_storage_total_100_100_150, hydrogen_storage_total_50_100_150)"""

"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results
import os

# List of base folder paths
base_folders = [
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\Results"
]

# List of folder names to process
folder_names = [
    "PI_HSP_FB_100PE_U1", "PI_HSP_FB_75PE_U1", "PI_HSP_FB_50PE_U1", "PI_HSP_FB_25PE_U1",
    "PI_HSP_FB_100PE_U2", "PI_HSP_FB_75PE_U2", "PI_HSP_FB_50PE_U2", "PI_HSP_FB_25PE_U2",
    "PI_HSP_FB_100PE_U3", "PI_HSP_FB_75PE_U3", "PI_HSP_FB_50PE_U3", "PI_HSP_FB_25PE_U3",
    "PI_HSP_FB_100PE_U4", "PI_HSP_FB_75PE_U4", "PI_HSP_FB_50PE_U4", "PI_HSP_FB_25PE_U4",
    "PI_HSP_FB_100PE_U5", "PI_HSP_FB_75PE_U5", "PI_HSP_FB_50PE_U5", "PI_HSP_FB_25PE_U5",
    "PI_HSP_FB_100PE_U6", "PI_HSP_FB_75PE_U6", "PI_HSP_FB_50PE_U6", "PI_HSP_FB_25PE_U6",
    "PI_HSP_FB_100PE_U7", "PI_HSP_FB_75PE_U7", "PI_HSP_FB_50PE_U7", "PI_HSP_FB_25PE_U7",
    "PI_HSP_FB_100PE_U8", "PI_HSP_FB_75PE_U8", "PI_HSP_FB_50PE_U8", "PI_HSP_FB_25PE_U8"
]


def process_and_save_capacity_data(data, capacity_type, threshold, out_folder, file_name, columns_to_check):
    # Filter data by capacity type
    data_filtered = data[data['capacity_type'] == capacity_type]

    # Filter data greater than the threshold
    data_filtered = data_filtered[(data_filtered[columns_to_check] > threshold).any(axis=1)].dropna()

    # Convert units to TW for power and TWh for energy
    data_filtered[columns_to_check] /= 1000

    # Group by technology and sum
    data_filtered = data_filtered.groupby('technology').sum()
    data_filtered.drop(columns=['capacity_type', 'location'], inplace=True)

    # Drop specific technologies if needed
    if 'natural_gas_storage' in data_filtered.index:
        data_filtered.drop(labels=['natural_gas_storage'], axis=0, inplace=True)

    # Save to CSV without the suffix
    data_filtered.to_csv(f"{out_folder}\\{file_name}.csv")

    return data_filtered


def process_and_save_cost_data(cost_dict, out_folder, file_name, filter_technologies=None):
    df = pd.DataFrame(cost_dict).reset_index()

    # Apply filter for specific technologies if provided
    if filter_technologies:
        df = df[df['technology'].isin(filter_technologies)]

    # Save to CSV without the suffix
    df.to_csv(f"{out_folder}\\{file_name}.csv", index=False)
    return df


# Loop over each folder name and process the data
for base_folder in base_folders:
    for folder_name in folder_names:
        out_folder1 = f"{base_folder}\\{folder_name}"

        # Ensure the output folder exists
        os.makedirs(out_folder1, exist_ok=True)

        r = Results(out_folder1)

        # Process and save energy capacities without suffix
        data_1 = r.get_total("capacity").reset_index()
        columns_to_check = data_1.columns.difference(['year', 'technology', 'capacity_type', 'location'])

        data_1_energy_filtered = process_and_save_capacity_data(data_1, 'energy', 1, out_folder1,
                                                                "data_1_energy_filtered", columns_to_check)

        # Process and save power capacities without suffix
        data_1_power_filtered = process_and_save_capacity_data(data_1, 'power', 0.001, out_folder1,
                                                               "data_1_power_filtered", columns_to_check)

        # Extract technologies present in the filtered data
        technologies_filter = list(set(data_1_energy_filtered.index).union(set(data_1_power_filtered.index)))

        # Process and save costs without suffix
        data_capex_total = r.get_total("cost_capex_total")
        data_opex_total = r.get_total("cost_opex_total")
        data_carrier_total = r.get_total("cost_carrier_total")
        data_carbon_emissions = r.get_df("cost_carbon_emissions_total")

        data_capex_total.to_csv(f"{out_folder1}\\data_capex_total.csv")
        data_opex_total.to_csv(f"{out_folder1}\\data_opex_total.csv")
        data_carrier_total.to_csv(f"{out_folder1}\\data_carrier_total.csv")

        # Convert dictionaries to DataFrames, filter for specific technologies, and save as CSV without suffix
        data_capex_split = process_and_save_cost_data(r.get_df("cost_capex"), out_folder1, "data_capex_split",
                                                      filter_technologies=technologies_filter)
        data_opex_split = process_and_save_cost_data(r.get_df("cost_opex"), out_folder1, "data_opex_split",
                                                     filter_technologies=technologies_filter)
        data_carrier_split = process_and_save_cost_data(r.get_df("cost_carrier"), out_folder1, "data_carrier_split")

        # Calculate cycles of operation
        data_cycles = (
                              (r.get_total("flow_storage_discharge").groupby('technology').sum() / r.get_total(
                                  "efficiency_discharge").groupby('technology').mean()) +
                              (r.get_total("flow_storage_charge").groupby('technology').sum() / r.get_total(
                                  "efficiency_charge").groupby('technology').mean())
                      ) / 2 / r.get_total('capacity').loc[:, 'energy', :].groupby('technology').sum()

        # Save the calculated cycles to a CSV file without the suffix
        data_cycles.to_csv(f"{out_folder1}\\data_cycles.csv")

        print(f"Processed folder: {folder_name} in base folder {base_folder}")
"""
