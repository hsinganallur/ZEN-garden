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

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(positions, labels, rotation=45, ha='right')  # Rotate labels and adjust alignment
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

    plt.legend(legend_patches, legend_labels, loc='center', ncol=1, frameon=False)
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
# Warm colors
colors = ['#FF5733', '#FF8D1A', '#FFC300', '#FF5733', '#FF8D1A', '#FFC300', '#FF5733']
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
legend_file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\legend.png'
create_legend_image(legend_file_path, color_map)

"""import matplotlib.pyplot as plt
import numpy as np


def create_min_max_plot(data, labels, ylabel, title, file_path):
    plt.figure(figsize=(10, 6))

    # Calculate min and max for each dataset
    min_values = [min(d) for d in data]
    max_values = [max(d) for d in data]

    # Calculate positions for the labels
    positions = np.arange(len(labels)) + 1

    # Plot min and max values as bars
    for pos, min_val, max_val, color in zip(positions, min_values, max_values, colors):
        plt.bar(pos, max_val - min_val, bottom=min_val, color=color, edgecolor='black')

    # Add legend with adjusted position outside the plot area
    legend_patches = [plt.Line2D([0], [0], color=color, lw=2) for color in colors]
    plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(positions, labels, rotation=45, ha='right')  # Rotate labels and adjust alignment
    plt.tight_layout()

    # Save plot to file
    plt.savefig(file_path)
    print(f"Plot saved at {file_path}")


# Data for different plots
data_sets = [
    (
    #capex_specific_energy (€ /kWh)
     [289.8614206, 289.8614206, 289.8614206, 289.8614206, 289.8614206],  # Battery
     [12.76487395, 12.76487395, 12.76487395, 12.76487395, 12.76487395],  # Hydrogen Storage
     [75.88346816, 75.88346816, 75.88346816, 75.88346816, 75.88346816],  # Pumped Hydro
     [310.55, 986.8242857],  # VRFB References
     [648.6874],  # Vanadium Redox Flow Battery
     [27537.73956, 11152.62214, 2293.374308, 157.4],  # UP Membraneless RFB
     [500.00, 370.00, 250.00, 210.00, 180.00]  # UP Devices
     ),

    #opex_specific_fixed_energy (€/kWh)
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [9.34, 9.34, 9.34, 9.34],
     # VRFB References
     [9.34, 9.34, 9.34, 9.34], [0, 0, 0, 9.34, 9.34, 9.34], [9.34, 9.34, 9.34, 9.34, 9.34]  # UP Devices
     ),

    #capex_specific (€/kW)
    ([280.3475604, 280.3475604, 280.3475604, 280.3475604, 280.3475604],  # Battery
     [2957.121575, 2957.121575, 2957.121575, 2957.121575, 2957.121575],  # Hydrogen Storage
     [280.3475604, 280.3475604, 280.3475604, 280.3475604, 280.3475604],  # Pumped Hydro
     [721.4, 1739.2],  # VRFB References
     [1137.45],  # Vanadium Redox Flow Battery
     [800, 4000, 8000, 200, 800],  # UP Membraneless RFB
     [4000.00, 200.00, 3155.56, 800.00, 1898.15]  # UP Devices
     ),

     #self_discharge (%)
    ([10, 10, 10, 10, 10] # Battery ,
      [0, 0, 0, 0, 0] # Hydrogen Storage,
      [0, 0, 0, 0, 0] # Pumped Hydro,
      [0, 0.2, 0.2],  # VRFB References
     [0.2, 0.2, 0.2, 0.2, 0.2] # Vanadium Redox Flow Battery,
     [ 0, 0, 0.2, 0.2] # UP Membraneless RFB,
     [0, 0.2, 0.2, 0.2, 0]  # UP Devices
     ),

    #efficiency_discharge (%)
    ([92.736185, 92.736185, 92.736185, 92.736185, 92.736185],  # Battery
     [63.2455532, 63.2455532, 63.2455532, 63.2455532, 63.2455532],  # Hydrogen Storage
     [88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784],  # Pumped Hydro
     [70, 78.3, 85, 80, 70],  # VRFB References
     [77.5],  # Vanadium Redox Flow Battery
     [80, 80, 80, 80, 80, 85, 85, 85, 85, 85.00, 70.00, 76.67, 85.00, 81.67, 70],  # UP Membraneless RFB
     [85.00, 70.00, 76.67, 85.00, 81.67]  # UP Devices
     ),

    #efficiency_charge (%)
    ([92.736185, 92.736185, 92.736185, 92.736185, 92.736185],  # Battery
     [63.2455532, 63.2455532, 63.2455532, 63.2455532, 63.2455532],  # Hydrogen Storage
     [88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784],  # Pumped Hydro
     [70, 85, 80, 70],  # VRFB References
     [77.5],  # Vanadium Redox Flow Battery
     [80, 80, 80, 80, 80, 85, 85, 85, 85,85.00,70.00, 76.67,85.00,81.67, 70],  # UP Membraneless RFB
     [85.00, 70.00, 76.67, 85.00, 81.67]  # UP Devices
     ),

    #opex_specific_fixed (€/kW)
    ([2.471110756, 2.471110756, 2.471110756, 2.471110756, 2.471110756],  # Battery
     [56.32675703, 56.32675703, 56.32675703, 56.32675703, 56.32675703],  # Hydrogen Storage
     [7.588346816, 7.588346816, 7.588346816, 7.588346816, 7.588346816],  # Pumped Hydro
     [6.39, 10.95, 14.6, 63.86, 5.47, 0],  # VRFB References
     [0, 0, 0, 0, 0],  # Vanadium Redox Flow Battery
     [0, 0, 0, 0, 0, 17.2, 0.86, 13.568908, 3.44, 8.162045],  # UP Membraneless RFB
     [17.2, 0.86, 13.568908, 3.44, 8.162045, 0]  # UP Devices
     ),

    #opex_specific_variable_energy (€/kWh)
    ([0, 0, 0, 0, 0], # Battery
     [0, 0, 0, 0, 0], # Hydrogen Storage
     [0, 0, 0, 0, 0], # Pumped Hydro
     [0.92],  # VRFB References
     [0.92], # Vanadium Redox Flow Battery
     [0.92], # UP Membraneless RFB
     [0.92, 0.92, 0.92, 0.92, 0.92] # UP Devices
     ),

    # lifetimes (year)
    ([13, 13, 13, 13, 13], # Battery
     [100, 100, 100, 100, 100], # Hydrogen Storage
     [60, 60, 60, 60, 60],  # Pumped Hydro
     [15, 20, 20, 25, 10], # VRFB References
     [20, 20, 20, 20, 20], # Vanadium Redox Flow Battery
     [20, 25, 25, 20, 20], # UP Membraneless RFB
     [20, 25, 25, 20, 20]  # UP Devices
     ),
]

# Labels for the plots
labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'VRFB References',
          'Vanadium RFB', 'UP Membraneless RFB Current Range', 'UP Devices']

# Common parameters for all plots
colors = plt.get_cmap('tab10').colors
ylabel = ['capex_specific_energy (€ /kWh)', 'opex_specific_energy (€/kWh)', 'capex_specific (€/kW)',
          'self_discharge (%)', 'efficiency_discharge (%)', 'efficiency_charge (%)',
          'opex_specific_fixed (€/kW)', 'opex_specific_variable_energy (€/kWh)', 'Lifetime (Years)']

file_prefix = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\min_max_plot_energy_storage_'

# Generate and save plots
for i, (data, y_label) in enumerate(zip(data_sets, ylabel)):
    title = f'Min-Max Plot of Energy Storage Types and {y_label}'
    file_path = f'{file_prefix}{i}.png'
    create_min_max_plot(data, labels, y_label, title, file_path)
"""