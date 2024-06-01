import matplotlib.pyplot as plt
import numpy as np


def create_min_max_plot(data, labels, ylabel, title, file_path, color_map):
    plt.figure(figsize=(10, 6))

    # Calculate min and max for each dataset
    min_values = [min(d) for d in data]
    max_values = [max(d) for d in data]

    # Calculate positions for the labels
    positions = np.arange(len(labels)) + 1

    # Plot min and max values as bars
    for pos, min_val, max_val, label in zip(positions, min_values, max_values, labels):
        color = color_map[label]
        plt.bar(pos, max_val - min_val, bottom=min_val, color=color, edgecolor='black')

    # Adjust y-axis ticks for the "Sum of costs per unit of power (€/kW)" plot
    if ylabel == 'Sum of costs per unit of power (€/kW)':
        max_y_value = max(max_values)
        y_ticks = np.arange(0, max_y_value + max_y_value * 0.1, max_y_value / 10)  # Add more ticks
        plt.yticks(y_ticks)

    if ylabel == 'Sum of costs per unit of energy (€/kWh)':
        plt.yscale('log')

    # Adjust y-axis for the self discharge plot
    if ylabel == 'Self discharge per lifetime (% / years)':
        plt.ylim(0, max(max_values) * 1.2)  # Increase the limit to ensure visibility

    # Adjust y-axis for the efficiency per lifetime plot
    if ylabel == 'Efficiency per lifetime (% / years)':
        plt.ylim(0, 10)  # Scale y-axis to 10

    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(positions, labels, rotation=45, ha='right', fontsize=12)  # Rotate labels and adjust alignment
    plt.yticks(fontsize=12)  # Increase y-axis tick font size
    plt.tight_layout()

    # Save plot to file
    plt.savefig(file_path)
    print(f"Plot saved at {file_path}")
    plt.close()


def create_legend_image(file_path, color_map):
    # Create a new figure for the legend
    plt.figure(figsize=(10, 2))
    legend_labels = [
        'B - Battery',
        'HS - Hydrogen Storage',
        'PH - Pumped Hydro',
        'VRFB - Vanadium Redox Flow Battery',
        'VRFBD - Vanadium Redox Flow Battery Device',
        'UPMRFB - UP Membraneless Redox Flow Battery',
        'UPMRFBD - UP Membraneless Redox Flow Battery Device'
    ]
    legend_patches = [plt.Line2D([0], [0], color=color_map[label.split(' ')[0]], lw=4) for label in legend_labels]

    plt.legend(legend_patches, legend_labels, loc='center', ncol=1, frameon=False, fontsize=12)
    plt.axis('off')
    plt.savefig(file_path, bbox_inches='tight')
    print(f"Legend saved at {file_path}")
    plt.close()


# Original data
capex_specific_energy = [
    [289.8614206] * 5, [12.76487395] * 5, [75.88346816] * 5, [310.55, 986.8242857],
    [648.6874], [27537.73956, 11152.62214, 2293.374308, 157.4], [500, 370, 250, 210, 180]
]

opex_specific_fixed_energy = [
    [0] * 5, [0] * 5, [0] * 5, [9.34] * 4, [9.34] * 4, [0, 0, 0, 9.34, 9.34, 9.34], [9.34] * 5
]

capex_specific = [
    [280.3475604] * 5, [2957.121575] * 5, [280.3475604] * 5, [721.4, 1739.2],
    [1137.45], [800, 4000, 8000, 200, 800], [4000, 200, 3155.56, 800, 1898.15]
]

opex_specific_fixed = [
    [2.471110756] * 5, [56.32675703] * 5, [7.588346816] * 5, [6.39, 10.95, 14.6, 63.86, 5.47, 0],
    [0] * 5, [0, 0, 0, 0, 0, 17.2, 0.86, 13.568908, 3.44, 8.162045], [17.2, 0.86, 13.568908, 3.44, 8.162045, 0]
]

opex_specific_variable_energy = [
    [0] * 5, [0] * 5, [0] * 5, [0.92] * 5, [0.92], [0.92] * 5, [0.92] * 5
]

self_discharge = [
    [10] * 5, [0] * 5, [0] * 5, [0, 0.2, 0.2, 0.2, 0.2], [0.2] * 5, [0, 0, 0.2, 0.2, 0.2], [0, 0.2, 0.2, 0.2, 0]
]

efficiency = [
    [92.736185] * 5, [63.2455532] * 5, [88.3176086632784] * 5, [70, 85, 80, 70, 70],
    [77.5], [80] * 6 + [85] * 4 + [70, 76.67, 85, 81.67, 70], [85, 70, 76.67, 85, 81.67]
]

lifetime = [
    [13] * 5, [100] * 5, [60] * 5, [15, 20, 20, 25, 10], [20] * 5, [20, 25, 25, 20, 20], [20, 25, 25, 20, 20]
]

labels = ['B', 'HS', 'PH', 'VRFB', 'VRFBD', 'UPMRFB', 'UPMRFBD']
# Updated colors for differentiation
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
color_map = {label: color for label, color in zip(labels, colors)}


# Calculations
def calculate_sum_and_ratios():
    sum_capex_opex_fixed = []
    sum_opex_capex_var_energy = []
    efficiency_charge_div_lifetime = []
    self_discharge_div_lifetime = []

    for i in range(len(labels)):
        sum_capex_opex_fixed.append(
            [c + o for c, o in zip(capex_specific[i], opex_specific_fixed[i])]
        )
        sum_opex_capex_var_energy.append(
            [o + c + v for o, c, v in
             zip(opex_specific_fixed_energy[i], capex_specific_energy[i], opex_specific_variable_energy[i])]
        )
        efficiency_charge_div_lifetime.append(
            [e / l for e, l in zip(efficiency[i], lifetime[i])]
        )
        self_discharge_div_lifetime.append(
            [s / l for s, l in zip(self_discharge[i], lifetime[i])]
        )

    return sum_capex_opex_fixed, sum_opex_capex_var_energy, efficiency_charge_div_lifetime, self_discharge_div_lifetime


sum_capex_opex_fixed, sum_opex_capex_var_energy, efficiency_charge_div_lifetime, self_discharge_div_lifetime = calculate_sum_and_ratios()

# Common parameters for all plots
file_prefix = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\min_max_plot_energy_storage_'
new_ylabels = [
    'Sum of costs per unit of power (€/kW)',
    'Sum of costs per unit of energy (€/kWh)',
    'Efficiency per lifetime (% / years)',
    'Self discharge per lifetime (% / years)'
]

new_data_sets = [sum_capex_opex_fixed, sum_opex_capex_var_energy, efficiency_charge_div_lifetime,
                 self_discharge_div_lifetime]

# Generate and save plots
for i, (data, y_label) in enumerate(zip(new_data_sets, new_ylabels)):
    title = f'{y_label}'
    file_path = f'{file_prefix}{i + 1}.png'
    create_min_max_plot(data, labels, y_label, title, file_path, color_map)

# Generate and save legend
legend_file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\legend1.png'
create_legend_image(legend_file_path, color_map)


"""# Define your data
data = {
    "Type": ["Battery", "Hydrogen Storage", "Pumped Hydro", "VRFB", "UPMRFB Device 1", "UPMRFB Device 2", "UPMRFB Device 3", "UPMRFB Device 4", "UPMRFB Device 5"],
    "E/P Ratio (h)": [1.00, 4.00, 24.00, 10.00, 2.8, 3.92, 7.93, 11.20, 16.8],
    "Lifetime (years)": [13.00, 100.00, 60.00, 20.00, 20.00, 25.00, 25.00, 20.00, 20.00],
    "Efficiency (%)": [92.74, 63.25, 88.32, 77.50, 85.00, 70.00, 76.67, 85.00, 81.67],
    "Self Discharge (%)": [10.00, 0.00, 0.00, 0.20, 0.00, 0.00, 0.20, 0.00, 0.20],
    "Costs per kW (€/kW)": [282.82, 3013.45, 287.94, 1142.64, 1406.31, 1456.94, 1992.49, 2362.86, 3037.96],
    "Costs per kWh (€/kWh)": [289.86, 12.76, 75.88, 658.95, 510.26, 380.26, 260.26, 220.26, 190.26]
}
"""
"""import os
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from your data
data = {
    "Type": ["Device 1", "Device 2", "Device 3", "Device 4", "Device 5"],
    "Energy (kWh)": [140.00, 1960.00, 2380.00, 560.00, 2520.0],
    "Power (kW)": [50.00, 500.00, 300.00, 50.00, 150.00],
    "E/P Ratio (h)": [2.80, 3.92, 7.93, 11.20, 16.80],
    "lifetime (years)": [20.00, 25.00, 25.00, 20.00, 20.00],
    "opex_specific_variable (€/kW)": [0.29, 0.30, 0.63, 0.74, 0.95],
    "opex_specific_variable_energy (€/kWh)": [0.92, 0.92, 0.92, 0.92, 0.92],
    "opex_specific_fixed (€/kW)": [6.02, 6.24, 8.53, 10.11, 13.00],
    "efficiency_charge (%)": [85.00, 70.00, 76.67, 85.00, 81.67],
    "efficiency_discharge (%)": [85.00, 70.00, 76.67, 85.00, 81.67],
    "self_discharge (%)": [0.00, 0.00, 0.20, 0.00, 0.20],
    "capex_specific (€/kW)": [1400.00, 1450.40, 1983.33, 2352.00, 3024.00],
    "opex_specific_fixed_energy (€/kWh)": [9.34, 9.34, 9.34, 9.34, 9.34],
    "capex_specific_energy (€ /kWh)": [500.00, 370.00, 250.00, 210.00, 180.00]
}

df = pd.DataFrame(data)

# Define the columns for the X and Y axes
x_col = "E/P Ratio (h)"
y_cols = [
    "lifetime (years)",
    "opex_specific_variable (€/kW)",
    "opex_specific_variable_energy (€/kWh)",
    "opex_specific_fixed (€/kW)",
    "efficiency_charge (%)",
    "efficiency_discharge (%)",
    "self_discharge (%)",
    "capex_specific (€/kW)",
    "opex_specific_fixed_energy (€/kWh)",
    "capex_specific_energy (€ /kWh)"
]

# Create a directory to save the plots if it doesn't exist
save_dir = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results"
os.makedirs(save_dir, exist_ok=True)

# Plot each Y column against the X column and save the plots
for i, y_col in enumerate(y_cols):
    plt.figure()
    plt.plot(df[x_col], df[y_col], marker='o')
    plt.title(f"{y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.savefig(os.path.join(save_dir, f"{i+1}.png"))
    plt.close()
"""