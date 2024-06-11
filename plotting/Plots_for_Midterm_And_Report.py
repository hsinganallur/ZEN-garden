import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import numpy as np

#RES Plot
# Load the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for European countries, excluding Russia
europe = world[(world['continent'] == 'Europe') & (world['name'] != 'Russia')]

# Create a DataFrame for RES data
res_data = {
    'country': ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
                'Germany', 'Greece', 'Hungary', 'Iceland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands',
                'Norway', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
                'United Kingdom'],
    'share_of_res': [33.758, 13.759, 19.095, 29.354, 18.195, 41.601, 38.472, 47.886, 20.259, 20.796, 22.678, 15.19,
                     79.475, 19.131, 43.316, 29.599, 14.356, 14.972, 75.82, 16.879, 34.677, 24.14, 17.501, 25.002,
                     22.116, 66.002, 57.3, 39.9]
}

res_df = pd.DataFrame(res_data)

# Merge the RES data with the European map data
europe = europe.merge(res_df, left_on='name', right_on='country')

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
cmap = 'Blues'
norm = mpl.colors.Normalize(vmin=0, vmax=100)

# Plot the data with the specified colormap and normalization
europe.plot(column='share_of_res', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=False)

# Create the colorbar with custom normalization
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm._A = []  # dummy array for the ScalarMappable

# Add the colorbar to the plot
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Share of Renewable Energy Sources (%)')

# Customize the plot
ax.set_title('Map of Continental Europe with Projections for 2030', fontsize=15)
ax.set_axis_off()

# Set the limits for the zoom (bounding box coordinates)
ax.set_xlim(-10, 40)  # Adjust these values to fit the zoom level you want
ax.set_ylim(30, 83)   # Adjust these values to fit the zoom level you want

plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\RES_Map.png")

# Mckinsey Plot
# Data
years = [2025, 2030, 2035, 2040]
capacity = [2, 10, 65, 140]

# Shades of blue
colors = ['#ADD8E6', '#87CEEB', '#4682B4', '#0000FF']

# Plotting the bar graph
plt.figure(figsize=(10, 6))
bars = plt.bar(years, capacity, color=colors, width=3)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Cumulative LDES Installed Energy Capacity (TWh)')
plt.title('Predicted Cumulative LDES Installed Energy Capacity Over Time')

# Setting x-axis to display only specified years
plt.xticks(years)

# Setting y-axis limit
plt.ylim(0, 160)

# Displaying the values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval} TWh',
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Save the plot
plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Mckinsey_plot.png")

#Generate Energy Supply Demand Profile

# Time values
time = np.linspace(0, 24, 1000)

# Simulating energy demand and supply curves
demand = 50 + 20 * np.sin(2 * np.pi * time / 24)  # Simulated demand curve
supply = 40 + 10 * np.sin(2 * np.pi * (time / 24 + 0.5))  # Simulated supply curve shifted

# Plotting
plt.figure(figsize=(10, 6))

# Plot demand and supply
plt.plot(time, demand, label='Demand', color='brown', linewidth=2)
plt.plot(time, supply, label='Supply', color='black', linewidth=2)

# Fill areas of deficit and excess
plt.fill_between(time, supply, demand, where=(demand > supply), facecolor='pink', alpha=0.5, interpolate=True, label='Deficit')
plt.fill_between(time, supply, demand, where=(demand < supply), facecolor='gold', alpha=0.5, interpolate=True, label='Excess')

# Adjusting x-axis limits to touch the left and right edges
plt.xlim(time.min(), time.max())

# Remove numerical values from both X and Y axes
plt.xticks([])
plt.yticks([])

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy Demand and Supply Mismatch')
plt.legend()

# SaVE Plot
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\power_supply_demand.png')





