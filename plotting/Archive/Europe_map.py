import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results
import os

# List of base folder paths
base_folders = [
    "C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Simulations\\00_Baseline\\Results"
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


def process_and_save_UP_capacity_data(data, capacity_type, threshold, out_folder, file_name, columns_to_check):
    # Filter data by capacity type
    data_filtered = data[data['capacity_type'] == capacity_type]

    # Filter data greater than the threshold
    data_filtered = data_filtered[(data_filtered[columns_to_check] > threshold).any(axis=1)].dropna()

    # Convert units to TW for power and TWh for energy
    data_filtered[columns_to_check] /= 1000

    # Group by technology and sum
    data_filtered.drop(columns=['capacity_type'], inplace=True)

    # Drop rows where 'technology' column is 'natural_gas_storage'
    data_filtered = data_filtered[data_filtered['technology'] != 'natural_gas_storage']

    # Save to CSV without the suffix
    data_filtered.to_csv(f"{out_folder}\\{file_name}.csv")

    return data_filtered


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

        data_1_energy_filtered = process_and_save_UP_capacity_data(data_1, 'energy', 1, out_folder1,
                                                                "data_UP_energy_filtered", columns_to_check)

        # Process and save power capacities without suffix
        data_1_power_filtered = process_and_save_UP_capacity_data(data_1, 'power', 0.001, out_folder1,
                                                               "data_UP_power_filtered", columns_to_check)

        # Extract technologies present in the filtered data
        technologies_filter = list(set(data_1_energy_filtered.index).union(set(data_1_power_filtered.index)))


        print(f"Processed folder: {folder_name} in base folder {base_folder}")