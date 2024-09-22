import os
import pandas as pd

# Define the base directory path
base_dir = r"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\00_Extreme_Pessimistic\Results"
excel_file_path = os.path.join(base_dir, "Energy_TWh_Summary.xlsx")

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
    if os.path.isdir(folder_path) and 'data_1_energy_filtered.csv' in os.listdir(folder_path):
        # Extract percentage of total costs and discharge time from the folder name
        parts = folder_name.split('_')
        percentage_str = parts[3].replace('PE', '')  # Extract percentage (100, 75, etc.)
        percentage = int(percentage_str)
        discharge_time_str = parts[-1]  # Extract discharge time (U1, U2, etc.)
        discharge_time = discharge_time_mapping[discharge_time_str]

        # Load the CSV data
        csv_file_path = os.path.join(folder_path, 'data_1_energy_filtered.csv')
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

"""import os
import pandas as pd

# Map units to discharge times (in hours)
discharge_time_map = {
    'U1': 2,
    'U2': 4,
    'U3': 8,
    'U4': 16,
    'U5': 20,
    'U6': 50,
    'U7': 100,
    'U8': 150
}

# List of possible technologies
technologies = ['battery', 'pumped_hydro', 'hydrogen_storage',
                'up_redox_flow_battery_1', 'up_redox_flow_battery_2',
                'up_redox_flow_battery_3', 'up_redox_flow_battery_4',
                'up_redox_flow_battery_5', 'up_redox_flow_battery_6',
                'up_redox_flow_battery_7', 'up_redox_flow_battery_8']


# Function to process a file and extract data from the 5th column for each technology
def process_file(file_path, percentage, unit):
    discharge_time = discharge_time_map[unit]  # Get discharge time for the unit

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Initialize data dictionary with all technologies set to 0
    data = {tech: 0.0 for tech in technologies}

    # Check each technology in the file and extract the 5th column value
    for tech in technologies:
        if tech in df['technology'].values:  # Check if the technology exists in the file
            value = df[df['technology'] == tech].iloc[0, 5]  # Get the value from the 5th column
            data[tech] = value

    # Add additional fields
    data['Discharge_Time_(h)'] = discharge_time
    data['Percentage_of_total_costs_(%)'] = percentage

    return data


# Main function to walk through directories and create the summary Excel file
def create_summary_excel(results_folder, output_file):
    percentages = [100, 75, 50, 25]  # List of percentages
    units = ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8']  # List of units

    # List to store processed rows
    rows = []

    # Loop through percentages and units to build file paths
    for percentage in percentages:
        for unit in units:
            # Construct the file path
            folder_name = f"PI_HSP_FB_{percentage}PE_{unit}"
            file_path = os.path.join(results_folder, folder_name, f'data_1_energy_filtered_{unit}.csv')

            if os.path.exists(file_path):
                # Process the file and add the data to the rows list
                processed_data = process_file(file_path, percentage, unit)
                rows.append(processed_data)
            else:
                print(f"File not found: {file_path}")

    # Create DataFrame from the processed rows
    df = pd.DataFrame(rows)

    # Calculate the UP_Devices column (sum of up_redox_flow_battery_1 to up_redox_flow_battery_8)
    df['UP_Devices'] = df.loc[:, 'up_redox_flow_battery_1':'up_redox_flow_battery_8'].sum(axis=1)

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

    print(f"Excel file created: {output_file}")


# Example usage
results_folder = r'C:\#Users\Hareesh S P\Documents\MT_Simulations\Baseline_Map\Results'  # Root folder containing the result files
output_file = r'C:\#Users\Hareesh S P\Documents\MT_Simulations\Baseline_Map\Results\simulation_summary.xlsx'  # Output Excel file path

# Call the function to create the summary Excel file
create_summary_excel(results_folder, output_file)
"""