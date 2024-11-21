# 🚗 Tesla Supercharger Clusters Project

Visualizing Tesla Supercharger clusters across the United States using spatial analysis, clustering, and geospatial visualization.

---

## 📋 Project Overview

This project aims to analyze and visualize Tesla Supercharger locations in the United States. By combining Tesla Supercharger data with mock population density and traffic flow data, we identify high-demand zones for EV charging stations. The project leverages powerful geospatial and clustering techniques to provide meaningful insights for optimizing EV infrastructure placement.

---

## 🔧 Key Features

- **Web Scraping**: Extracted real-time Tesla Supercharger data from the official Tesla website.
- **Geocoding**: Transformed raw addresses into geographical coordinates using open geocoding tools.
- **Spatial Analysis**: Enriched data with mock population density and traffic flow data to perform advanced geospatial joins.
- **Clustering**: Applied clustering algorithms (KMeans) to group Superchargers into high-demand zones.
- **Interactive Visualization**: Visualized the clustered Supercharger locations on an interactive map with dynamic color-coding for demand density.
- **Streamlit Dashboard**: Developed a user-friendly Streamlit app for interactive exploration of the data.

---

## 🛠️ Technologies Used

- **Python Libraries**:
  - `Selenium`: For web scraping Supercharger data.
  - `Pandas` and `Geopandas`: For data manipulation and geospatial analysis.
  - `Folium` and `Streamlit`: For interactive map visualization and dashboard development.
  - `Scikit-learn`: For clustering high-demand zones using KMeans.
- **Data Sources**:
  - Tesla Supercharger website (scraped).
  - Mock datasets for population density and traffic flow.

---

## 📊 Workflow

1. **Data Collection**:
   - Scraped Tesla Supercharger locations using Selenium.
   - Geocoded raw addresses to obtain latitude and longitude.

2. **Data Enrichment**:
   - Merged Supercharger data with mock population density and traffic flow data using spatial joins.

3. **Clustering**:
   - Applied KMeans clustering to group Superchargers into demand zones.

4. **Visualization**:
   - Created an interactive map with Folium and rendered it in a Streamlit dashboard.

---

## 📂 Project Structure

```plaintext
Tesla_SuperCharger_Clusters/
│
├── data/
│   ├── population_density.geojson       # Mock population density data
│   ├── traffic_flow.geojson             # Mock traffic flow data
│   ├── superchargers.csv                # Scraped Tesla Superchargers data
│   ├── processed_data.geojson           # Data after spatial joins
│   ├── clustered_superchargers.geojson  # Clustered data with demand zones
│
├── scripts/
│   ├── scrape_superchargers.py          # Web scraping script
│   ├── geocode_addresses.py             # Geocoding script
│   ├── etl_process.py                   # ETL pipeline
│   ├── clustering.py                    # KMeans clustering script
│   ├── generate_map.py                  # Static map generation
│
├── app/
│   ├── streamlit_app.py                 # Streamlit dashboard
│
└── README.md                            # Project documentation

```
---

## 🚀 How to Run

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/varunmj/Tesla_SuperCharger_Clusters.git
cd Tesla_SuperCharger_Clusters
```

### **Step 2: Set Up the Environment**
Create a virtual environment and install the dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

### **Step 3: Run the Scripts**
1. **Scrape Supercharger Data**:
   ```bash
   python scripts/scrape_superchargers.py

   ```
   
2. **Geocode the Data**:
   ```bash
   python scripts/geocode_addresses.py
   ```

3. **Run ETL Process**:
    ```bash
    python scripts/etl_process.py
    ```

4. **Perform Clustering**:
    ```bash
    python scripts/clustering.py
    ```

5. **Generate Map**:
    ```bash
    python scripts/generate_map.py
    ```
    
### **Step 4: Run the Streamlit Dashboard**

  ```bash
  streamlit run app/streamlit_app.py
  ```

## 📊 Output

The project generates:

- **Processed GeoJSON files**: 
  - `processed_data.geojson`: Contains enriched Tesla Supercharger data with population density and traffic flow information.
  - `clustered_superchargers.geojson`: Includes clustered Supercharger data for demand analysis.

- **Interactive Streamlit Dashboard**:
  - Displays Supercharger clusters on an interactive map.
  - Allows users to explore data with details like address, latitude, longitude, and cluster assignments.

- **HTML Map Output**:
  - `supercharger_map.html`: A standalone interactive map showing Supercharger locations and clusters.

## 🌟 Features

- **Data Scraping**:
  - Automates the collection of Tesla Supercharger data directly from the Tesla website.

- **Geocoding**:
  - Converts Supercharger addresses into precise geographic coordinates using an efficient geocoding process.

- **ETL Pipeline**:
  - Integrates and enriches data with additional metrics like population density and traffic flow using spatial joins.

- **Clustering**:
  - Utilizes machine learning (KMeans) to identify demand-heavy regions and clusters for better Supercharger management.

- **Visualization**:
  - Provides an interactive dashboard and HTML maps to visually explore Supercharger locations and clusters.

## 💡 Future Enhancements

- **Real-Time Data Updates**:
  - Automating updates to Supercharger data periodically.

- **Enhanced Clustering**:
  - Incorporate additional factors like vehicle density, weather data, or time-series demand analysis.

- **Advanced Visualization**:
  - Build predictive models to suggest optimal locations for new Supercharger installations.

- **User Engagement**:
  - Provide insights directly to Tesla owners for trip planning.

## 🛠️ Technologies Used

- **Python Libraries**:
  - `pandas`, `geopandas`, `folium`, `scikit-learn`, `streamlit`
- **Tools**:
  - GeoJSON for spatial data
  - Streamlit for dashboard visualization
  - Machine Learning with KMeans clustering

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the project as needed.

## 🙌 Acknowledgments

- **Tesla Inc.**: For making Supercharger data available publicly.
- **Geopy**: For geocoding functionalities.
- **OpenStreetMap**: For population density and traffic data.

---
