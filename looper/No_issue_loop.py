import subprocess
from zen_garden.postprocess.results import Results
def run_zen_garden(config_file="./config.py", dataset=None, job_index=None):
    # Construct the command to run the ZEN-Garden module
    command = ["python", "-m", "zen_garden", "--config", config_file]

    if dataset:
        command.extend(["--dataset", dataset])

    if job_index:
        command.extend(["--job_index", job_index])

    # Run the ZEN-Garden module
    subprocess.run(command)


def analyze_results(results_folder):
    # Analyze the results using the Results class
    print("Before Results")
    results = Results(results_folder)
    print("After Results")
    return results

    #Example: Get the dataframe for a specific component
    #component_name = "capacity"
    #dataframe = results.get_df(component_name)


if __name__ == "__main__":
    # Specify the configuration file, dataset, and job index if needed
    config_file = "C:\GitHub\ZEN-garden\data\config.py"
    dataset_path = "C:\GitHub\ZEN-garden\data\looping_test_folder"
    #job_index = "your_job_index"

    # Run ZEN-Garden module
    run_zen_garden(config_file, dataset_path)

    # Analyze results
    results_folder = "C:\GitHub\ZEN-garden\data\outputs\looping_test_folder"
    analyze_results(results_folder)
