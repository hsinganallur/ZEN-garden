import os
import pandas as pd
import matplotlib.pyplot as plt

import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_stacked_bar_plots(data, num_years, file_name, save_path, ylabel, title, unit, scenario_info, y_axis_limit=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = None
    for tech in data.columns:
        if bottom is None:
            ax.bar(data.index, data[tech], label=f"{tech} ({data[tech].sum():.0f} {unit})", alpha=0.7)
            bottom = data[tech]
        else:
            ax.bar(data.index, data[tech], bottom=bottom, label=f"{tech} ({data[tech].sum():.0f} {unit})", alpha=0.7)
            bottom += data[tech]

    ax.set_xlabel('Year')
    ax.set_ylabel(ylabel)
    ax.set_title(f"{title} - {scenario_info}")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xticks(range(1, num_years + 1))
    ax.tick_params(axis='x', rotation=0)

    if y_axis_limit is not None:
        ax.set_ylim(y_axis_limit)

    plt.tight_layout()
    plt.savefig(f"{save_path}/{file_name}.png", dpi=300, bbox_inches='tight')
    plt.close()

def generate_power_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000

        power_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_power_data = pd.DataFrame(index=range(1, num_years + 1), columns=power_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in power_data.items():
                stacked_power_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_power_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000

        power_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_power_data = pd.DataFrame(index=range(1, num_years + 1), columns=power_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in power_data.items():
                stacked_power_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_power_data, num_years, f"stacked_power_{file_name}", save_path,
                                   'Installed Power(GW)', 'Installed Power Over Technologies', 'GW', scenario_info, y_axis_limit)

def generate_energy_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000000

        energy_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=energy_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in energy_data.items():
                stacked_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_energy_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3
        #data.iloc[:, 3:] *= 1000000

        energy_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=energy_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in energy_data.items():
                stacked_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_energy_data, num_years, f"stacked_energy_{file_name}", save_path,
                                   'Installed Energy(GWh)', 'Installed Energy Over Technologies', 'GWh', scenario_info, y_axis_limit)

def generate_specific_tech_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3

        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_specific_tech_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_tech_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_specific_tech_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3

        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]

        stacked_specific_tech_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_tech_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_specific_tech_data, num_years, f"stacked_specific_tech_{file_name}", save_path,
                                   'Installed Power(GW)', 'Installed Power for Specific Technologies', 'GW', scenario_info, y_axis_limit)


def generate_specific_energy_plots(file_paths, save_paths, scenarios):
    all_data = []
    for file_path, scenario_info in zip(file_paths, scenarios):
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3


        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_specific_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        all_data.extend(stacked_specific_energy_data.values.flatten().tolist())

    y_axis_limit = (min(all_data), 1.5*max(all_data))  # Calculate the y-axis limit across all data

    for file_path, save_path, scenario_info in zip(file_paths, save_paths, scenarios):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        data = pd.read_csv(file_path)
        num_years = len(data.columns) - 3

        specific_techs = ["battery", "hydrogen_storage", "pumped_hydro", "vanadium_redox_flow_battery"]
        available_techs = [tech for tech in specific_techs if tech in data['technology'].unique()]

        if not available_techs:
            print(f"No data available for the specified technologies in {file_name}. Skipping...")
            continue

        specific_tech_data = {}
        for tech in available_techs:
            tech_data = data[data['technology'] == tech]
            specific_tech_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        stacked_specific_energy_data = pd.DataFrame(index=range(1, num_years + 1), columns=specific_tech_data.keys(), dtype=float)
        for year in range(1, num_years + 1):
            for tech, tech_data in specific_tech_data.items():
                stacked_specific_energy_data.loc[year, tech] = tech_data.iloc[:, year + 2].sum()

        generate_stacked_bar_plots(stacked_specific_energy_data, num_years, f"stacked_specific_energy_{file_name}", save_path,
                                   'Installed Energy(GWh)', 'Installed Energy for Specific Technologies', 'GWh', scenario_info, y_axis_limit)


file_paths = [
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_No_VRFB_Imports_0_capacity_total.csv",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_No_VRFB_Imports_capacity_total.csv",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_VRFB_Imports_0_capacity_total.csv",
    #"C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14\\PI_VRFB_Imports_capacity_total.csv"
    ]

save_paths = [
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14",
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14",
    #"C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_14"
    ]

scenarios = [
    "PI folder without VRFBs and Imports",
    "PI folder without VRFBs and Imports permitted",
    "PI folder with VRFBs No Imports",
    #"PI folder with VRFBs and Imports permitted"
    ]

generate_power_plots(file_paths, save_paths, scenarios)
generate_energy_plots(file_paths, save_paths, scenarios)
generate_specific_tech_plots(file_paths, save_paths, scenarios)
generate_specific_energy_plots(file_paths, save_paths, scenarios)
