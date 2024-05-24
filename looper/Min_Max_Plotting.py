import matplotlib.pyplot as plt
import numpy as np


def create_min_max_plot(data, labels, ylabel, title, file_path):
    plt.figure(figsize=(10, 6))

    # Calculate min and max for each dataset
    min_values = [min(d) for d in data]
    max_values = [max(d) for d in data]

    # Calculate positions for the labels
    positions = np.arange(len(labels)) + 1

    # Plot min and max values as bars or lines
    for pos, min_val, max_val, color in zip(positions, min_values, max_values, colors):
        plt.plot([pos, pos], [min_val, max_val], color=color, lw=2)
        plt.scatter([pos, pos], [min_val, max_val], color=color, zorder=5)

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
    ([289.8614206, 289.8614206, 289.8614206, 289.8614206, 289.8614206],  # Battery
     [12.76487395, 12.76487395, 12.76487395, 12.76487395, 12.76487395],  # Hydrogen Storage
     [75.88346816, 75.88346816, 75.88346816, 75.88346816, 75.88346816],  # Pumped Hydro
     [310.55, 986.8242857],  # VRFB References
     [648.6874],  # Vanadium Redox Flow Battery
     [27537.73956, 11152.62214, 2293.374308, 157.4],  # UP Membraneless RFB
     [500.00, 370.00, 250.00, 210.00, 180.00]  # UP Devices
     ),

    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [9.34, 9.34, 9.34, 9.34],
     # VRFB References
     [9.34, 9.34, 9.34, 9.34], [0, 0, 0, 9.34, 9.34, 9.34], [9.34, 9.34, 9.34, 9.34, 9.34]  # UP Devices
     ),

    ([280.3475604, 280.3475604, 280.3475604, 280.3475604, 280.3475604],  # Battery
     [2957.121575, 2957.121575, 2957.121575, 2957.121575, 2957.121575],  # Hydrogen Storage
     [280.3475604, 280.3475604, 280.3475604, 280.3475604, 280.3475604],  # Pumped Hydro
     [721.4, 1739.2],  # VRFB References
     [1137.45],  # Vanadium Redox Flow Battery
     [800, 4000, 8000, 200, 800],  # UP Membraneless RFB
     [4000.00, 200.00, 3155.56, 800.00, 1898.15]  # UP Devices
     ),

    ([10, 10, 10, 10, 10], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0.2, 0.2],  # VRFB References
     [0.2, 0.2, 0.2, 0.2, 0.2], [ 0, 0, 0.2, 0.2], [0, 0.2, 0.2, 0.2, 0]  # UP Devices
     ),

    ([92.736185, 92.736185, 92.736185, 92.736185, 92.736185],  # Battery
     [63.2455532, 63.2455532, 63.2455532, 63.2455532, 63.2455532],  # Hydrogen Storage
     [88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784],  # Pumped Hydro
     [70, 78.3, 85, 80, 70],  # VRFB References
     [77.5],  # Vanadium Redox Flow Battery
     [80, 80, 80, 80, 80, 85, 85, 85, 85, 85.00, 70.00, 76.67, 85.00, 81.67, 70],  # UP Membraneless RFB
     [85.00, 70.00, 76.67, 85.00, 81.67]  # UP Devices
     ),

    ([92.736185, 92.736185, 92.736185, 92.736185, 92.736185],  # Battery
     [63.2455532, 63.2455532, 63.2455532, 63.2455532, 63.2455532],  # Hydrogen Storage
     [88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784, 88.3176086632784],  # Pumped Hydro
     [70, 85, 80, 70],  # VRFB References
     [77.5],  # Vanadium Redox Flow Battery
     [80, 80, 80, 80, 80, 85, 85, 85, 85,85.00,70.00, 76.67,85.00,81.67, 70],  # UP Membraneless RFB
     [85.00, 70.00, 76.67, 85.00, 81.67]  # UP Devices
     ),

    # Data set 8
    ([2.471110756, 2.471110756, 2.471110756, 2.471110756, 2.471110756],  # Battery
     [56.32675703, 56.32675703, 56.32675703, 56.32675703, 56.32675703],  # Hydrogen Storage
     [7.588346816, 7.588346816, 7.588346816, 7.588346816, 7.588346816],  # Pumped Hydro
     [6.39, 10.95, 14.6, 63.86, 5.47, 0],  # VRFB References
     [0, 0, 0, 0, 0],  # Vanadium Redox Flow Battery
     [0, 0, 0, 0, 0, 17.2, 0.86, 13.568908, 3.44, 8.162045],  # UP Membraneless RFB
     [17.2, 0.86, 13.568908, 3.44, 8.162045, 0]  # UP Devices
     ),

    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [6.39, 1.73, 3.74, 4.74, 2.19, 0],  # VRFB References
     [0, 0, 0, 0, 0], [0, 0, 0, 0.84108, 0.042054, 0.99641919, 0.25261296, 0.599371613],
     [0.84108, 0.042054, 0.99641919, 0.25261296, 0.599371613]
     # UP Devices
     ),
    # Data set 9 Lifetimes
    ([13, 13, 13, 13, 13], [100, 100, 100, 100, 100], [60, 60, 60, 60, 60],  # Battery
     [15, 20, 20, 25, 10], [20, 20, 20, 20, 20], [20, 25, 25, 20, 20], [20, 25, 25, 20, 20]  # UP Devices
     ),
]

# Labels for the plots
labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'VRFB References',
          'Vanadium RFB', 'UP Membraneless RFB Current Range', 'UP Devices']

# Common parameters for all plots
colors = plt.get_cmap('tab10').colors
ylabel = ['capex_specific_energy (€ /kWh)', 'opex_specific_energy (€/kWh)', 'capex_specific (€/kW)',
          'self_discharge (%)', 'efficiency_discharge (%)', 'efficiency_charge (%)',
          'opex_specific_fixed (€/kW)', 'opex_specific_variable (€/kW)', 'Lifetime (Years)']

file_prefix = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\min_max_plot_energy_storage_'

# Generate and save plots
for i, (data, y_label) in enumerate(zip(data_sets, ylabel)):
    title = f'Min-Max Plot of Energy Storage Types and {y_label}'
    file_path = f'{file_prefix}{i}.png'
    create_min_max_plot(data, labels, y_label, title, file_path)
