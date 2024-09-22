import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Define a consistent color mapping for the technologies across plots
color_mapping = {
    'Lithium Ion Battery': 'dodgerblue',
    'Hydrogen Storage': 'forestgreen',
    'UP Devices': 'tomato',
    'Pumped Hydro Storage': 'orange'
}

# Function to read the data, interpolate and return common discharge times and energy values
def get_data_for_percentage(data, percentage):
    data_percent = data[data['Percentage_of_total_costs_(%)'] == percentage]

    discharge_times = data_percent[['Discharge_Time_Battery (h)', 'Discharge_Time_Hydrogen_Storage(h)',
                                    'Discharge_Time_UP_Devices(h)', 'Discharge_Time_pumped_hydro_storage(h)']].values

    battery_energy = data_percent['battery_power(TW)'].values
    hydrogen_energy = data_percent['hydrogen_storage_power(TW)'].values
    up_devices_energy = data_percent['up_devices_power(TW)'].values
    pumped_hydro_energy = data_percent['pumped_hydro_storage_power(TW)'].values

    common_discharge_times = np.linspace(discharge_times.min(), discharge_times.max(), 100)

    battery_energy_interp = np.interp(common_discharge_times, discharge_times[:, 0], battery_energy)
    hydrogen_energy_interp = np.interp(common_discharge_times, discharge_times[:, 1], hydrogen_energy)
    up_devices_energy_interp = np.interp(common_discharge_times, discharge_times[:, 2], up_devices_energy)
    pumped_hydro_energy_interp = np.interp(common_discharge_times, discharge_times[:, 3], pumped_hydro_energy)

    # Filter out technologies that have zero energy values
    included_labels = []
    included_energies = []

    if battery_energy_interp.max() > 0:
        included_energies.append(battery_energy_interp)
        included_labels.append('Lithium Ion Battery')

    if hydrogen_energy_interp.max() > 0:
        included_energies.append(hydrogen_energy_interp)
        included_labels.append('Hydrogen Storage')

    if up_devices_energy_interp.max() > 0:
        included_energies.append(up_devices_energy_interp)
        included_labels.append('UP Devices')

    if pumped_hydro_energy_interp.max() > 0:
        included_energies.append(pumped_hydro_energy_interp)
        included_labels.append('Pumped Hydro Storage')

    return common_discharge_times, included_energies, included_labels


# Function to plot and save images
def plot_and_save_image(common_discharge_times, included_energies, included_labels, percentage, folder_path):
    plt.figure(figsize=(10, 6))

    # Assign consistent colors based on the included labels
    colors = [color_mapping[label] for label in included_labels]

    plt.stackplot(common_discharge_times, *included_energies, labels=included_labels, colors=colors)

    # Customize the plot
    plt.xlabel('Discharge Time (hours)', fontsize=15, fontweight='bold')
    plt.ylabel('Power (TW)', fontsize=15, fontweight='bold')
    plt.ylim(0, 3)

    # Set the x-axis limits and labels from 10 to 150 with steps of 10 (same as the energy code)
    plt.xticks(ticks=[0, 12, 50, 150], labels=['0', '12', '50', '150'], fontsize=15, fontweight='bold')
    plt.yticks(fontsize=15, fontweight='bold')

    # Ensure the x-axis starts from the minimum discharge time value
    plt.xlim(left=common_discharge_times.min())

    # Save the plot as an image in the same folder as the Excel file
    plot_file_path = os.path.join(folder_path, f'power_plot_{percentage}.png')
    plt.tight_layout()
    plt.savefig(plot_file_path)
    plt.close()


# Function to save the interpolated data to Excel
def save_data_to_excel(common_discharge_times, included_energies, included_labels, percentage, folder_path):
    df = pd.DataFrame({'Discharge Time (h)': common_discharge_times})
    for label, energy in zip(included_labels, included_energies):
        df[label + ' (TW)'] = energy
    data_file_path = os.path.join(folder_path, f'power_data_{percentage}.xlsx')
    df.to_excel(data_file_path, index=False)


# Main code
def main():
    # File path to your Excel file
    file_path = "C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Simulations\\00_Extreme_Optimistic\\Results\\Power_TW_Upload.xlsx"  # Replace with your actual file path
    folder_path = os.path.dirname(file_path)  # Extract folder path where the file is located

    # Read the Excel file
    data = pd.read_excel(file_path, sheet_name='Tabelle1')

    # List of percentages
    percentages = [100, 50]

    # Process and save for each percentage
    for percentage in percentages:
        common_discharge_times, included_energies, included_labels = get_data_for_percentage(data, percentage)

        # Save the plot as an image in the file directory
        plot_and_save_image(common_discharge_times, included_energies, included_labels, percentage, folder_path)

        # Save the interpolated data as Excel in the file directory
        save_data_to_excel(common_discharge_times, included_energies, included_labels, percentage, folder_path)


# Run the main function
if __name__ == "__main__":
    main()
