import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib as mpl

# Replace this with the path where you extracted the downloaded shapefile
shapefile_path = "C:\\Users\\Hareesh S P\\Downloads\\ne_110m_admin_0_countries\\ne_110m_admin_0_countries.shp"

# Load the shapefile
world = gpd.read_file(shapefile_path)

# Filter for Europe
europe = europe = world[(world['CONTINENT'] == 'Europe') & (world['NAME'] != 'Russia')]

# Create a DataFrame for RES data
res_data = {
    'country': ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
                'Germany', 'Greece', 'Hungary', 'Iceland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands',
                'Norway', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
                'United Kingdom'],
    'share_of_res': [24.78, 0.0, 5.04, 30.79, 32.83, 0.0, 100.0, 0.0, 0.0, 19.66, 12.45, 0.0,
 0.0, 24.52, 100.0, 85.15, 100.0, 0.0, 100.0, 0.0, 100.0, 0.0, 21.55, 0.01,
 1.89, 10.71, 27.9, 35.54]
}

res_df = gpd.GeoDataFrame(res_data)

# Merge the RES data with the European map data
europe = europe.merge(res_df, left_on='NAME', right_on='country')

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
cmap = 'Oranges'
norm = mpl.colors.Normalize(vmin=0, vmax=100)

# Plot the data with the specified colormap and normalization
europe.plot(column='share_of_res', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=False)

# Create the colorbar with custom normalization
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm._A = []  # dummy array for the ScalarMappable

# Add the colorbar to the plot
cbar = fig.colorbar(sm, ax=ax)
cbar.ax.tick_params(labelsize=15)
cbar.set_label('Normalised Share of Installed Energy for UP Devices (%)', fontsize=15, fontweight='bold')

# Customize the plot
#ax.set_title('Map of Continental Europe with Projections for 2030', fontsize=15)
ax.set_axis_off()

# Set the limits for the zoom (bounding box coordinates)
ax.set_xlim(-10, 40)  # Adjust these values to fit the zoom level you want
ax.set_ylim(30, 83)   # Adjust these values to fit the zoom level you want

plt.savefig("C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Images\\RES_Map.png")