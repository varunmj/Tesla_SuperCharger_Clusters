import geopandas as gpd
import folium
import pandas as pd
from folium.plugins import MarkerCluster

# Load clustered data
print("Loading clustered data...")
clustered_data = gpd.read_file("../data/clustered_superchargers.geojson")

# Compute density (number of superchargers per cluster)
cluster_density = clustered_data.groupby("Cluster").size()
clustered_data["Cluster Density"] = clustered_data["Cluster"].map(cluster_density)

# Define colors for clusters based on density
def assign_color(density):
    if density > 50:
        return "red"
    elif density > 30:
        return "orange"
    elif density > 10:
        return "yellow"
    else:
        return "green"

clustered_data["Color"] = clustered_data["Cluster Density"].apply(assign_color)

# Initialize map
print("Initializing map...")
supercharger_map = folium.Map(location=[37.8, -96], zoom_start=4, tiles="CartoDB dark_matter")

# Add markers to the map
print("Adding points to the map...")
marker_cluster = MarkerCluster().add_to(supercharger_map)
for _, row in clustered_data.iterrows():
    if not pd.isna(row["Latitude"]) and not pd.isna(row["Longitude"]):
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=(
                f"Cluster: {row['Cluster']}<br>"
                f"Density: {row['Cluster Density']}<br>"
                f"Address: {row['Address']}"
            ),
            icon=folium.Icon(color=row["Color"], icon="info-sign"),
        ).add_to(marker_cluster)

# Save map
print("Saving map to supercharger_map.html...")
supercharger_map.save("../data/supercharger_map.html")
print("Map generation completed!")
