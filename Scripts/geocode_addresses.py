from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import pandas as pd
import time


def geocode(address, retries=3, delay=1):
    """
    Geocode an address to get its latitude and longitude.
    Includes retry logic and delay for rate limiting.

    Args:
        address (str): The address to geocode.
        retries (int): Number of retries in case of failure.
        delay (int): Delay in seconds between retries.

    Returns:
        tuple: Latitude and Longitude, or (None, None) if geocoding fails.
    """
    geolocator = Nominatim(user_agent="ev-charging-project", timeout=10)  # Increased timeout to 10 seconds
    for attempt in range(retries):
        try:
            print(f"Geocoding address: {address} (Attempt {attempt + 1})")
            location = geolocator.geocode(address)
            if location:
                print(f"Success: {address} -> ({location.latitude}, {location.longitude})")
                return location.latitude, location.longitude
        except (GeocoderTimedOut, GeocoderUnavailable) as e:
            print(f"Timeout or unavailable for address '{address}'. Retrying... ({attempt + 1}/{retries})")
            time.sleep(delay)  # Wait before retrying
        except Exception as e:
            print(f"Error geocoding address '{address}': {e}")
            return None, None
    print(f"Failed to geocode address '{address}' after {retries} attempts.")
    return None, None


if __name__ == "__main__":
    try:
        # Load the Superchargers data
        print("Loading superchargers data...")
        supercharger_df = pd.read_csv("../data/superchargers.csv")
        print(f"Loaded {len(supercharger_df)} addresses for geocoding.")

        # Apply geocoding to the Address column
        print("Starting geocoding...")
        supercharger_df["Latitude"], supercharger_df["Longitude"] = zip(
            *supercharger_df["Address"].apply(lambda x: geocode(x))
        )

        # Save the updated data back to the CSV file
        supercharger_df.to_csv("../data/superchargers.csv", index=False)
        print("Geocoding completed and saved to ../data/superchargers.csv!")
    except Exception as e:
        print(f"Error: {e}")
