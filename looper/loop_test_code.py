import subprocess
import read_results
import pandas as pd
import os
import shutil
import sys
# Add the directory containing system.py to the Python path
sys.path.append("C:\\GitHub\\ZEN-garden\\data\\looping_test_folder")
# Import system from system.py
from system import system

#################################################### Functions ####################################################
def get_years_of_operation(reference_year, optimized_years, interval_between_years):
    return [reference_year + i * interval_between_years for i in range(optimized_years)]

def run_zen_garden(config_file="./config.py", dataset=None, job_index=None):
    # Construct the command to run the ZEN-Garden module
    command = ["python", "-m", "zen_garden", "--config", config_file]

    if dataset:
        command.extend(["--dataset", dataset])

    if job_index:
        command.extend(["--job_index", job_index])

    # Run the ZEN-Garden module
    subprocess.run(command)

#################################################### Functions ####################################################

# Specify the configuration file, if needed
config_file = "C:\\GitHub\\ZEN-garden\\data\\config.py"
dataset_path = "C:\\GitHub\\ZEN-garden\\data\\looping_test_folder"
results_path = "C:\\GitHub\\ZEN-garden\\data\\outputs\\looping_test_folder"
storage_path = "C:\\GitHub\\ZEN-garden\\looper\\storage_test_folder"

# Read parameters from system variable
reference_year = system["reference_year"]
optimized_years = system["optimized_years"]
interval_between_years = system["interval_between_years"]

# Calculate years of operation
years_of_operation = get_years_of_operation(reference_year, optimized_years, interval_between_years)
#print("Years of operation:", years_of_operation)

# Extend it for the number of nodes
# Count the number of set_nodes
num_set_nodes = len(system["set_nodes"])

# Repeat years_of_operation for num_set_nodes times
years_of_operation_corrected = years_of_operation * num_set_nodes

#################################################### Running ZEN-garden and outputting results ####################################################

for i, year in enumerate(years_of_operation, start=1):
    print(f"Running iteration {i}...")

    # Setting up and solving optimization problem in ZEN-Garden module
    run_zen_garden(config_file, dataset_path)
    # Analyzing results
    r = read_results.Results(results_path)

    cn_1 = "capacity"
    cn_2 = "storage_level"
    cn_3 = "flow_storage_charge"
    cn_4 = "flow_storage_discharge"

    df_1 = r.get_df(cn_1)
    df_1 = pd.DataFrame(df_1)
    df_2 = r.get_df(cn_2)
    df_2 = pd.DataFrame(df_2)
    df_3 = r.get_total(cn_3)
    df_3 = pd.DataFrame(df_3)
    df_4 = r.get_total(cn_4)
    df_4 = pd.DataFrame(df_4)

    # Create Run folder
    run_path = os.path.join(storage_path, f"Run {i}")
    # Create a new folder for each run
    os.makedirs(run_path, exist_ok=True)

    # Store results
    fn_1 = 'capacity.csv'
    fn_2 = 'storage_level.csv'
    fn_3 = 'flow_storage_charge.csv'
    fn_4 = 'flow_storage_discharge.csv'

    fp_1 = os.path.join(run_path, fn_1)
    fp_2 = os.path.join(run_path, fn_2)
    fp_3 = os.path.join(run_path, fn_3)
    fp_4 = os.path.join(run_path, fn_4)

    # Save the DataFrame as a CSV file in the specified directory
    df_1.to_csv(fp_1, index=True, mode='w')
    df_2.to_csv(fp_2, index=True, mode='w')
    df_3.to_csv(fp_3, index=True, mode='w')
    df_4.to_csv(fp_4, index=True, mode='w')

    # Calculating number of cycles at each node and each node of operation

    # Reset indexes and set the first column as 'technology'
    df_3_reset_charge = df_3.reset_index()
    df_3_reset_charge.columns = ['technology'] + df_3_reset_charge.columns[1:].tolist()
    charge_df = df_3_reset_charge.loc[(df_3_reset_charge['technology'].str.strip() == 'vanadium_redox_flow_battery')]

    print("Charge DataFrame before summing:")
    print(charge_df.head())

    # Reset indexes and set the first column as 'technology'
    df_4_reset_discharge = df_4.reset_index()
    df_4_reset_discharge.columns = ['technology'] + df_4_reset_discharge.columns[1:].tolist()
    discharge_df = df_4_reset_discharge.loc[(df_4_reset_discharge['technology'].str.strip() ==
                                             'vanadium_redox_flow_battery')]

    print("Discharge DataFrame before summing:")
    print(discharge_df.head())

    # Combine charge and discharge dataframes into one dataframe
    charge_discharge_df = charge_df.merge(discharge_df, on=['technology', 'node'], suffixes=('_charge', '_discharge'))

    print("Charge-Discharge DataFrame before summing:")
    print(charge_discharge_df.head())

    # Define columns to sum
    cols_to_sum = [col.split("_")[0] for col in charge_discharge_df.columns if col.endswith('_charge')]

    # Sum the corresponding charge and discharge values for each node and each time step
    for col in cols_to_sum:
        charge_discharge_df[col] = charge_discharge_df[col + '_charge'] + charge_discharge_df[col + '_discharge']

    # Drop the intermediate charge and discharge columns
    charge_discharge_df.drop(
        columns=[col + '_charge' for col in cols_to_sum] + [col + '_discharge' for col in cols_to_sum], inplace=True)

    print("Charge-Discharge DataFrame after summing:")
    print(charge_discharge_df.head())

    # Reset indexes and set the first column as 'technology'
    df_1_reset_power = df_1.reset_index()
    df_1_reset_power.columns = ['technology'] + df_1_reset_power.columns[1:].tolist()

    # Filter the DataFrame to get only vanadium_redox_flow_battery power values
    filtered_df = df_1_reset_power.loc[(df_1_reset_power['technology'].str.strip() == 'vanadium_redox_flow_battery') &
                                       (df_1_reset_power['capacity_type'] == 'power')]

    # Create a new DataFrame in the desired format
    existing_capacity_df = pd.DataFrame({
        'node': filtered_df['location'],
        'year_construction': years_of_operation_corrected,
        'capacity_existing': filtered_df['none']
    })

    # Save the new DataFrame as a CSV file inside the vanadium_redox_flow_battery folder
    existing_capacity_path = "C:\\GitHub\\ZEN-garden\\data\\looping_test_folder\\set_technologies\\set_storage_technologies\\vanadium_redox_flow_battery"
    fn_exp = 'capacity_existing.csv'
    existing_capacity_path = os.path.join(existing_capacity_path,fn_exp)
    existing_capacity_df.to_csv(existing_capacity_path, index=False, mode='w')

    # Reset indexes and set the first column as 'technology'
    df_1_reset_capacity = df_1.reset_index()
    df_1_reset_capacity.columns = ['technology'] + df_1_reset_capacity.columns[1:].tolist()

    # Filter the DataFrame to get only vanadium_redox_flow_battery power values
    filtered_df = df_1_reset_capacity.loc[(df_1_reset_capacity['technology'].str.strip() == 'vanadium_redox_flow_battery') &
                                 (df_1_reset_capacity['capacity_type'] == 'energy')]
    # Create a new DataFrame in the desired format
    existing_capacity_df = pd.DataFrame({
        'node': filtered_df['location'],
        'year_construction': years_of_operation_corrected,
        'capacity_existing_energy': filtered_df['none']
    })

    # Save the new DataFrame as a CSV file inside the vanadium_redox_flow_battery folder
    existing_capacity_path = "C:\\GitHub\\ZEN-garden\\data\\looping_test_folder\\set_technologies\\set_storage_technologies\\vanadium_redox_flow_battery"
    fn_exp = 'capacity_existing_energy.csv'
    existing_capacity_path = os.path.join(existing_capacity_path,fn_exp)
    existing_capacity_df.to_csv(existing_capacity_path, index=False, mode='w')

    #Move the result folder to make space for the next Run
    destination_path = "C:\\GitHub\\ZEN-garden\\looper\\storage_test_folder"
    destination_path = os.path.join(destination_path, f"Run {i}")
    # Create a new folder for each run
    os.makedirs(destination_path, exist_ok=True)
    shutil.move(results_path, destination_path)

#################################################### Running ZEN-garden and outputting results ####################################################

print(f"External loop ran for {len(years_of_operation)} successful iterations")