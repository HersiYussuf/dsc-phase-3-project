import geopandas as gpd
import matplotlib.pyplot as plt
import mplcursors
# selecting cordinate columns for the ploting of the map
tanzanian_map = df_train[['longitude', 'latitude', 'wpt_name']]

# Load shapefile of Tanzania map
tanzania_map = gpd.read_file('data1\Training-set-labels.csv')

# Plot Tanzania map
fig, ax = plt.subplots(figsize=(10, 10))
tanzania_map.plot(ax=ax, color='lightgray')

# Plot wells on the map
df_wells = gpd.GeoDataFrame(df_train, geometry=gpd.points_from_xy(df_train.longitude, df_train.latitude))
df_wells.plot(ax=ax, markersize=5, color='blue')

# Set plot title and labels
plt.title('Wells in Tanzania')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Set the aspect ratio and adjust the axis limits
ax.set_aspect('equal')
ax.set_xlim([28, 42])  # Adjust the x-axis limits according to your data
ax.set_ylim([-14, 0])  # Adjust the y-axis limits according to your data
ax.set_facecolor('lightgray')

# Add labels to the wells
labels = []
for x, y, label in zip(df_wells.geometry.x, df_wells.geometry.y, df_wells['wpt_name']):
    labels.append(ax.text(x, y, label, fontsize=5))

# Enable interactivity on the map
mplcursors.cursor(labels)

# Show the plot
plt.tight_layout()
plt.show()