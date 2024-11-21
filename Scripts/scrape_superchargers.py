from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


def scrape_tesla_superchargers():
    url = "https://tesla.com/findus/list/superchargers/United+States"

    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Make sure ChromeDriver matches your Chrome version
    driver.get(url)
    time.sleep(5)  # Wait for the page to fully load

    chargers = []  # List to store the scraped data

    # Locate all state blocks (div with class `state`)
    state_blocks = driver.find_elements(By.CLASS_NAME, "state")
    print(f"Found {len(state_blocks)} states. Starting scrape...")

    for state_block in state_blocks:
        try:
            # Extract the state name (from the <h2> tag inside the state block)
            state_name = state_block.find_element(By.TAG_NAME, "h2").text.strip()
            print(f"Scraping data for state: {state_name}")

            # Find all charger rows within the state
            charger_rows = state_block.find_elements(By.CLASS_NAME, "row-state")
            print(f"Found {len(charger_rows)} chargers in {state_name}.")

            for charger_row in charger_rows:
                try:
                    # Extract charger name
                    charger_name = charger_row.find_element(By.TAG_NAME, "a").text.strip()

                    # Extract street address
                    street_address = charger_row.find_element(By.CLASS_NAME, "street-address-states").text.strip()

                    # Extract city and postal code
                    city_postal = charger_row.find_element(By.CLASS_NAME, "locality-city-postal").text.strip()

                    # Combine address components
                    full_address = f"{street_address}, {city_postal}"

                    # Append to the chargers list
                    chargers.append({
                        "State": state_name,
                        "Charger Name": charger_name,
                        "Address": full_address
                    })

                    # Debug output
                    print(f"Scraped: {charger_name} - {full_address}")

                except Exception as e:
                    print(f"Error scraping charger in {state_name}: {e}")

        except Exception as e:
            print(f"Error scraping state block: {e}")

    # Close the WebDriver
    driver.quit()

    # Return the data as a pandas DataFrame
    return pd.DataFrame(chargers)


if __name__ == "__main__":
    print("Starting Tesla Supercharger scraper...")
    data = scrape_tesla_superchargers()
    if not data.empty:
        output_file = "../data/superchargers.csv"
        data.to_csv(output_file, index=False)
        print(f"Scraping completed! Data saved to {output_file}")
    else:
        print("No data scraped.")
