from sklearn.cluster import KMeans
import geopandas as gpd

if __name__ == "__main__":
    # Load processed data
    print("Loading processed data...")
    processed_data = gpd.read_file("../data/processed_data.geojson")

    # Ensure the CRS is set (default to WGS84 if not)
    if processed_data.crs is None:
        processed_data.set_crs("EPSG:4326", inplace=True)

    # Check for Latitude and Longitude columns
    if "Latitude" not in processed_data.columns or "Longitude" not in processed_data.columns:
        raise ValueError("Latitude and Longitude columns are missing in the processed data.")

    # Prepare locations for clustering
    locations = processed_data[["Latitude", "Longitude"]].dropna().values
    if locations.shape[0] == 0:
        raise ValueError("No valid Latitude and Longitude data available for clustering.")

    print(f"Clustering {locations.shape[0]} locations into 10 clusters...")

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=10, random_state=42).fit(locations)
    processed_data["Cluster"] = -1  # Initialize with -1 for unmatched rows
    processed_data.loc[processed_data[["Latitude", "Longitude"]].notna().all(axis=1), "Cluster"] = kmeans.labels_

    # Save the clustered data to a GeoJSON file
    processed_data.to_file("../data/clustered_superchargers.geojson", driver="GeoJSON")
    print("Clustering completed! Output saved to ../data/clustered_superchargers.geojson")
