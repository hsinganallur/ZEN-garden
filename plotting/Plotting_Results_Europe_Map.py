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

from mpl_toolkits.basemap import Basemap
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
plt.savefig('C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Results\\europe_map_with_stacked_plots.png')




