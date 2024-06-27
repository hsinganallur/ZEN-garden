import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define the regions and their corresponding country codes
regions = {
    'Western Europe': ['AT', 'BE', 'FR', 'DE', 'LU', 'NL', 'CH', 'UK'],
    'Northern Europe': ['DK', 'EE', 'FI', 'IE', 'LV', 'LT', 'NO', 'SE'],
    'Southern Europe': ['HR', 'EL', 'IT', 'PT', 'SI', 'ES'],
    'Eastern Europe': ['BG', 'CZ', 'HU', 'PL', 'RO', 'SK']
}

out_folder1 = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\Results\\Vanilla_PI_FB_No_Power_Lines_Green_4"
r1 = Results(out_folder1)
data_1 = r1.get_total("capacity")
data_1 = data_1.reset_index()

# Extract relevant data for each technology
storage_technologies = ['battery', 'hydrogen_storage', 'pumped_hydro', 'vanadium_redox_flow_battery',
                        'up_redox_flow_battery_1', 'up_redox_flow_battery_2',
                        'up_redox_flow_battery_3', 'up_redox_flow_battery_4', 'up_redox_flow_battery_5']

conversion_technologies = ["DAC", "biomass_boiler", "biomass_plant", "biomass_plant_CCS", "carbon_storage",
                           "hard_coal_plant_CCS", "heat_pump", "lignite_coal_plant", "lng_terminal",
                           "natural_gas_boiler", "natural_gas_turbine", "natural_gas_turbine_CCS", "nuclear",
                           "photovoltaics", "reservoir_hydro", "run-of-river_hydro", "waste_plant", "wind_offshore",
                           "wind_onshore"]

# Define colors for each technology
colors = {
    'battery': '#00BFFF',
    'hydrogen_storage': '#FF6347',
    'pumped_hydro': '#00008B',
    'vanadium_redox_flow_battery': '#d62728',
    'up_redox_flow_battery_1': '#9467bd',
    'up_redox_flow_battery_2': '#8c564b',
    'up_redox_flow_battery_3': '#e377c2',
    'up_redox_flow_battery_4': '#7f7f7f',
    'up_redox_flow_battery_5': '#bcbd22',
    'DAC': '#1f77b4',
    'biomass_boiler': '#ff7f0e',
    'biomass_plant': '#2ca02c',
    'biomass_plant_CCS': '#d62728',
    'carbon_storage': '#9467bd',
    'hard_coal_plant_CCS': '#8c564b',
    'heat_pump': '#e377c2',
    'lignite_coal_plant': '#7f7f7f',
    'lng_terminal': '#bcbd22',
    'natural_gas_boiler': '#17becf',
    'natural_gas_turbine': '#9edae5',
    'natural_gas_turbine_CCS': '#dbdb8d',
    'nuclear': '#393b79',
    'photovoltaics': '#5254a3',
    'reservoir_hydro': '#6b6ecf',
    'run-of-river_hydro': '#9c9ede',
    'waste_plant': '#637939',
    'wind_offshore': '#8ca252',
    'wind_onshore': '#b5cf6b'
}

# Function to plot storage levels over time
def plot_storage_levels_all_regions(storage_data, regions, storage_technologies):
    plt.figure(figsize=(14, 8))
    aggregated_storage_data = pd.DataFrame(columns=storage_data.columns)

    for region in regions:
        region_storage_data = storage_data[storage_data['node'].isin(regions[region])]
        if not region_storage_data.empty:
            aggregated_storage_data = pd.concat([aggregated_storage_data, region_storage_data], ignore_index=True)

    for tech in storage_technologies:
        tech_storage_data = aggregated_storage_data[aggregated_storage_data['technology'] == tech]
        if not tech_storage_data.empty:
            time_steps = tech_storage_data.columns[2:]
            storage_values = tech_storage_data.iloc[:, 2:].sum(axis=0).values / 1000
            if np.any(storage_values > 0.0001):
                plt.plot(time_steps, storage_values, label=f"{tech}", color=colors[tech])

    plt.xlabel('Time Steps', fontsize=15)
    plt.ylabel('Energy Capacity Level (TWh)', fontsize=15)
    plt.title('Energy Over Time', fontsize=15)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Storage_Levels_Over_Time_Europe.png", format='png', bbox_inches='tight')

# Function to plot conversion levels over time
def plot_conversion_levels_all_regions(conversion_data, regions, conversion_technologies):
    # Filter rows where "carrier" column contains the word "electricity"
    conversion_data = conversion_data[conversion_data['carrier'].str.contains('electricity', na=False)]
    conversion_data = conversion_data.drop(columns=['carrier'])

    aggregated_conversion_data = pd.DataFrame(columns=conversion_data.columns)

    for region in regions:
        region_conversion_data = conversion_data[conversion_data['node'].isin(regions[region])]
        if not region_conversion_data.empty:
            aggregated_conversion_data = pd.concat([aggregated_conversion_data, region_conversion_data], ignore_index=True)

    for tech in conversion_technologies:
        tech_conversion_data = aggregated_conversion_data[aggregated_conversion_data['technology'] == tech]
        if not tech_conversion_data.empty:
            time_steps = tech_conversion_data.columns[2:]
            conversion_values = tech_conversion_data.iloc[:, 2:].sum(axis=0).values / 1000
            if np.any(conversion_values > 0.0001):
                plt.plot(time_steps, conversion_values, label=f"{tech}", linestyle='--', color=colors[tech])

    plt.xlabel('Time Steps', fontsize=15)
    plt.ylabel('Energy Conversion Level (TWh)', fontsize=15)
    plt.title('Energy Conversion Over Time', fontsize=15)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Storage_and_Conversion_Levels_Over_Time_Europe.png", format='png', bbox_inches='tight')

# Function to get the total cost
def get_total_cost():
    cost_capex = r1.get_df("cost_capex_total")
    cost_opex = r1.get_df("cost_opex_total")

    # Convert dictionaries to DataFrames
    df_cost_capex = pd.DataFrame.from_dict(cost_capex)
    df_cost_opex = pd.DataFrame.from_dict(cost_opex)

    # Summing up the DataFrames
    total_cost = df_cost_capex.add(df_cost_opex, fill_value=0)

    # Printing the total cost
    print("Total Cost (Capex + Opex):")
    print(total_cost)

get_total_cost()

# Prepare tech_data for plotting
tech_data = {}
for tech in storage_technologies:
    tech_data[tech] = data_1[(data_1['capacity_type'] == 'energy') & (data_1['technology'] == tech)]

# Sum the values of columns from 2024 to 2050 and add a new column with the sum
for tech in storage_technologies:
    tech_data[tech]['sum_2024_to_2050'] = tech_data[tech].iloc[:, 3:7].sum(axis=1)

# Function to get the sum of capacity for each region and each technology
def get_region_data(region, tech_data, regions):
    region_data = {tech: 0 for tech in storage_technologies}
    for country in regions[region]:
        for tech in storage_technologies:
            country_data = tech_data[tech][tech_data[tech]['location'] == country]
            if not country_data.empty:
                region_data[tech] += country_data['sum_2024_to_2050'].values[0]
    return region_data

# Create pie charts for each region
for region in regions:
    region_data = get_region_data(region, tech_data, regions)
    total_capacity = sum(region_data.values())

    labels = [tech for tech in region_data if region_data[tech] > 0 and (region_data[tech] / total_capacity) * 100 >= 1]
    sizes = [region_data[tech] for tech in labels]
    color_list = [colors[tech] for tech in labels]

    fig, ax = plt.subplots()
    ax.set_facecolor('none')  # Set the background color to none
    wedges, texts, autotexts = ax.pie(sizes, colors=color_list, autopct=lambda pct: ('%1.1f%%' % pct) if pct >= 1 else '',
                                      startangle=90, textprops=dict(fontsize=20))  # Increased font size

    for text in texts:
        text.set_fontsize(30)  # Increased font size
    for autotext in autotexts:
        autotext.set_fontsize(30)  # Increased font size
        autotext.set_color('white')  # Set color to white

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(
        "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Energy_Storage_Distribution_" + region + ".png",
        format='png', transparent=True)

# Create a separate legend image
fig, ax = plt.subplots()
ax.set_facecolor('none')  # Set the background color to none
color_list = [colors[tech] for tech in storage_technologies]
wedges, texts = ax.pie([1] * len(storage_technologies), labels=storage_technologies, startangle=90, colors=color_list)
ax.clear()
ax.legend(wedges, storage_technologies, loc='center', fontsize=20)  # Increased font size
ax.axis('off')  # Hide the axes
plt.savefig(
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Legend.png",
    format='png', transparent=True)

# Function to print total installed energy
def print_total_installed_energy(tech_data, regions):
    for region in regions:
        region_data = get_region_data(region, tech_data, regions)
        total_capacity = sum(region_data.values())

        print(f"Total Installed Energy Capacity for {region}:")
        total_region_capacity = sum(region_data.values())
        print(f"Total Capacity: {total_region_capacity} MW")

# Function to get the total installed energy of batteries in Europe
def get_total_installed_battery_energy(tech_data, regions):
    total_battery_capacity = 0
    for region in regions:
        region_data = get_region_data(region, tech_data, regions)
        total_battery_capacity += region_data['battery']
    return total_battery_capacity

# Get the total installed energy of batteries in Europe and print it
total_installed_battery_energy = get_total_installed_battery_energy(tech_data, regions)
print(f"Total Installed Energy Capacity of Batteries in Europe: {total_installed_battery_energy} MW")

print_total_installed_energy(tech_data, regions)

# Plot storage levels over time
storage_data = r1.get_full_ts("storage_level")
storage_data = storage_data.reset_index()
plot_storage_levels_all_regions(storage_data, regions, storage_technologies)

# Plot storage discharges over time
storage_discharge_data = r1.get_full_ts("flow_storage_discharge")
storage_discharge_data = storage_discharge_data.reset_index()

# Plot conversion levels over time
conversion_data = r1.get_full_ts("flow_conversion_output")
conversion_data = conversion_data.reset_index()
plot_conversion_levels_all_regions(conversion_data, regions, conversion_technologies)

"""import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

from zen_garden.postprocess.results.results import Results

def main():
    #zen_garden
    out_folder = "C:\\GitHub\\ZEN-garden\\data\\outputs\\Run_1_PI_Imports"
    r = Results(out_folder)
    data_1 = r.get_total("capacity_addition").groupby('technology').sum()
    data_2 = r.get_total("capacity")
    # First, reset the index to get 'capacity_type' as a column
    data_2 = data_2.reset_index()
    # Filter the DataFrame by capacity_type "power"
    filtered_data = data_2[data_2['capacity_type'] == 'energy']
    a = 1
if __name__ == "__main__":
    main()
"""
#Autoplotting graphs over the map
"""import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for European countries
europe = world[(world['continent'] == 'Europe') & (world['name'] != 'Russia')]

# Define regions (this is a simple example, regions can be defined more specifically)
regions = {
    'Northern Europe': ['Denmark', 'Estonia', 'Finland', 'Iceland', 'Ireland', 'Latvia', 'Lithuania', 'Norway', 'Sweden', 'United Kingdom'],
    'Western Europe': ['Austria', 'Belgium', 'France', 'Germany', 'Liechtenstein', 'Luxembourg', 'Monaco', 'Netherlands', 'Switzerland'],
    'Southern Europe': ['Albania', 'Andorra', 'Bosnia and Herzegovina', 'Croatia', 'Greece', 'Italy', 'Kosovo', 'Malta', 'Montenegro', 'North Macedonia', 'Portugal', 'San Marino', 'Serbia', 'Slovenia', 'Spain', 'Vatican'],
    'Eastern Europe': ['Belarus', 'Bulgaria', 'Czech Republic', 'Hungary', 'Moldova', 'Poland', 'Romania', 'Slovakia', 'Ukraine']
}

# Create a new column in the GeoDataFrame for regions
europe['region'] = None
for region, countries in regions.items():
    europe.loc[europe['name'].isin(countries), 'region'] = region

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
europe.boundary.plot(ax=ax, linewidth=1, color='black')
europe.plot(ax=ax, column='region', categorical=True, legend=True, legend_kwds={'bbox_to_anchor': (1, 1)}, cmap='tab20')

# Add titles and labels
plt.title('Map of Europe (excluding Russia) with Regions')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()"""


"""import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geodatasets import get_path
from shapely.geometry import Point

# Load world map and restrict to Europe excluding Russia
world = gpd.read_file(get_path("naturalearth.land"))
europe = world[world['continent'] == 'Europe']
europe = europe[europe['name'] != 'Russia']

# Create sample data for demonstration
data = {
    'Country': ['France', 'Germany', 'Italy', 'Spain', 'Poland', 'Netherlands', 'Belgium', 'Greece', 'Portugal', 'Sweden'],
    'Value1': [5, 7, 3, 4, 6, 8, 2, 9, 4, 5],
    'Value2': [6, 3, 7, 8, 2, 4, 6, 5, 7, 8]
}
df = pd.DataFrame(data)

# Convert DataFrame to GeoDataFrame by merging with Europe's GeoDataFrame
europe = europe.set_index('name').join(df.set_index('Country'))
europe = europe.reset_index()

# Initialize plot
fig, ax = plt.subplots(1, 1, figsize=(15, 15))

# Plot Europe map
europe.boundary.plot(ax=ax, linewidth=1)

# Plot bar graphs at each country's centroid
for idx, row in europe.iterrows():
    if not pd.isnull(row['Value1']):
        centroid = row['geometry'].centroid
        x, y = centroid.x, centroid.y
        ax.barh([y + 0.5, y - 0.5], [row['Value1'], row['Value2']], height=0.1, align='center', color=['blue', 'red'])

# Set axis off and show plot
ax.set_axis_off()
# Save the figure
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\europe_map_with_stacked_plots.png')"""

"""from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the map extents for Europe
llcrnrlat = 35
llcrnrlon = -12
urcrnrlat = 71
urcrnrlon = 35

# Function to create inset axes and plot stacked bar chart on it
def build_stacked_bar(mapx, mapy, ax, width, country, technologies):
    ax_h = inset_axes(ax, width=width, height=width, loc=3, bbox_to_anchor=(mapx, mapy), bbox_transform=ax.transData, borderpad=0)
    bottom = np.zeros(len(technologies))
    for i, (tech, value) in enumerate(technologies.items()):
        ax_h.bar(country, value, bottom=bottom, label=tech, color=colors[i])
        bottom += value
    ax_h.axis('off')
    return ax_h

fig, ax = plt.subplots(figsize=(10, 9))

# Create the map of Europe
bm = Basemap(llcrnrlat=llcrnrlat, llcrnrlon=llcrnrlon, urcrnrlat=urcrnrlat, urcrnrlon=urcrnrlon,
             ax=ax, resolution='i', projection='tmerc', lon_0=10, lat_0=50)

# Fill continents and draw coastlines
bm.fillcontinents(color='lightyellow', zorder=0)
bm.drawcoastlines(color='gray', linewidth=0.3, zorder=2)

plt.title('Energy Storage Technologies in Europe', fontsize=20)

# Dummy data for energy storage technologies by country
countries = ['Germany', 'France', 'Italy', 'Spain', 'Netherlands', 'Belgium', 'Switzerland', 'Austria', 'Portugal', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Greece', 'Poland', 'Czech Republic', 'Hungary', 'Romania', 'Bulgaria', 'Slovakia', 'Croatia', 'Ireland', 'Lithuania', 'Latvia', 'Estonia', 'Slovenia', 'Cyprus', 'Luxembourg', 'Malta']
technologies = {'Batteries': np.random.randint(10, 100, len(countries)), 'Pumped Hydro': np.random.randint(10, 100, len(countries)), 'Flywheels': np.random.randint(10, 100, len(countries))}

# Define colors for different technologies
colors = ['blue', 'green', 'red']

# Loop over countries and plot stacked bar charts
bar_width = 0.2
for country in countries:
    lon, lat = bm(10, 50)  # Dummy coordinates
    build_stacked_bar(lon, lat, ax, bar_width, country, technologies)

# Create legend
legend_patches = [mpatches.Patch(color=colors[i], label=tech) for i, tech in enumerate(technologies.keys())]
ax.legend(handles=legend_patches, loc=1)

# Save the figure
#plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\europe_map_with_stacked_plots.png')"""

"""import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

def plot_europe_map(output_file):
    # Load the world map dataset from GeoPandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Filter the dataset to include only European countries, excluding Russia
    europe = world[(world['continent'] == 'Europe') & (world['name'] != 'Russia')]

    # Further filter out entries with iso_a3 code '-99'
    europe = europe[europe['iso_a3'] != '-99']

    # Create a figure
    fig = plt.figure(figsize=(15, 10))
    ax_map = fig.add_axes([0, 0, 1, 1])
    europe.plot(ax=ax_map, color='whitesmoke', edgecolor='black')

    # Sample data for energy storage technologies
    countries = europe['iso_a3'].tolist()  # European country codes
    battery = np.random.randint(1, 20, len(countries))
    pumped_hydro = np.random.randint(1, 20, len(countries))
    thermal = np.random.randint(1, 20, len(countries))

    # Plot stacked bar plots for each country
    for i, country in enumerate(countries):
        # Get the centroid of the country
        centroid = europe[europe['iso_a3'] == country]['geometry'].centroid.values[0]
        lon, lat = centroid.x, centroid.y

        # Add a new axes for the bar plot inside the country
        ax_bar = fig.add_axes([0.5 * (1 + lon / 180), 0.5 * (1 + lat / 90), 0.05, 0.05])

        # Plot stacked bar plot
        ax_bar.bar([1, 2, 3], [battery[i], pumped_hydro[i], thermal[i]], color=['blue', 'green', 'red'])
        ax_bar.set_axis_off()

    plt.savefig(output_file, bbox_inches='tight')
    plt.close(fig)

# Specify the output file path
output_file = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\europe_map.png'

# Generate and save the map
plot_europe_map(output_file)

print(f"Map saved to {output_file}")"""

"""import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define the regions and their corresponding country codes
regions = {
    'Western Europe': ['AT', 'BE', 'FR', 'DE', 'LU', 'NL', 'CH', 'UK'],
    'Northern Europe': ['DK', 'EE', 'FI', 'IE', 'LV', 'LT', 'NO', 'SE'],
    'Southern Europe': ['HR', 'EL', 'IT', 'PT', 'SI', 'ES'],
    'Eastern Europe': ['BG', 'CZ', 'HU', 'PL', 'RO', 'SK']
}

out_folder1 = "C:\\GitHub\\ZEN-garden\\data\\outputs\\Vanilla_PI_FB_No_Power_Lines_Green_3"
r1 = Results(out_folder1)
data_1 = r1.get_total("capacity")
data_1 = data_1.reset_index()

# Extract relevant data for each technology
storage_technologies = ['battery', 'hydrogen_storage', 'pumped_hydro', 'vanadium_redox_flow_battery',
                        'up_redox_flow_battery_1', 'up_redox_flow_battery_2',
                        'up_redox_flow_battery_3', 'up_redox_flow_battery_4', 'up_redox_flow_battery_5']

conversion_technologies = ["DAC", "biomass_boiler", "biomass_plant", "biomass_plant_CCS", "carbon_storage",
                           "hard_coal_plant_CCS", "heat_pump", "lignite_coal_plant", "lng_terminal",
                           "natural_gas_boiler", "natural_gas_turbine", "natural_gas_turbine_CCS", "nuclear",
                           "photovoltaics", "reservoir_hydro", "run-of-river_hydro", "waste_plant", "wind_offshore",
                           "wind_onshore"]

# Define colors for each technology
colors = {
    'battery': '#00BFFF',
    'hydrogen_storage': '#FF6347',
    'pumped_hydro': '#00008B',
    'vanadium_redox_flow_battery': '#d62728',
    'up_redox_flow_battery_1': '#9467bd',
    'up_redox_flow_battery_2': '#8c564b',
    'up_redox_flow_battery_3': '#e377c2',
    'up_redox_flow_battery_4': '#7f7f7f',
    'up_redox_flow_battery_5': '#bcbd22',
    'DAC': '#1f77b4',
    'biomass_boiler': '#ff7f0e',
    'biomass_plant': '#2ca02c',
    'biomass_plant_CCS': '#d62728',
    'carbon_storage': '#9467bd',
    'hard_coal_plant_CCS': '#8c564b',
    'heat_pump': '#e377c2',
    'lignite_coal_plant': '#7f7f7f',
    'lng_terminal': '#bcbd22',
    'natural_gas_boiler': '#17becf',
    'natural_gas_turbine': '#9edae5',
    'natural_gas_turbine_CCS': '#dbdb8d',
    'nuclear': '#393b79',
    'photovoltaics': '#5254a3',
    'reservoir_hydro': '#6b6ecf',
    'run-of-river_hydro': '#9c9ede',
    'waste_plant': '#637939',
    'wind_offshore': '#8ca252',
    'wind_onshore': '#b5cf6b'
}

# Function to plot storage levels over time
def plot_storage_levels_all_regions(storage_data, regions, storage_technologies):
    plt.figure(figsize=(14, 8))
    aggregated_storage_data = pd.DataFrame(columns=storage_data.columns)

    for region in regions:
        region_storage_data = storage_data[storage_data['node'].isin(regions[region])]
        if not region_storage_data.empty:
            aggregated_storage_data = pd.concat([aggregated_storage_data, region_storage_data], ignore_index=True)

    for tech in storage_technologies:
        tech_storage_data = aggregated_storage_data[aggregated_storage_data['technology'] == tech]
        if not tech_storage_data.empty:
            time_steps = tech_storage_data.columns[2:]
            storage_values = tech_storage_data.iloc[:, 2:].sum(axis=0).values / 1000
            if np.any(storage_values > 0.0001):
                plt.plot(time_steps, storage_values, label=f"{tech}", color=colors[tech])

    plt.xlabel('Time Steps', fontsize=15)
    plt.ylabel('Energy Capacity Level (TWh)', fontsize=15)
    plt.title('Energy Over Time', fontsize=15)
    plt.grid(True)

# Function to plot conversion levels over time
def plot_conversion_levels_all_regions(conversion_data, regions, conversion_technologies):
    # Filter rows where "carrier" column contains the word "electricity"
    conversion_data = conversion_data[conversion_data['carrier'].str.contains('electricity', na=False)]
    conversion_data = conversion_data.drop(columns=['carrier'])

    aggregated_conversion_data = pd.DataFrame(columns=conversion_data.columns)

    for region in regions:
        region_conversion_data = conversion_data[conversion_data['node'].isin(regions[region])]
        if not region_conversion_data.empty:
            aggregated_conversion_data = pd.concat([aggregated_conversion_data, region_conversion_data], ignore_index=True)

    for tech in conversion_technologies:
        tech_conversion_data = aggregated_conversion_data[aggregated_conversion_data['technology'] == tech]
        if not tech_conversion_data.empty:
            time_steps = tech_conversion_data.columns[2:]
            conversion_values = tech_conversion_data.iloc[:, 2:].sum(axis=0).values / 1000
            if np.any(conversion_values > 0.0001):
                plt.plot(time_steps, conversion_values, label=f"{tech} (Europe)", linestyle='--', color=colors[tech])

    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig("C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Storage_and_Conversion_Levels_Over_Time_Europe.png", format='png', bbox_inches='tight')

storage_data = r1.get_full_ts("storage_level")
storage_data = storage_data.reset_index()

conversion_data = r1.get_full_ts("flow_conversion_output")
conversion_data = conversion_data.reset_index()

plt.figure(figsize=(14, 8))
plot_storage_levels_all_regions(storage_data, regions, storage_technologies)
plot_conversion_levels_all_regions(conversion_data, regions, conversion_technologies)
"""


