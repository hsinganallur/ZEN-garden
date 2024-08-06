import pandas as pd
import matplotlib.pyplot as plt

# Load the additional data for detailed contributions
opex_split = pd.read_csv('C:\\Users\\Hareesh S P\\Downloads\\data_opex_split.csv')
capex_split = pd.read_csv('C:\\Users\\Hareesh S P\\Downloads\\data_capex_split.csv')
carrier_split = pd.read_csv("C:\\Users\\Hareesh S P\\Downloads\\data_carrier_split.csv")

# Convert all values to billions by dividing by 1000
opex_split.iloc[:, 1:] /= 1000
capex_split.iloc[:, 1:] /= 1000
carrier_split.iloc[:, 1:] /= 1000

# Define the color mapping for technologies
tech_colors = {
    "DAC": 'aqua',
    "biomass_boiler": 'darkseagreen',
    "biomass_boiler_DH": 'lightseagreen',
    "biomass_plant": 'springgreen',
    "biomass_plant_CCS": 'mediumseagreen',
    "carbon_storage": 'limegreen',
    "district_heating_grid": 'lime',
    "electrode_boiler": 'mediumspringgreen',
    "electrode_boiler_DH": 'darkgreen',
    "hard_coal_boiler": 'brown',
    "hard_coal_boiler_DH": 'darkred',
    "hard_coal_plant": 'firebrick',
    "hard_coal_plant_CCS": 'maroon',
    "heat_pump": 'yellowgreen',
    "heat_pump_DH": 'olive',
    "lignite_coal_plant": 'chocolate',
    "lng_terminal": 'peru',
    "natural_gas_boiler": 'darkgoldenrod',
    "natural_gas_boiler_DH": 'goldenrod',
    "natural_gas_turbine": 'khaki',
    "natural_gas_turbine_CCS": 'gold',
    "nuclear": 'slateblue',
    "oil_boiler": 'orangered',
    "oil_boiler_DH": 'coral',
    "oil_plant": 'tomato',
    "photovoltaics": 'orange',
    "reservoir_hydro": 'skyblue',
    "run-of-river_hydro": 'deepskyblue',
    "waste_boiler_DH": 'lightblue',
    "waste_plant": 'powderblue',
    "wind_offshore": 'aquamarine',
    "wind_onshore": 'deeppink',
    "battery": 'darkslategray',
    "hydrogen_storage": 'teal',
    "natural_gas_storage": 'darkturquoise',
    "pumped_hydro": 'cadetblue',
    "carbon_pipeline": 'lightsteelblue',
    "natural_gas_pipeline": 'steelblue',
    "power_line": 'darkslateblue',
    "vanadium_redox_flow_battery": 'mediumblue',
    "up_redox_flow_battery_1": 'blue',
    "up_redox_flow_battery_2": 'royalblue',
    "up_redox_flow_battery_3": 'cornflowerblue',
    "up_redox_flow_battery_4": 'lightblue',
    "up_redox_flow_battery_5": 'powderblue'
}

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 8))

# Plot OPEX contributions
bottom_opex = pd.Series([0]*len(opex_split), index=opex_split.index)
for tech in opex_split.columns[1:]:
    color = tech_colors.get(tech, None)
    ax.bar(opex_split['Year'], opex_split[tech], bottom=bottom_opex, label=f'OPEX: {tech}', color=color)
    bottom_opex += opex_split[tech]

# Plot CAPEX contributions
bottom_capex = pd.Series([0]*len(capex_split), index=capex_split.index)
for tech in capex_split.columns[1:]:
    color = tech_colors.get(tech, None)
    ax.bar(capex_split['Year'], capex_split[tech], bottom=bottom_capex, label=f'CAPEX: {tech}', color=color)
    bottom_capex += capex_split[tech]

# Plot Carrier contributions
bottom_carrier = pd.Series([0]*len(carrier_split), index=carrier_split.index)
for carrier in carrier_split.columns[1:]:
    ax.bar(carrier_split['Year'], carrier_split[carrier], bottom=bottom_carrier, label=f'Carrier: {carrier}')
    bottom_carrier += carrier_split[carrier]

# Final adjustments
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_xlabel('Year')
ax.set_ylabel('Cost (Billion Euros)')
ax.set_title('Stacked Costs by Year with Detailed Contributions')
plt.tight_layout()

# Save or display the plot
plt.show()  # You can use plt.savefig('filename.png') to save the plot




"""import numpy as np
import pandas as pd

# Given values
year_start = 2022
value_start = 1400
year_end = 2050
value_end = 700

# Number of years
years = np.arange(year_start, year_end + 1)

# Generate exponential data
values = np.logspace(np.log10(value_start), np.log10(value_end), len(years))

# Create DataFrame
data = pd.DataFrame({'Year': years, 'Value': values})

# Display the DataFrame
print(data)
"""

"""import matplotlib.pyplot as plt
import numpy as np

# Data provided
data = [
    ('biomass_plant', 'power', 'DE', 0.001984),
    ('hard_coal_plant', 'power', 'DE', 0.013054),
    ('lignite_coal_plant', 'power', 'AT', 0.003648),
    ('lignite_coal_plant', 'power', 'CH', 0.003774),
    ('lignite_coal_plant', 'power', 'DE', 0.027838),
    ('natural_gas_turbine', 'power', 'DE', 0.011386),
    ('nuclear', 'power', 'CH', 0.00219),
    ('nuclear', 'power', 'DE', 0.006615),
    ('photovoltaics', 'power', 'AT', 0.002742),
    ('photovoltaics', 'power', 'CH', 0.003646),
    ('photovoltaics', 'power', 'DE', 0.061051),
    ('reservoir_hydro', 'power', 'AT', 0.001859),
    ('reservoir_hydro', 'power', 'CH', 0.006701),
    ('run-of-river_hydro', 'power', 'AT', 0.003256),
    ('run-of-river_hydro', 'power', 'CH', 0.003156),
    ('wind_offshore', 'power', 'DE', 0.007682),
    ('wind_onshore', 'power', 'AT', 0.002863),
    ('wind_onshore', 'power', 'DE', 0.053814),
    ('pumped_hydro', 'power', 'AT', 0.005843),
    ('pumped_hydro', 'power', 'CH', 0.004681),
    ('pumped_hydro', 'power', 'DE', 0.004997)
]

# Colors for each technology
color_map = {
    "biomass_plant": 'springgreen',
    "hard_coal_plant": 'firebrick',
    "lignite_coal_plant": 'chocolate',
    "natural_gas_turbine": 'khaki',
    "nuclear": 'slateblue',
    "photovoltaics": 'orange',
    "reservoir_hydro": 'skyblue',
    "run-of-river_hydro": 'deepskyblue',
    "wind_offshore": 'aquamarine',
    "wind_onshore": 'deeppink',
    "pumped_hydro": 'cadetblue'
}

# Extracting data for each country
countries = ['AT', 'DE', 'CH']
technologies = []
values = {country: [] for country in countries}

for tech, _, country, value in data:
    if tech not in technologies:
        technologies.append(tech)
    values[country].append(value)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Width of the bars
bar_width = 0.35
index = np.arange(len(countries))

# Plot each technology as a stacked bar
bottom = np.zeros(len(countries))

for i, tech in enumerate(technologies):
    tech_values = [values[country][i] if i < len(values[country]) else 0 for country in countries]
    ax.bar(index, tech_values, bar_width, label=tech, bottom=bottom, color=color_map.get(tech, 'gray'))
    bottom += tech_values

ax.set_xlabel('Countries')
ax.set_ylabel('Power (TW)')
ax.set_title('Power Generation by Technology and Country')
ax.set_xticks(index)
ax.set_xticklabels(countries)
ax.legend()

# Adjusting Y-axis limits
ax.set_ylim(0, 0.3)  # Adjust this limit as per your requirement

plt.tight_layout()
plt.show()

# Data provided for energy generation
energy_data = [
    ('pumped_hydro', 'energy', 'AT', 0.105854),
    ('pumped_hydro', 'energy', 'CH', 0.0848),
    ('pumped_hydro', 'energy', 'DE', 0.025284)
]

# Colors for each technology (reuse the previous color map for consistency)
color_map = {
    "pumped_hydro": 'cadetblue'
}

# Extracting data for each country
countries = ['AT', 'DE', 'CH']
technologies = []
energy_values = {country: [] for country in countries}

for tech, _, country, value in energy_data:
    if tech not in technologies:
        technologies.append(tech)
    energy_values[country].append(value)

# Plotting energy data
fig, ax = plt.subplots(figsize=(10, 6))

# Width of the bars
bar_width = 0.35
index = np.arange(len(countries))

# Plot each technology as a stacked bar
bottom = np.zeros(len(countries))

for i, tech in enumerate(technologies):
    tech_values = [energy_values[country][i] if i < len(energy_values[country]) else 0 for country in countries]
    ax.bar(index, tech_values, bar_width, label=tech, bottom=bottom, color=color_map.get(tech, 'gray'))
    bottom += tech_values

ax.set_xlabel('Countries')
ax.set_ylabel('Energy')
ax.set_title('Energy Generation by Technology and Country')
ax.set_xticks(index)
ax.set_xticklabels(countries)
ax.legend()

# Adjusting Y-axis limits
ax.set_ylim(0, 0.3)  # Adjust this limit as per your requirement

plt.tight_layout()
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

# Provided data
installed_battery_energy_capacities = [1.895660994063559, 1.2667246940871096, 2.3559550329609974, 1.400711801020117, 1.6328159422367958, 2.8443719489602095, 0.8007480579013488,
                                       2.581884447468497, 2.581884447468497, 3.0451920636379855, 1.5336799827347043]
time_steps = [1000, 800, 400, 80, 72, 4380, 100, 2000,3000,6000,8760]

# Plotting the data as a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(time_steps, installed_battery_energy_capacities, color='b', label='Installed Capacity')

# Adding title and labels
plt.title('Installed Battery Energy Capacities Over Time Steps')
plt.xlabel('Time Steps')
plt.ylabel('Installed Battery Energy Capacity (TWh)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Provided data
installed_battery_power_capacities = [0.34340603558962505, 0.21331998615219487,
                                       0.14502107743315875, 0.16066099634396886,
                                       0.6173959631300573, 0.09005729100899161,
                                       0.8007480579013488,
                                       0.4950679051726866, 0.4950679051726866,
                                       0.6437273364029385, 0.3132161880280894]
time_steps = [1000, 800, 400, 80, 72, 4380, 100, 2000,3000,6000,8760]

# Plotting the data as a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(time_steps, installed_battery_power_capacities, color='b', label='Installed Capacity')

# Adding title and labels
plt.title('Installed Battery Power Capacities Over Time Steps')
plt.xlabel('Time Steps')
plt.ylabel('Installed Battery Power Capacity (TWh)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
"""

"""import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = ['LiB', 'HS', 'PH', 'VRFB', 'UPMRFB']
E_P_min = [1/60, 1/60, 4, 1, 1]  # Minimum E/P in hours (converted minutes to hours)
E_P_max = [8, 7*24, 16, 30, 30]  # Maximum E/P in hours (extended for VRFB and UPMRFB)

# Number of variables
num_vars = len(labels)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is made in a circular (not polygon) shape, so we need to "complete the loop"
# and append the start to the end.
E_P_min += E_P_min[:1]
E_P_max += E_P_max[:1]
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], labels, fontsize=15)  # Set font size for the labels

# Draw ylabels
ax.set_rscale('log')
ax.set_rlabel_position(0)
plt.yticks([0.1, 1, 10, 100, 200], ["0.1h", "1h", "10h", "100h", "200h"], color="grey", size=15)  # Set font size for the y-ticks
plt.ylim(0.1, 200)

# Plot data
ax.plot(angles, E_P_min, linewidth=1, linestyle='solid', label='E/P Min')
ax.fill(angles, E_P_min, 'b', alpha=0.1)

ax.plot(angles, E_P_max, linewidth=1, linestyle='solid', label='E/P Max')
ax.fill(angles, E_P_max, 'r', alpha=0.1)

# Adjust layout
plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=15)  # Set font size for the legend

plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\WebSpider.png")"""


"""
#BackgroundPlot
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Load the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for European countries, excluding Russia
europe = world[(world['continent'] == 'Europe') & (world['name'] != 'Russia')]

# Define regions and their countries
regions = {
    'Western Europe': ['Austria', 'Belgium', 'France', 'Germany', 'Luxembourg', 'Netherlands', 'Switzerland'],
    'Northern Europe': ['Denmark', 'Estonia', 'Finland', 'Iceland', 'Ireland', 'Latvia', 'Lithuania', 'Norway', 'Sweden', 'United Kingdom'],
    'Southern Europe': ['Croatia', 'Greece', 'Italy', 'Portugal', 'Slovenia', 'Spain'],
    'Eastern Europe': ['Bulgaria', 'Czech Republic', 'Hungary', 'Poland', 'Romania', 'Slovakia']
}

# Create a DataFrame for region data
region_data = {
    'country': [],
    'region': []
}

for region, countries in regions.items():
    for country in countries:
        region_data['country'].append(country)
        region_data['region'].append(region)

region_df = pd.DataFrame(region_data)

# Merge the region data with the European map data
europe = europe.merge(region_df, left_on='name', right_on='country')

# Assign colors to each region
region_colors = {
    'Western Europe': '#a6cee3',
    'Northern Europe': '#1f78b4',
    'Southern Europe': '#b2df8a',
    'Eastern Europe': '#33a02c'
}

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the data with region colors
for region, color in region_colors.items():
    region_subset = europe[europe['region'] == region]
    region_subset.plot(ax=ax, color=color, edgecolor='0.8', linewidth=0.8, label=region)

# Customize the plot
#ax.set_title('Map of Continental Europe by Region', fontsize=15)
ax.set_axis_off()

# Set the limits for the zoom (bounding box coordinates)
ax.set_xlim(-10, 40)  # Adjust these values to fit the zoom level you want
ax.set_ylim(30, 83)   # Adjust these values to fit the zoom level you want

# Add legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=region)
           for region, color in region_colors.items()]
ax.legend(handles=handles, loc='upper left', title='Regions', frameon=True)

# Save the plot
plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Europe_Regions_Map_with_Legend.png")

plt.show()"""

"""
#Demand Supply Mismatch
import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
np.random.seed(0)
time = np.arange(0, 10, 0.1)
demand = np.sin(time) + np.random.normal(scale=0.5, size=len(time))
supply = np.sin(time + 0.5) + np.random.normal(scale=0.5, size=len(time))

# Create the plot
plt.figure(figsize=(10, 6))

# Plot supply and demand with straight lines
plt.plot(time, supply, label='Supply', color='black', drawstyle='steps-post')
plt.plot(time, demand, label='Demand', color='gray', drawstyle='steps-post')

# Fill the deficit and excess areas
plt.fill_between(time, supply, demand, where=(supply < demand), step='post', color='lightcoral', alpha=0.5, label='Deficit')
plt.fill_between(time, supply, demand, where=(supply > demand), step='post', color='lightblue', alpha=0.5, label='Excess')

# Highlight the mismatch region
mismatch_start = 50  # Index for start of mismatch (adjust as needed)
mismatch_end = 80    # Index for end of mismatch (adjust as needed)
plt.axvspan(time[mismatch_start], time[mismatch_end], color='gray', alpha=0.3, label='Mismatch')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power Supply and Demand Over Time')
plt.legend(loc='upper right')

# Save the plot to a file
plt.savefig('power_supply_demand_straight_lines.png')

# Save the plot to a file
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\power_supply_demand.png')
"""
"""#Plotting_PI_No_VRFB
import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the folder if it doesn't exist
folder_path = "C:/GitHub/ZEN-garden/looper/PI_No_VRFB"
os.makedirs(folder_path, exist_ok=True)

# Load the data
file_path = "C:/GitHub/ZEN-garden/looper/PI_No_VRFB_Capacity.csv"
df = pd.read_csv(file_path)

# Iterate over unique locations
locations = df['location'].unique()
for location in locations:
    # Filter data for the current location
    location_df = df[df['location'] == location]

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(location_df['year'], location_df['Capacity in kW'], color='skyblue')
    plt.title(f"Capacity vs Year for {location}")
    plt.xlabel("Year")
    plt.ylabel("Capacity (kW)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

    # Save the plot
    plot_filename = os.path.join(folder_path, f"{location}_capacity_bar_plot.png")
    plt.savefig(plot_filename)
    plt.close()

    print(f"Bar plot saved for {location} at: {plot_filename}")

    #Plotting_PI_No_VRFB_PI_VRFB
    import os
    import pandas as pd
    import matplotlib.pyplot as plt


    def plot_and_save_power(df, folder_path):
        # Iterate over unique locations
        locations = df['location'].unique()
        for location in locations:
            # Filter data for the current location
            location_df = df[df['location'] == location]

            # Create a bar plot
            plt.figure(figsize=(10, 6))
            plt.bar(location_df['year'], location_df['Capacity in kW'], color='skyblue')
            plt.title(f"Capacity vs Year for {location}")
            plt.xlabel("Year")
            plt.ylabel("Installed Power (kW)")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

            # Save the plot
            plot_filename = os.path.join(folder_path, f"{location}_capacity_bar_plot.png")
            plt.savefig(plot_filename)
            plt.close()

            print(f"Bar plot saved for {location} at: {plot_filename}")


    def plot_and_save_energy(df, folder_path):
        # Iterate over unique locations
        locations = df['location'].unique()
        for location in locations:
            # Filter data for the current location
            location_df = df[df['location'] == location]

            # Create a bar plot
            plt.figure(figsize=(10, 6))
            plt.bar(location_df['year'], location_df['Capacity in kWh'], color='skyblue')
            plt.title(f"Capacity vs Year for {location}")
            plt.xlabel("Year")
            plt.ylabel("Installed Energy (kWh)")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.xticks(location_df['year'])  # Ensure all years are shown on x-axis

            # Save the plot
            plot_filename = os.path.join(folder_path, f"{location}_capacity_bar_plot.png")
            plt.savefig(plot_filename)
            plt.close()

            print(f"Bar plot saved for {location} at: {plot_filename}")


    # Code for the first data set (No VRFB)
    folder_path_no_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Battery_Energy"
    os.makedirs(folder_path_no_vrfb_beu, exist_ok=True)
    file_path_no_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\PI_No_VRFB_Energy.csv"
    df_no_vrfb_beu = pd.read_csv(file_path_no_vrfb_beu)
    plot_and_save_energy(df_no_vrfb_beu, folder_path_no_vrfb_beu)

    # Code for the second data set (With VRFB)
    folder_path_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Battery_Energy"
    os.makedirs(folder_path_vrfb_beu, exist_ok=True)
    file_path_vrfb_beu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Energy_Battery.csv"
    df_vrfb_beu = pd.read_csv(file_path_vrfb_beu)
    plot_and_save_energy(df_vrfb_beu, folder_path_vrfb_beu)

    # Code for the third data set (With VRFB)
    folder_path_vrfb_vrfbeu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\VRFB_Energy"
    os.makedirs(folder_path_vrfb_vrfbeu, exist_ok=True)
    file_path_vrfb_vrfbeu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Energy_VRFB.csv"
    df_vrfb_vrfbeu = pd.read_csv(file_path_vrfb_vrfbeu)
    plot_and_save_energy(df_vrfb_vrfbeu, folder_path_vrfb_vrfbeu)

    # Code for the fourth data set (No VRFB)
    folder_path_no_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Battery_Energy"
    os.makedirs(folder_path_no_vrfb_ben, exist_ok=True)
    file_path_no_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\PI_No_VRFB_Energy.csv"
    df_no_vrfb_ben = pd.read_csv(file_path_no_vrfb_ben)
    plot_and_save_energy(df_no_vrfb_ben, folder_path_no_vrfb_ben)

    # Code for the fifth data set (With VRFB)
    folder_path_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Battery_Energy"
    os.makedirs(folder_path_vrfb_ben, exist_ok=True)
    file_path_vrfb_ben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Energy_Battery.csv"
    df_vrfb_ben = pd.read_csv(file_path_vrfb_ben)
    plot_and_save_energy(df_vrfb_ben, folder_path_vrfb_ben)

    # Code for the sixth data set (With VRFB)
    folder_path_vrfb_vrfben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\VRFB_Energy"
    os.makedirs(folder_path_vrfb_vrfben, exist_ok=True)
    file_path_vrfb_vrfben = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Energy_VRFB.csv"
    df_vrfb_vrfben = pd.read_csv(file_path_vrfb_vrfben)
    plot_and_save_energy(df_vrfb_vrfben, folder_path_vrfb_vrfben)

    # Code for the seventh data set (No VRFB)
    folder_path_no_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Battery_Power"
    os.makedirs(folder_path_no_vrfb_bpu, exist_ok=True)
    file_path_no_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\PI_No_VRFB_Power.csv"
    df_no_vrfb_bpu = pd.read_csv(file_path_no_vrfb_bpu)
    plot_and_save_power(df_no_vrfb_bpu, folder_path_no_vrfb_bpu)

    # Code for the eighth data set (With VRFB)
    folder_path_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Battery_Power"
    os.makedirs(folder_path_vrfb_bpu, exist_ok=True)
    file_path_vrfb_bpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Power_Battery.csv"
    df_vrfb_bpu = pd.read_csv(file_path_vrfb_bpu)
    plot_and_save_power(df_vrfb_bpu, folder_path_vrfb_bpu)

    # Code for the ninth data set (With VRFB)
    folder_path_vrfb_vrfbpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\VRFB_Power"
    os.makedirs(folder_path_vrfb_vrfbpu, exist_ok=True)
    file_path_vrfb_vrfbpu = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\PI_VRFB_Power_VRFB.csv"
    df_vrfb_vrfbpu = pd.read_csv(file_path_vrfb_vrfbpu)
    plot_and_save_power(df_vrfb_vrfbpu, folder_path_vrfb_vrfbpu)

    # Code for the tenth data set (No VRFB)
    folder_path_no_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Battery_Power"
    os.makedirs(folder_path_no_vrfb_bpn, exist_ok=True)
    file_path_no_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\PI_No_VRFB_Power.csv"
    df_no_vrfb_bpn = pd.read_csv(file_path_no_vrfb_bpn)
    plot_and_save_power(df_no_vrfb_bpn, folder_path_no_vrfb_bpn)

    # Code for the eleventh data set (With VRFB)
    folder_path_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Battery_Power"
    os.makedirs(folder_path_vrfb_bpn, exist_ok=True)
    file_path_vrfb_bpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Power_Battery.csv"
    df_vrfb_bpn = pd.read_csv(file_path_vrfb_bpn)
    plot_and_save_power(df_vrfb_bpn, folder_path_vrfb_bpn)

    # Code for the twelfth data set (With VRFB)
    folder_path_vrfb_vrfbpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\VRFB_Power"
    os.makedirs(folder_path_vrfb_vrfbpn, exist_ok=True)
    file_path_vrfb_vrfbpn = "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\PI_VRFB_Power_VRFB.csv"
    df_vrfb_vrfbpn = pd.read_csv(file_path_vrfb_vrfbpn)
    plot_and_save_power(df_vrfb_vrfbpn, folder_path_vrfb_vrfbpn)

    #Plotting_PI_No_VRFB_PI_VRFB_totals
    import pandas as pd
    import matplotlib.pyplot as plt


    def generate_plots(file_path, save_path):
        # Load the data
        data = pd.read_csv(file_path)

        # Task 1: Count the number of years
        num_years = len(
            data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"
        data.iloc[:, 3:] *= 1000000

        # Task 2: Extract data for power and energy for each technology
        power_data = {}
        energy_data = {}
        for tech in data['technology'].unique():
            tech_data = data[data['technology'] == tech]
            power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
            energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

        # Task 3: Generate plot of installed power for each country for each technology
        for tech, power_df in power_data.items():
            fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
            for country in power_df['location'].unique():
                country_data = power_df[power_df['location'] == country]
                ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

            ax.set_xlabel('Year')
            ax.set_ylabel('Installed Power (kW)')
            ax.set_title('Installed Power Over Years')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
            ax.set_ylim(bottom=0)  # Set the lower limit of y-axis to 0
            ax.set_ylim(top=None)  # Remove the upper limit of y-axis
            plt.tight_layout()  # Adjust layout
            plt.savefig(f"{save_path}/{tech}_installed_power.png",
                        bbox_inches='tight')  # Save plot with tight bounding box

        # Task 4: Generate plot of installed energy for each country for each technology
        for tech, energy_df in energy_data.items():
            fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
            for country in energy_df['location'].unique():
                country_data = energy_df[energy_df['location'] == country]
                ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

            ax.set_xlabel('Year')
            ax.set_ylabel('Installed Energy (kWh)')
            ax.set_title('Installed Energy Over Years')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
            ax.set_ylim(bottom=0)  # Set the lower limit of y-axis to 0
            ax.set_ylim(top=None)  # Remove the upper limit of y-axis
            plt.tight_layout()  # Adjust layout
            plt.savefig(f"{save_path}/{tech}_installed_energy.png",
                        bbox_inches='tight')  # Save plot with tight bounding box


    # List of file paths and corresponding save paths
    file_save_paths = [
        ("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv",
         "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\All_Technologies_Total"),
        ("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv",
         "C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\Unlimited_Imports\\All_Technologies_Total"),
        ("C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\Unsorted\\PI_No_VRFB_Capacity_Total_Unsorted.csv",
         "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\No_Imports\\All_Technologies_Total"),
        (
        "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\Unsorted\\PI_No_VRFB_Capacity_Total_Unsorted.csv",
        "C:\\GitHub\\ZEN-garden\\looper\\PI_No_VRFB\\Unlimited_Imports\\All_Technologies_Total")]

    # Generate plots for each file
    for file_path, save_path in file_save_paths:
        generate_plots(file_path, save_path)

    # Load the data
    data = pd.read_csv("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv")  # Replace "your_data.csv" with the path to your data file

    # Task 1: Count the number of years
    num_years = len(data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"

    # Task 2: Extract data for power and energy for each technology
    power_data = {}
    energy_data = {}
    for tech in data['technology'].unique():
        tech_data = data[data['technology'] == tech]
        power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
        energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

    # Task 3: Generate plot of installed power  for each country for each technology
    for tech, power_df in power_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in power_df['location'].unique():
            country_data = power_df[power_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Power')
        ax.set_title('Installed Power Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_power.png", bbox_inches='tight')  # Save plot with tight bounding box

    # Task 4: Generate plot of installed energy for each country for each technology
    for tech, energy_df in energy_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in energy_df['location'].unique():
            country_data = energy_df[energy_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Energy')
        ax.set_title('Installed Energy Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_energy.png", bbox_inches='tight')  # Save plot with tight bounding box

    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data
    data = pd.read_csv("C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\PI_VRFB_Capacity_Total_Unsorted.csv")  # Replace "your_data.csv" with the path to your data file

    # Task 1: Count the number of years
    num_years = len(data.columns) - 3  # Assuming the first three columns are "technology", "capacity_type", and "location"

    # Task 2: Extract data for power and energy for each technology
    power_data = {}
    energy_data = {}
    for tech in data['technology'].unique():
        tech_data = data[data['technology'] == tech]
        power_data[tech] = tech_data[tech_data['capacity_type'].str.contains('power')]
        energy_data[tech] = tech_data[tech_data['capacity_type'].str.contains('energy')]

    # Task 3: Generate plot of installed power  for each country for each technology
    for tech, power_df in power_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in power_df['location'].unique():
            country_data = power_df[power_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Power')
        ax.set_title('Installed Power Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_power.png", bbox_inches='tight')  # Save plot with tight bounding box

    # Task 4: Generate plot of installed energy for each country for each technology
    for tech, energy_df in energy_data.items():
        fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
        for country in energy_df['location'].unique():
            country_data = energy_df[energy_df['location'] == country]
            ax.plot(range(1, num_years + 1), country_data.iloc[:, 3:].sum(axis=0), label=f"{country} - {tech}")

        ax.set_xlabel('Year')
        ax.set_ylabel('Installed Energy')
        ax.set_title('Installed Energy Over Years')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Place legend outside the plot
        plt.tight_layout()  # Adjust layout
        plt.savefig(f"C:\\GitHub\\ZEN-garden\\looper\\PI_VRFB\\No_Imports\\Unsorted\\{tech}_installed_energy.png", bbox_inches='tight')  # Save plot with tight bounding box"""

"""#Plotting_PI_No_VRFB_PI_VRFB_totals_V2
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

#Plotting_Configurations_25_04_2024

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
generate_storage_level_plots(file_paths, save_paths, scenarios, selected_technologies, log_scale=True)"""
