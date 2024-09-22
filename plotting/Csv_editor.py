import os
import pandas as pd

# Load the Excel file once
excel_file_path = r"C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\UP_MRFB_Costs_opex_specific_fixed.xlsx"
excel_data = pd.read_excel(excel_file_path, sheet_name=None)

# Define the base path to the simulation scenario
scenario_path = r"C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\{}"

# Replace "Extreme_Pessimistic_Map_Map" with your scenario variable (you can change this value)
scenario_name = "00_Extreme_Pessimistic"

# List of relative paths and their corresponding sheet names for opex_specific_fixed
file_sheet_mapping = {
    r"PI_HSP_FB_50PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U1",
    r"PI_HSP_FB_100PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U1",
    r"PI_HSP_FB_50PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U2",
    r"PI_HSP_FB_100PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U2",
    r"PI_HSP_FB_50PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U3",
    r"PI_HSP_FB_100PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U3",
    r"PI_HSP_FB_50PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U4",
    r"PI_HSP_FB_100PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U4",
    r"PI_HSP_FB_50PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U5",
    r"PI_HSP_FB_100PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U5",
    r"PI_HSP_FB_50PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U6",
    r"PI_HSP_FB_100PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U6",
    r"PI_HSP_FB_50PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U7",
    r"PI_HSP_FB_100PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U7",
    r"PI_HSP_FB_50PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\opex_specific_fixed.csv": "PI_HSP_FB_50PE_U8",
    r"PI_HSP_FB_100PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\opex_specific_fixed.csv": "PI_HSP_FB_100PE_U8"
}

# Iterate over each relative path and its corresponding sheet
for relative_path, sheet_name in file_sheet_mapping.items():
    # Construct the full path by combining the scenario path and relative path
    full_csv_path = os.path.join(scenario_path.format(scenario_name), relative_path)

    # Load the CSV file
    csv_data = pd.read_csv(full_csv_path)

    # Extract the corresponding column from the Excel sheet
    opex_specific_fixed_values = excel_data[sheet_name]['opex_specific_fixed']

    # Replace the values in the 'opex_specific_fixed' column
    csv_data['opex_specific_fixed'] = opex_specific_fixed_values

    # Save the modified CSV file
    csv_data.to_csv(full_csv_path, index=False)

print("All files updated successfully.")

"""import os
import pandas as pd

# Load the Excel file once
excel_file_path = r"C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\UP_MRFB_Costs_capex_specific_storage_energy.xlsx"
excel_data = pd.read_excel(excel_file_path, sheet_name=None)

# Define the base path to the simulation scenario
scenario_path = r"C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\{}"

# Replace "Extreme_Pessimistic_Map_Map" with your scenario variable (you can change this value)
scenario_name = "00_Extreme_Pessimistic"

# List of relative paths and their corresponding sheet names for capex_specific_storage_energy
file_sheet_mapping = {
    r"PI_HSP_FB_50PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U1",
    r"PI_HSP_FB_100PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U1",
    r"PI_HSP_FB_50PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U2",
    r"PI_HSP_FB_100PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U2",
    r"PI_HSP_FB_50PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U3",
    r"PI_HSP_FB_100PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U3",
    r"PI_HSP_FB_50PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U4",
    r"PI_HSP_FB_100PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U4",
    r"PI_HSP_FB_50PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U5",
    r"PI_HSP_FB_100PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U5",
    r"PI_HSP_FB_50PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U6",
    r"PI_HSP_FB_100PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U6",
    r"PI_HSP_FB_50PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U7",
    r"PI_HSP_FB_100PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U7",
    r"PI_HSP_FB_50PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\capex_specific_storage_energy.csv": "PI_HSP_FB_50PE_U8",
    r"PI_HSP_FB_100PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\capex_specific_storage_energy.csv": "PI_HSP_FB_100PE_U8"
}

# Iterate over each relative path and its corresponding sheet
for relative_path, sheet_name in file_sheet_mapping.items():
    # Construct the full path by combining the scenario path and relative path
    full_csv_path = os.path.join(scenario_path.format(scenario_name), relative_path)

    # Load the CSV file
    csv_data = pd.read_csv(full_csv_path)

    # Extract the corresponding column from the Excel sheet
    capex_specific_storage_energy_values = excel_data[sheet_name]['capex_specific_storage_energy']

    # Replace the values in the 'capex_specific_storage_energy' column
    csv_data['capex_specific_storage_energy'] = capex_specific_storage_energy_values

    # Save the modified CSV file
    csv_data.to_csv(full_csv_path, index=False)

print("All files updated successfully.")"""

"""import os
import pandas as pd

# Load the Excel file once
excel_file_path = r"C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\UP_MRFB_Costs_capex_specific_storage.xlsx"
excel_data = pd.read_excel(excel_file_path, sheet_name=None)

# Define the base path to the simulation scenario
scenario_path = r"C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\{}"

# Replace "Extreme_Pessimistic_Map_Map" with your scenario variable (you can change this value)
scenario_name = "00_Extreme_Pessimistic"

# List of relative paths and their corresponding sheet names (generic)
file_sheet_mapping = {
    r"PI_HSP_FB_50PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U1",
    r"PI_HSP_FB_100PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U1",
    r"PI_HSP_FB_50PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U2",
    r"PI_HSP_FB_100PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U2",
    r"PI_HSP_FB_50PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U3",
    r"PI_HSP_FB_100PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U3",
    r"PI_HSP_FB_50PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U4",
    r"PI_HSP_FB_100PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U4",
    r"PI_HSP_FB_50PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U5",
    r"PI_HSP_FB_100PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U5",
    r"PI_HSP_FB_50PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U6",
    r"PI_HSP_FB_100PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U6",
    r"PI_HSP_FB_50PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U7",
    r"PI_HSP_FB_100PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U7",
    r"PI_HSP_FB_50PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\capex_specific_storage.csv": "PI_HSP_FB_50PE_U8",
    r"PI_HSP_FB_100PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\capex_specific_storage.csv": "PI_HSP_FB_100PE_U8"
}

# Iterate over each relative path and its corresponding sheet
for relative_path, sheet_name in file_sheet_mapping.items():
    # Construct the full path by combining the scenario path and relative path
    full_csv_path = os.path.join(scenario_path.format(scenario_name), relative_path)

    # Load the CSV file
    csv_data = pd.read_csv(full_csv_path)

    # Extract the corresponding column from the Excel sheet
    capex_specific_storage_values = excel_data[sheet_name]['capex_specific_storage']

    # Replace the values in the 'capex_specific_storage' column
    csv_data['capex_specific_storage'] = capex_specific_storage_values

    # Save the modified CSV file
    csv_data.to_csv(full_csv_path, index=False)

print("All files updated successfully.")"""