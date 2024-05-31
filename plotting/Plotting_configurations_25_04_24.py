import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies=None, log_scale=False):
    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        data = pd.read_csv(file_path)
        num_ts = len(data.columns) - 2
        data.iloc[:, 2:] /= 1000

        # Adjust column indices
        new_indices = np.linspace(0, 12, num=num_ts)
        data.columns = data.columns[:2].tolist() + new_indices.tolist()

        if selected_technologies:
            data = data[data['technology'].isin(selected_technologies)]

        if data.empty:
            print(f"No data available for the specified technologies in {file_path}. Skipping...")
            continue

        storage_level_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            storage_level_data[tech] = tech_data.iloc[:, 2:].sum(axis=0)  # Sum capacity across countries

        plt.figure(figsize=(10, 6))
        for tech, tech_data in storage_level_data.items():
            plt.plot(new_indices, tech_data, label=tech)

        plt.xlabel('Time Steps (Months)')
        plt.ylabel('Storage Level (TWh)')
        plt.title('Storage Level Over Time for Different Technologies' + f" ({scenario_info})")
        plt.grid(True)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        if log_scale:
            plt.yscale('log')  # Set Y-axis to log scale
            plt.savefig(os.path.join(save_path, f"stacked_storage_level_{scenario_info}_log.png"), bbox_inches='tight')
        else:
            plt.savefig(os.path.join(save_path, f"stacked_storage_level_{scenario_info}_linear.png"), bbox_inches='tight')

file_paths = [
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08\\PI_VRFB_Imports_storage_level_fullts.csv",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09\\PI_VRFB_Imports_storage_level_fullts.csv",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10\\PI_VRFB_Imports_storage_level_fullts.csv",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_No_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_No_VRFB_Imports_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_VRFB_Imports_0_storage_level_fullts.csv",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11\\PI_VRFB_Imports_storage_level_fullts.csv"
]

save_paths = [
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_08_Plots",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_09_Plots",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_10_Plots",

    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots",
    "C:\\GitHub\\ZEN-garden\\looper\\plot_tests\\T_11_Plots"
]

scenarios = [
    "PI folder without VRFBs and No Imports",
    "PI folder without VRFBs and Imports",
    "PI folder with VRFBs and No Imports",
    "PI folder with VRFBs and Imports"
]

# List of selected technologies (None if you want to plot all)
selected_technologies = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]

# Generate plot with linear scale
generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies, log_scale=False)

# Generate plot with log scale
generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies, log_scale=True)
