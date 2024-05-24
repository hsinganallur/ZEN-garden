import os
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
