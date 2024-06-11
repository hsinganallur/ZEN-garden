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

out_folder1 = "C:\\GitHub\\ZEN-garden\\data\\outputs\\Run_4_PI_No_Imports_FB"
r1 = Results(out_folder1)
data_1 = r1.get_total("capacity")
data_1 = data_1.reset_index()

# Extract relevant data for each technology
technologies = ['battery', 'hydrogen_storage', 'pumped_hydro', 'vanadium_redox_flow_battery',
                'up_redox_flow_battery_1', 'up_redox_flow_battery_2',
                'up_redox_flow_battery_3', 'up_redox_flow_battery_4', 'up_redox_flow_battery_5']

tech_data = {}
for tech in technologies:
    tech_data[tech] = data_1[(data_1['capacity_type'] == 'energy') & (data_1['technology'] == tech)]

# Sum the values of columns from 2024 to 2050 and add a new column with the sum
for tech in technologies:
    tech_data[tech]['sum_2024_to_2050'] = tech_data[tech].iloc[:, 3:7].sum(axis=1)

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
    'up_redox_flow_battery_5': '#bcbd22'
}

# Function to get the sum of capacity for each region and each technology
def get_region_data(region, tech_data, regions):
    region_data = {tech: 0 for tech in technologies}
    for country in regions[region]:
        for tech in technologies:
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
                                      startangle=90, textprops=dict(fontsize=14))  # Increased font size

    for text in texts:
        text.set_fontsize(14)  # Increased font size
    for autotext in autotexts:
        autotext.set_fontsize(14)  # Increased font size
        autotext.set_color('white')  # Set color to white

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(
        "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Energy_Storage_Distribution_" + region + ".png",
        format='png', transparent=True)

# Create a separate legend image
fig, ax = plt.subplots()
ax.set_facecolor('none')  # Set the background color to none
color_list = [colors[tech] for tech in technologies]
wedges, texts = ax.pie([1] * len(technologies), labels=technologies, startangle=90, colors=color_list)
ax.clear()
ax.legend(wedges, technologies, loc='center', fontsize=20)  # Increased font size
ax.axis('off')  # Hide the axes
plt.savefig(
    "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\Mid-Term Presentation\\Legend.png",
    format='png', transparent=True)

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
ax.legend(handles=legend_patches, loc=1)"""

# Save the figure
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\europe_map_with_stacked_plots.png')

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


