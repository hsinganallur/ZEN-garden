import json

# List of file paths
file_paths = [
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_25PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_50PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_75PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_100PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_25PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_50PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_75PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_100PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_25PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_50PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_75PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\00_Baseline\\PI_HSP_FB_100PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",

]

# New values for efficiency_charge and efficiency_discharge
new_efficiency_charge = 0.8366600265340755# Change this to the new value
new_efficiency_discharge = 0.8366600265340755# Change this to the new value

def update_efficiency_values(file_path, charge_value, discharge_value):
    # Open the JSON file and load it into a Python dictionary
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Update the specific values
    data['efficiency_charge']['default_value'] = charge_value
    data['efficiency_discharge']['default_value'] = discharge_value

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Values updated successfully in {file_path}")


# Loop through each file path and update the values
for path in file_paths:
    update_efficiency_values(path, new_efficiency_charge, new_efficiency_discharge)


"""
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U1\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_1\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U2\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_2\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U3\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_3\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U4\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_4\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U5\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_5\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U6\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_6\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U7\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_7\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_25PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_50PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_75PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",
    "C:\\Users\\Hareesh S P\\Documents\\MT_Simulations\\Extreme_Pessimistic_Map_Map\\PI_HSP_FB_100PE_U8\\set_technologies\\set_storage_technologies\\up_redox_flow_battery_8\\attributes.json",

"""