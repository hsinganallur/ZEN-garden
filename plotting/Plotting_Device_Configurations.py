import matplotlib.pyplot as plt
import numpy as np

def create_min_max_plot(data, labels, ylabel, title, file_path, color_map):
    plt.figure(figsize=(10, 6))

    # Exclude 'VRFBD' and 'UPMRFBD' from labels and data
    filtered_labels = [label for label in labels if label not in ['VRFBD', 'UPMRFBD']]
    filtered_data = [data[labels.index(label)] for label in filtered_labels]

    # Calculate min and max for each dataset
    min_values = [min(d) for d in filtered_data]
    max_values = [max(d) for d in filtered_data]

    # Calculate positions for the labels
    positions = np.arange(len(filtered_labels)) + 1

    # Plot lines for categories with single unique values
    for pos, d, label in zip(positions, filtered_data, filtered_labels):
        color = color_map[label]
        if len(set(d)) == 1:  # Check if all values are the same
            plt.plot([pos - 0.4, pos + 0.4], [d[0], d[0]], color=color, linewidth=5)
        elif label == 'UPMRFB':  # For UPMRFBD, plot each value as an individual line on the UPMRFB position
            plt.bar(pos, max(d) - min(d), bottom=min(d), color=color)
            for val in data[labels.index('UPMRFBD')]:
                plt.plot([pos - 0.4, pos + 0.4], [val, val], color=color_map['UPMRFBD'], linewidth=2, linestyle='--')
        elif label == 'VRFB':  # For VRFBD, plot each value as an individual line on the VRFB position
            plt.bar(pos, max(d) - min(d), bottom=min(d), color=color)
            for val in data[labels.index('VRFBD')]:
                plt.plot([pos - 0.4, pos + 0.4], [val, val], color=color_map['VRFBD'], linewidth=2, linestyle='--')

    # Adjust y-axis ticks for the "Sum of costs per unit of power (€/kW)" plot
    if ylabel == 'Sum of costs per unit of power (€/kW/year)':
        max_y_value = max(max_values)
        y_ticks = np.arange(0, max_y_value + max_y_value * 0.1, max_y_value / 10)  # Add more ticks
        plt.yticks(y_ticks)

    if ylabel == 'Sum of costs per unit of energy (€/kWh/year)':
        plt.yscale('log')

    # Adjust y-axis for the self discharge plot
    if ylabel == 'Self discharge (%/hour)':
        plt.ylim(0, max(max_values) * 1.2)  # Increase the limit to ensure visibility

    # Adjust y-axis for the efficiency plot
    if ylabel == 'Efficiency (%)':
        plt.ylim(0, 100)  # Scale y-axis to 100

    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(positions, filtered_labels, rotation=45, ha='right', fontsize=12)  # Rotate labels and adjust alignment
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
    [0] * 5, [0] * 5, [0] * 5, [9.34] * 4, [9.34], [0, 0, 0, 9.34, 9.34, 9.34], [9.34] * 5
]

capex_specific = [
    [280.3475604] * 5, [2957.121575] * 5, [280.3475604] * 5, [721.4, 1739.2],
    [1137.45], [800, 4000, 8000, 200, 800], [4000, 200, 3155.56, 800, 1898.15]
]

opex_specific_fixed = [
    [2.471110756] * 5, [56.32675703] * 5, [7.588346816] * 5, [6.39, 10.95, 14.6, 63.86, 5.47, 0],
    [0] , [0, 0, 0, 0, 0, 17.2, 0.86, 13.568908, 3.44, 8.162045], [17.2, 0.86, 13.568908, 3.44, 8.162045, 0]
]

opex_specific_variable_energy = [
    [0] * 5, [0] * 5, [0] * 5, [0.92] * 5, [0.92], [0.92] * 5, [0.92] * 5
]

self_discharge = [
    [10] * 5, [0] * 5, [0] * 5, [0, 0.2, 0.2, 0.2, 0.2], [0.2] , [0, 0, 0.2, 0.2, 0.2], [0, 0.2, 0.2, 0.2, 0]
]

efficiency = [
    [92.736185] * 5, [63.2455532] * 5, [88.3176086632784] * 5, [70, 85, 80, 70, 70],
    [77.5], [70, 76.67, 85, 81.67, 70], [85, 70, 76.67, 85, 81.67]
]

lifetime = [
    [13] * 5, [100] * 5, [60] * 5, [15, 20, 20, 25, 10], [20] , [20, 25, 25, 20, 20], [20, 25, 25, 20, 20]
]

labels = ['B', 'HS', 'PH', 'VRFB', 'VRFBD', 'UPMRFB', 'UPMRFBD']
# Updated colors for differentiation
color_map = {
    'B': '#00BFFF',
    'HS': '#FF6347',
    'PH': '#00008B',
    'VRFB': '#FFC0CB',
    'VRFBD': '#d62728',
    'UPMRFB': '#FFD700',
    'UPMRFBD': '#9467bd'
}

# Calculations
def calculate_sum_and_ratios():
    sum_capex_opex_fixed = []
    sum_opex_capex_var_energy = []

    for i in range(len(labels)):
        sum_capex_opex_fixed.append(
            [c + o for c, o in zip(capex_specific[i], opex_specific_fixed[i])]
        )
        sum_opex_capex_var_energy.append(
            [o + c + v for o, c, v in
             zip(opex_specific_fixed_energy[i], capex_specific_energy[i], opex_specific_variable_energy[i])]
        )

    return sum_capex_opex_fixed, sum_opex_capex_var_energy

def calculate_annualized_costs(sum_costs, lifetime):
    annualized_costs = []
    for i in range(len(sum_costs)):
        annualized_costs.append([cost / lt for cost, lt in zip(sum_costs[i], lifetime[i])])
    return annualized_costs

sum_capex_opex_fixed, sum_opex_capex_var_energy = calculate_sum_and_ratios()
annualized_capex_opex_fixed = calculate_annualized_costs(sum_capex_opex_fixed, lifetime)
annualized_opex_capex_var_energy = calculate_annualized_costs(sum_opex_capex_var_energy, lifetime)

# Convert 'Self discharge (%/day)' to 'Self discharge (%/hour)'
self_discharge_per_hour = [[value / 24 for value in sublist] for sublist in self_discharge]

# Common parameters for all plots
file_prefix = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\min_max_plot_energy_storage_new'
new_ylabels = [
    'Sum of costs per unit of power (€/kW/year)',
    'Sum of costs per unit of energy (€/kWh/year)',
    'Efficiency (%)',
    'Self discharge (%/hour)'  # Update ylabel to reflect hourly self-discharge
]

new_data_sets = [annualized_capex_opex_fixed, annualized_opex_capex_var_energy, efficiency, self_discharge_per_hour]

# Generate and save plots
for i, (data, y_label) in enumerate(zip(new_data_sets, new_ylabels)):
    title = f'{y_label}'
    file_path = f'{file_prefix}{i + 1}.png'
    create_min_max_plot(data, labels, y_label, title, file_path, color_map)

# Generate and save legend
legend_file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\legend1new.png'
create_legend_image(legend_file_path, color_map)

"""
import matplotlib.pyplot as plt
import numpy as np

def create_min_max_plot(data, labels, ylabel, title, file_path, color_map):
    plt.figure(figsize=(10, 6))

    # Exclude 'VRFBD' and 'UPMRFBD' from labels and data
    filtered_labels = [label for label in labels if label not in ['VRFBD', 'UPMRFBD']]
    filtered_data = [data[labels.index(label)] for label in filtered_labels]

    # Calculate min and max for each dataset
    min_values = [min(d) for d in filtered_data]
    max_values = [max(d) for d in filtered_data]

    # Calculate positions for the labels
    positions = np.arange(len(filtered_labels)) + 1

    # Plot lines for categories with single unique values
    for pos, d, label in zip(positions, filtered_data, filtered_labels):
        color = color_map[label]
        if len(set(d)) == 1:  # Check if all values are the same
            plt.plot([pos - 0.4, pos + 0.4], [d[0], d[0]], color=color, linewidth=5)
        elif label == 'UPMRFB':  # For UPMRFBD, plot each value as an individual line on the UPMRFB position
            plt.bar(pos, max(d) - min(d), bottom=min(d), color=color)
            for val in data[labels.index('UPMRFBD')]:
                plt.plot([pos - 0.4, pos + 0.4], [val, val], color=color_map['UPMRFBD'], linewidth=2, linestyle='--')
        elif label == 'VRFB':  # For VRFBD, plot each value as an individual line on the VRFB position
            plt.bar(pos, max(d) - min(d), bottom=min(d), color=color)
            for val in data[labels.index('VRFBD')]:
                plt.plot([pos - 0.4, pos + 0.4], [val, val], color=color_map['VRFBD'], linewidth=2, linestyle='--')

    # Adjust y-axis ticks for the "Sum of costs per unit of power (€/kW)" plot
    if ylabel == 'Sum of costs per unit of power (€/kW/year)':
        max_y_value = max(max_values)
        y_ticks = np.arange(0, max_y_value + max_y_value * 0.1, max_y_value / 10)  # Add more ticks
        plt.yticks(y_ticks)

    if ylabel == 'Sum of costs per unit of energy (€/kWh/year)':
        plt.yscale('log')

    # Adjust y-axis for the self discharge plot
    if ylabel == 'Self discharge (%/hour)':
        plt.yscale('log')  # Use log scale for better visibility
        plt.ylim(0.0001, max(max_values) * 1.2)  # Set lower limit to ensure visibility

    # Adjust y-axis for the efficiency plot
    if ylabel == 'Efficiency (%)':
        plt.ylim(0, 100)  # Scale y-axis to 100

    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(positions, filtered_labels, rotation=45, ha='right', fontsize=12)  # Rotate labels and adjust alignment
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
    [0] * 5, [0] * 5, [0] * 5, [9.34] * 4, [9.34], [0, 0, 0, 9.34, 9.34, 9.34], [9.34] * 5
]

capex_specific = [
    [280.3475604] * 5, [2957.121575] * 5, [280.3475604] * 5, [721.4, 1739.2],
    [1137.45], [800, 4000, 8000, 200, 800], [4000, 200, 3155.56, 800, 1898.15]
]

opex_specific_fixed = [
    [2.471110756] * 5, [56.32675703] * 5, [7.588346816] * 5, [6.39, 10.95, 14.6, 63.86, 5.47, 0],
    [0] , [0, 0, 0, 0, 0, 17.2, 0.86, 13.568908, 3.44, 8.162045], [17.2, 0.86, 13.568908, 3.44, 8.162045, 0]
]

opex_specific_variable_energy = [
    [0] * 5, [0] * 5, [0] * 5, [0.92] * 5, [0.92], [0.92] * 5, [0.92] * 5
]

self_discharge = [
    [10] * 5, [0] * 5, [0] * 5, [0, 0.2, 0.2, 0.2, 0.2], [0.2] , [0, 0, 0.2, 0.2, 0.2], [0, 0.2, 0.2, 0.2, 0]
]

efficiency = [
    [92.736185] * 5, [63.2455532] * 5, [88.3176086632784] * 5, [70, 85, 80, 70, 70],
    [77.5], [70, 76.67, 85, 81.67, 70], [85, 70, 76.67, 85, 81.67]
]

lifetime = [
    [13] * 5, [100] * 5, [60] * 5, [15, 20, 20, 25, 10], [20] , [20, 25, 25, 20, 20], [20, 25, 25, 20, 20]
]

labels = ['B', 'HS', 'PH', 'VRFB', 'VRFBD', 'UPMRFB', 'UPMRFBD']
# Updated colors for differentiation
color_map = {
    'B': '#00BFFF',
    'HS': '#FF6347',
    'PH': '#00008B',
    'VRFB': '#FFC0CB',
    'VRFBD': '#d62728',
    'UPMRFB': '#FFD700',
    'UPMRFBD': '#9467bd'
}

# Calculations
def calculate_sum_and_ratios():
    sum_capex_opex_fixed = []
    sum_opex_capex_var_energy = []

    for i in range(len(labels)):
        sum_capex_opex_fixed.append(
            [c + o for c, o in zip(capex_specific[i], opex_specific_fixed[i])]
        )
        sum_opex_capex_var_energy.append(
            [o + c + v for o, c, v in
             zip(opex_specific_fixed_energy[i], capex_specific_energy[i], opex_specific_variable_energy[i])]
        )

    return sum_capex_opex_fixed, sum_opex_capex_var_energy

def calculate_annualized_costs(sum_costs, lifetime):
    annualized_costs = []
    for i in range(len(sum_costs)):
        annualized_costs.append([cost / lt for cost, lt in zip(sum_costs[i], lifetime[i])])
    return annualized_costs

sum_capex_opex_fixed, sum_opex_capex_var_energy = calculate_sum_and_ratios()
annualized_capex_opex_fixed = calculate_annualized_costs(sum_capex_opex_fixed, lifetime)
annualized_opex_capex_var_energy = calculate_annualized_costs(sum_opex_capex_var_energy, lifetime)

# Convert 'Self discharge (%/day)' to 'Self discharge (%/hour)'
self_discharge_per_hour = [[value / 24 for value in sublist] for sublist in self_discharge]

# Common parameters for all plots
file_prefix = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\min_max_plot_energy_storage_new'
new_ylabels = [
    'Sum of costs per unit of power (€/kW/year)',
    'Sum of costs per unit of energy (€/kWh/year)',
    'Efficiency (%)',
    'Self discharge (%/hour)'  # Update ylabel to reflect hourly self-discharge
]

new_data_sets = [annualized_capex_opex_fixed, annualized_opex_capex_var_energy, efficiency, self_discharge_per_hour]

# Generate and save plots
for i, (data, y_label) in enumerate(zip(new_data_sets, new_ylabels)):
    title = f'{y_label}'
    file_path = f'{file_prefix}{i + 1}.png'
    create_min_max_plot(data, labels, y_label, title, file_path, color_map)

# Generate and save legend
legend_file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\legend1new.png'
create_legend_image(legend_file_path, color_map)

"""
