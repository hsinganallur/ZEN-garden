import os
import pandas as pd

# Define the base directory path
base_dir = r"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\00_Extreme_Pessimistic\Results"
excel_file_path = os.path.join(base_dir, "Power_TW_Summary.xlsx")

# Load the existing Excel file
df_excel = pd.read_excel(excel_file_path)

# Define the mapping for discharge times based on folder names
discharge_time_mapping = {
    'U1': 2,
    'U2': 4,
    'U3': 8,
    'U4': 16,
    'U5': 20,
    'U6': 50,
    'U7': 100,
    'U8': 150
}

# Create a mapping of the technology names to the corresponding column in the Excel file
technology_to_column = {
    'battery': 'battery',
    'pumped_hydro': 'pumped_hydro',
    'hydrogen_storage': 'hydrogen_storage',
    'up_redox_flow_battery_1': 'up_redox_flow_battery_1',
    'up_redox_flow_battery_2': 'up_redox_flow_battery_2',
    'up_redox_flow_battery_3': 'up_redox_flow_battery_3',
    'up_redox_flow_battery_4': 'up_redox_flow_battery_4',
    'up_redox_flow_battery_5': 'up_redox_flow_battery_5',
    'up_redox_flow_battery_6': 'up_redox_flow_battery_6',
    'up_redox_flow_battery_7': 'up_redox_flow_battery_7',
    'up_redox_flow_battery_8': 'up_redox_flow_battery_8'
}

# Loop through the folders and fill data
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)

    # Check if it's a folder and has the required CSV file
    if os.path.isdir(folder_path) and 'data_1_power_filtered.csv' in os.listdir(folder_path):
        # Extract percentage of total costs and discharge time from the folder name
        parts = folder_name.split('_')
        percentage_str = parts[3].replace('PE', '')  # Extract percentage (100, 75, etc.)
        percentage = int(percentage_str)
        discharge_time_str = parts[-1]  # Extract discharge time (U1, U2, etc.)
        discharge_time = discharge_time_mapping[discharge_time_str]

        # Load the CSV data
        csv_file_path = os.path.join(folder_path, 'data_1_power_filtered.csv')
        df_csv = pd.read_csv(csv_file_path)

        # Find the corresponding row in the Excel file
        row_index = df_excel[(df_excel['Discharge_Time_(h)'] == discharge_time) &
                             (df_excel['Percentage_of_total_costs_(%)'] == percentage)].index[0]

        # Fill the corresponding row with the data from the CSV file
        for tech, col_name in technology_to_column.items():
            if tech in df_csv['technology'].values:
                # Get the value for the corresponding technology from the last column of the CSV
                value = df_csv[df_csv['technology'] == tech].iloc[:, -1].values[0]
                df_excel.at[row_index, col_name] = value
            else:
                # If the technology isn't mentioned, set the value to 0
                df_excel.at[row_index, col_name] = 0

# Save the updated Excel file
df_excel.to_excel(excel_file_path, index=False)

print(f"Data from all folders has been successfully added to {excel_file_path}")