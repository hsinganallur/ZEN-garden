import os
import shutil
import json

def find_newest_folder(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    newest_folder = max(folders, key=lambda f: os.path.getctime(os.path.join(path, f)))
    return os.path.join(path, newest_folder)

def copy_subfolders(src, dest):
    for folder in os.listdir(src):
        folder_path = os.path.join(src, folder)
        if os.path.isdir(folder_path):
            shutil.copytree(folder_path, os.path.join(dest, folder))

def update_capex_specific_storage_energy(attributes_path, factor):
    with open(attributes_path, 'r') as file:
        attributes = json.load(file)

    # Update the value based on the factor
    attributes["capex_specific_storage_energy"]["default_value"] *= factor

    with open(attributes_path, 'w') as file:
        json.dump(attributes, file, indent=2)

if __name__ == "__main__":
    outputs_path = r"C:\GitHub\ZEN-garden\data\outputs"
    data_path = r"C:\GitHub\ZEN-garden\data"
    looper_path = r"C:\GitHub\ZEN-garden\looper"

    newest_folder_path = find_newest_folder(outputs_path)

    # Check if a folder with the same name exists in the data_path
    matching_folder_path = os.path.join(data_path, os.path.basename(newest_folder_path))

    if os.path.exists(matching_folder_path):
        for i in range(1, 6):
            # Create destination folder if it doesn't exist
            destination_path = os.path.join(data_path, f"looped_folder_{i}")
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Copy subfolders from the matching folder to the destination
            copy_subfolders(matching_folder_path, destination_path)

            # Update capex_specific_storage_energy in each subfolder
            attributes_path = os.path.join(destination_path, "set_technologies", "set_storage_technologies",
                                           "vanadium_redox_flow_battery", "attributes.json")
            update_capex_specific_storage_energy(attributes_path, 0.2 * i)

            print(f"Subfolders copied from {matching_folder_path} to {destination_path}")

        # Copy the newest folder to looper_path
        shutil.copytree(newest_folder_path, os.path.join(looper_path, os.path.basename(newest_folder_path)))
        print(f"Newest folder copied to {looper_path}")
    else:
        print(f"No matching folder found in {data_path}")

from zen_garden.model import Config
import os

# create a config
config2 = Config()

## Analysis - Default dictionary
analysis = config2.analysis
## Solver - Default dictionary
solver = config2.solver

## Analysis - settings update compared to default values
analysis["dataset"] = os.path.join(os.path.dirname(__file__), "looping_folder_1")
analysis["objective"] = "total_cost"
# use greenfield or brownfield approach
analysis["use_capacities_existing"] = True

## Solver - settings update compared to default values
solver["name"] = "glpk" # free solver
solver["analyze_numerics"] = True
solver["immutable_unit"] = ["hour","km"]

## Solver - settings from Lukas Kunz in ZEN-disciples
solver["solver_options"]["Method"]= 2
solver["solver_options"]["NodeMethod"]= 2
solver["solver_options"]["BarHomogeneous"]= 1
solver["solver_options"]["DualReductions"] = 0
solver["solver_options"]["Threads"]=64
solver["solver_options"]["Crossover"]=0
solver["solver_options"]["ScaleFlag"]=2


