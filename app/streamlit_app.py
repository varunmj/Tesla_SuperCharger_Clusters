import streamlit as st
import geopandas as gpd
import os

# Use absolute path for the file
file_path = "/Users/varunmj/Desktop/Projects/Tesla_SuperCharger/data/clustered_superchargers.geojson"

# Check if the file exists
if not os.path.exists(file_path):
    st.error(f"File not found: {file_path}")
    st.stop()

# Load the clustered GeoJSON data
st.title("Tesla Supercharger Clusters")
st.write("Visualizing Tesla Supercharger clusters on the map.")

clustered_data = gpd.read_file(file_path)

# Rename columns for Streamlit compatibility
clustered_data.rename(columns={"Latitude": "latitude", "Longitude": "longitude"}, inplace=True)

# Ensure there are no missing latitude or longitude values
valid_data = clustered_data.dropna(subset=["latitude", "longitude"])

# Display map
st.map(valid_data[["latitude", "longitude"]])

# Display data table
st.write("Clustered Supercharger Data")
st.dataframe(valid_data[["State", "Charger Name", "Address", "latitude", "longitude", "Cluster"]])
