import subprocess
import read_results
import pandas as pd
import os

import sys

# Add the directory containing system.py to the Python path
sys.path.append("C:\GitHub\ZEN-garden\data\looping_test_folder")

# Now you can import system from system.py
from system import system

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

    #Example: Get the dataframe for a specific component
    #component_name = "capacity"
    #dataframe = results.get_df(component_name)


if __name__ == "__main__":
    # Read parameters from system variable
    reference_year = system["reference_year"]
    optimized_years = system["optimized_years"]
    interval_between_years = system["interval_between_years"]

    # Calculate years of operation
    years_of_operation = get_years_of_operation(reference_year, optimized_years, interval_between_years)
    #print("Years of operation:", years_of_operation)

    # Specify the configuration file, dataset, and job index if needed
    config_file = "C:\GitHub\ZEN-garden\data\config.py"
    dataset_path = "C:\GitHub\ZEN-garden\data\looping_test_folder"
    #job_index = "your_job_index"

    # Run ZEN-Garden module
    run_zen_garden(config_file, dataset_path)

    # Analyze results
    results_path = "C:\GitHub\ZEN-garden\data\outputs\looping_test_folder"
    r = read_results.Results(results_path)

    cn_1 = "capacity"
    cn_2 = "storage_level"
    cn_3 = "flow_storage_charge"
    cn_4 = "flow_storage_discharge"
    #cn_5 = "tech_on_var"
    #cn_6 = "tech_off_var"
    df_1 = r.get_df(cn_1)
    df_1 = pd.DataFrame(df_1)
    df_2 = r.get_df(cn_2)
    df_2 = pd.DataFrame(df_2)
    df_3 = r.get_df(cn_3)
    df_3 = pd.DataFrame(df_3)
    df_4 = r.get_df(cn_4)
    df_4 = pd.DataFrame(df_4)
    #df_5 = r.get_df(cn_5)
    #df_5 = pd.DataFrame(df_5)
    #df_6 = pd.DataFrame(df_6)

    # Store results
    storage_path = "C:\GitHub\ZEN-garden\looper\storage_test_folder"

    # Create Run folder
    run_path = os.path.join(storage_path, f"Run {1}")

    # Create a new folder for each run
    os.makedirs(run_path, exist_ok=True)

    fn_1 = 'capacity.csv'
    fn_2 = 'storage_level.csv'
    fn_3 = 'flow_storage_charge.csv'
    fn_4 = 'flow_storage_discharge.csv'
    #fn_5 = 'tech_on_var.csv'
    #fn_6 = 'tech_off_var.csv'

    fp_1 = os.path.join(run_path, fn_1)
    fp_2 = os.path.join(run_path, fn_2)
    fp_3 = os.path.join(run_path, fn_3)
    fp_4 = os.path.join(run_path, fn_4)
    #fp_5 = os.path.join(storage_path, fn_5)
    #fp_6 = os.path.join(storage_path, fn_6)

    # Save the DataFrame as a CSV file in the specified directory
    df_1.to_csv(fp_1, index=True, mode = 'w')
    df_2.to_csv(fp_2, index=True, mode = 'w')
    df_3.to_csv(fp_3, index=True, mode = 'w')
    df_4.to_csv(fp_4, index=True, mode = 'w')
    #df_5.to_csv(fp_5, index=False)
    #df_6.tocsv(fp_6, index=False)

    # New Tests
    # Reset indexes and set the first column as 'technology'
    df_1_reset = df_1.reset_index()
    df_1_reset.columns = ['technology'] + df_1_reset.columns[1:].tolist()

    # Filter the DataFrame to get only vanadium_redox_flow_battery power values
    #filtered_df = df_1_reset.loc[df_1_reset['technology'].str.strip() == 'vanadium_redox_flow_battery']
    filtered_df = df_1_reset.loc[(df_1_reset['technology'].str.strip() == 'vanadium_redox_flow_battery') &
                                 (df_1_reset['capacity_type'] == 'power')]

    # Create a new DataFrame in the desired format
    existing_capacity_df = pd.DataFrame({
        'node': filtered_df['location'],
        'year_construction': filtered_df['year'],
        'capacity_existing': filtered_df['none']
    })

    # Save the new DataFrame as a CSV file inside the vanadium_redox_flow_battery folder
    existing_capacity_path = "C:/GitHub/ZEN-garden/data/looping_test_folder/set_technologies/set_storage_technologies/vanadium_redox_flow_battery"
    fn_exp = 'capacity_existing.csv'
    existing_capacity_path = os.path.join(existing_capacity_path,fn_exp)
    existing_capacity_df.to_csv(existing_capacity_path, index=False, mode='w')

    # New Tests
    # Reset indexes and set the first column as 'technology'
    df_1_reset = df_1.reset_index()
    df_1_reset.columns = ['technology'] + df_1_reset.columns[1:].tolist()

    # Filter the DataFrame to get only vanadium_redox_flow_battery power values
    #filtered_df = df_1_reset.loc[df_1_reset['technology'].str.strip() == 'vanadium_redox_flow_battery']
    filtered_df = df_1_reset.loc[(df_1_reset['technology'].str.strip() == 'vanadium_redox_flow_battery') &
                                 (df_1_reset['capacity_type'] == 'energy')]
    # Create a new DataFrame in the desired format
    existing_capacity_df = pd.DataFrame({
        'node': filtered_df['location'],
        'year_construction': filtered_df['year'],
        'capacity_existing': filtered_df['none']
    })

    # Save the new DataFrame as a CSV file inside the vanadium_redox_flow_battery folder
    existing_capacity_path = "C:/GitHub/ZEN-garden/data/looping_test_folder/set_technologies/set_storage_technologies/vanadium_redox_flow_battery"
    fn_exp = 'capacity_existing_energy.csv'
    existing_capacity_path = os.path.join(existing_capacity_path,fn_exp)
    existing_capacity_df.to_csv(existing_capacity_path, index=False, mode='w')
