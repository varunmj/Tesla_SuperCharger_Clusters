import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon


def generate_mock_population_density():
    """
    Generate mock population density GeoJSON file.
    """
    population_data = {
        "region_id": [1, 2, 3],
        "population_density": [500, 1200, 800],  # Example density values
        "geometry": [
            Polygon([(-125, 49), (-124, 49), (-124, 48), (-125, 48), (-125, 49)]),  # Example polygon 1
            Polygon([(-123, 48), (-122, 48), (-122, 47), (-123, 47), (-123, 48)]),  # Example polygon 2
            Polygon([(-120, 46), (-119, 46), (-119, 45), (-120, 45), (-120, 46)]),  # Example polygon 3
        ],
    }

    population_density_gdf = gpd.GeoDataFrame(population_data, crs="EPSG:4326")
    population_density_gdf.to_file("../data/population_density.geojson", driver="GeoJSON")
    print("Mock population_density.geojson created!")


def generate_mock_traffic_flow():
    """
    Generate mock traffic flow GeoJSON file.
    """
    traffic_data = {
        "region_id": [1, 2, 3],
        "traffic_flow": [200, 400, 300],  # Example traffic flow values
        "geometry": [
            Polygon([(-125, 48), (-124, 48), (-124, 47), (-125, 47), (-125, 48)]),  # Example polygon 1
            Polygon([(-123, 46), (-122, 46), (-122, 45), (-123, 45), (-123, 46)]),  # Example polygon 2
            Polygon([(-121, 44), (-120, 44), (-120, 43), (-121, 43), (-121, 44)]),  # Example polygon 3
        ],
    }

    traffic_flow_gdf = gpd.GeoDataFrame(traffic_data, crs="EPSG:4326")
    traffic_flow_gdf.to_file("../data/traffic_flow.geojson", driver="GeoJSON")
    print("Mock traffic_flow.geojson created!")


def etl_process():
    """
    Perform ETL process with spatial joins on Supercharger data, population density, and traffic flow.
    """
    print("Starting ETL process...")

    # Load data
    supercharger_df = pd.read_csv("../data/superchargers.csv")
    population_density = gpd.read_file("../data/population_density.geojson")
    traffic_data = gpd.read_file("../data/traffic_flow.geojson")

    # Ensure there are no conflicting column names
    reserved_columns = {"index", "index_right"}
    for gdf in [population_density, traffic_data]:
        for col in reserved_columns:
            if col in gdf.columns:
                gdf.rename(columns={col: f"{col}_renamed"}, inplace=True)

    # Reset indices to avoid conflicts
    population_density = population_density.reset_index(drop=True)
    traffic_data = traffic_data.reset_index(drop=True)

    # Convert Supercharger DataFrame to GeoDataFrame
    supercharger_gdf = gpd.GeoDataFrame(
        supercharger_df, geometry=gpd.points_from_xy(supercharger_df.Longitude, supercharger_df.Latitude)
    )
    supercharger_gdf.set_crs("EPSG:4326", inplace=True)

    # Perform spatial joins
    try:
        print("Joining with population density data...")
        supercharger_gdf = gpd.sjoin(
            supercharger_gdf, population_density, how="left", predicate="within", rsuffix="_pop_density"
        )
    except ValueError as e:
        print(f"Error during join with population density: {e}")
        raise

    try:
        print("Joining with traffic data...")
        supercharger_gdf = gpd.sjoin(
            supercharger_gdf, traffic_data, how="left", predicate="within", rsuffix="_traffic"
        )
    except ValueError as e:
        print(f"Error during join with traffic data: {e}")
        raise

    # Save the processed GeoDataFrame to GeoJSON
    supercharger_gdf.to_file("../data/processed_data.geojson", driver="GeoJSON")
    print("ETL process completed and saved to ../data/processed_data.geojson!")


if __name__ == "__main__":
    # Step 1: Generate Mock Data
    print("Generating mock data...")
    generate_mock_population_density()
    generate_mock_traffic_flow()

    # Step 2: Perform ETL Process
    etl_process()
