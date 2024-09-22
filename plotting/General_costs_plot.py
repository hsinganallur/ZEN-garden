import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded file to check its contents
file_path = 'C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\Upload.xlsx'
uploaded_data = pd.read_excel(file_path)

# Extract the relevant columns from the uploaded data
df_uploaded = uploaded_data.copy()

# Create an array for years between 2025 and 2050 for interpolation
years_uploaded = np.arange(2025, 2051)

# Interpolate data for capex_specific and capex_specific_energy from the uploaded data
capex_specific_uploaded = {}
capex_specific_energy_uploaded = {}

for i, row in df_uploaded.iterrows():
    capex_specific_uploaded[row['Type']] = np.linspace(row['capex_specific_2025 (€/kW)'], row['capex_specific_2050 (€/kW)'], len(years_uploaded))
    capex_specific_energy_uploaded[row['Type']] = np.linspace(row['capex_specific_energy_2050 (€ /kWh)'], row['capex_specific_energy_2050 (€ /kWh).1'], len(years_uploaded))

# Plot capex_specific from the uploaded data with markers
plt.figure(figsize=(10, 6))
plt.plot(years_uploaded, capex_specific_uploaded["LiB"], label="Lithium Ion Battery", color='dodgerblue', marker='o')
plt.plot(years_uploaded, capex_specific_uploaded["Hydrogen"], label="Hydrogen Storage", color='forestgreen', marker='s')
plt.plot(years_uploaded, capex_specific_uploaded["Pumped Hydro"], label="Pumped Hydro Storage", color='orange', marker='^')
plt.plot(years_uploaded, capex_specific_uploaded["UPMRFB Minimum"], label="UP Devices Minimum", color='tomato', linestyle='--', marker='v')
plt.plot(years_uploaded, capex_specific_uploaded["UPMRFB Maximum"], label="UP Devices Maximum", color='tomato', linestyle='-', marker='x')

#plt.title('Capex Specific Interpolation (2025-2050)',  fontsize=15, fontweight='bold')
plt.xlabel('Year', fontsize=15, fontweight='bold')
plt.ylabel('Capex Specific (€ / kW)',  fontsize=15, fontweight='bold')
plt.xticks( fontsize=15, fontweight='bold')
plt.yticks( fontsize=15, fontweight='bold')
plt.ylim(0,3001)
#plt.legend()
plt.grid(False)

# Plot capex_specific_energy from the uploaded data with markers
plt.figure(figsize=(10, 6))
plt.plot(years_uploaded, capex_specific_energy_uploaded["LiB"], label="Lithium Ion Battery", color='dodgerblue', marker='o')
plt.plot(years_uploaded, capex_specific_energy_uploaded["Hydrogen"], label="Hydrogen Storage", color='forestgreen', marker='s')
plt.plot(years_uploaded, capex_specific_energy_uploaded["Pumped Hydro"], label="Pumped Hydro Storage", color='orange', marker='^')
plt.plot(years_uploaded, capex_specific_energy_uploaded["UPMRFB Minimum"], label="UP Devices Minimum", color='tomato', linestyle='--', marker='v')
plt.plot(years_uploaded, capex_specific_energy_uploaded["UPMRFB Maximum"], label="UP Devices Maximum", color='tomato', linestyle='-', marker='x')

#plt.title('Capex Specific Energy Interpolation (2025-2050)',  fontsize=15, fontweight='bold')
plt.xlabel('Year',  fontsize=15, fontweight='bold')
plt.ylabel('Capex Specific Energy (€ / kWh)',  fontsize=15, fontweight='bold')
plt.xticks( fontsize=15, fontweight='bold')
plt.yticks( fontsize=15, fontweight='bold')
#plt.legend()
plt.grid(False)
plt.ylim(0,501)
plt.show()