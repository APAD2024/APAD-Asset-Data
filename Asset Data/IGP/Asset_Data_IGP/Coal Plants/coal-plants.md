# Coal Plant (IGP Region) Dataset

## Description

The Coal Plant dataset is a comprehensive collection of data detailing various aspects of coal power plants for the Indo-Gangetic Plain (IGP) region spanning **Pakistan**, **India**, and **Bangladesh**. This dataset includes information on plant locations, capacities, emissions, operational status, and other relevant attributes. The primary goal of this dataset is to enable the monitoring and analysis of air pollution and its impact on the environment and public health.

## Dataset Contents

- **Plant Information**: Names, locations (latitude and longitude), and operational status of coal power plants.
- **Capacity**: Generation capacity of each plant, measured in megawatts (MW).
- **Emissions**: Data on various emissions, including SO2, NOx, and particulate matter (PM2.5 & PM10).

## 🗂️ **Dataset Overview**

| Column Name | Description |
|-------------|-------------|
| FID       | Unique ID for each power plant record. |
| plnt_nm   | Name of the power plant. |
| country   | Country where the plant is located (India, Pakistan, Bangladesh). |
| cap_all   | List of generation capacities (in MW) of each unit within the plant. |
| ttl_cp_   | Total capacity of the plant (in MW). |
| stts_ll   | Status of units in the plant (operating, permitted, etc.). |
| units     | Total number of operational units. |
| status    | Current overall status of the plant (operating, permitted, etc.). |
| prod_kw   | Annual electricity production (in kWh). |
| nx_ef | Nitrogen oxide emission factor (grams per kWh [g/kWh]).|
| nx_tn_y   | NOx (Nitrogen Oxides) emissions (in tons/year). |
| so2_ef | SO2 emission factor (grams per kWh [g/kWh]).|
| so2_tn_y   | SO2 emissions (in tons/year). |
| p10_ef | PM10 (Particulate Matter < 10µm) emission factor (grams per kWh [g/kWh]).|
| p10_tn_   | PM10 (Particulate Matter < 10µm) emissions (in tons/year). |
| pm25_ef | PM2.5 (Particulate Matter < 2.5µm) emission factor (grams per kWh [g/kWh]).|
| p25_tn_   | PM2.5 (Particulate Matter < 2.5µm) emissions (in tons/year). |
| lat       | Latitude of the plant's location. |
| long      | Longitude of the plant's location. |
| geometry  | Geospatial point geometry in WKT format. |

--- 

## Metadata Overview

| **Metadata Field**     | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Geospatial Coverage** | Indo-Gangetic Plain (IGP)               |
| **Data Formats**        | CSV, GeoJSON, SHP                                                          |
| **Categories**          | Energy and Environment, Emissions and Air Quality, Operational Metrics    |
| **Core Features**       | Locations, capacities, emissions (SO2, NOx, PM10, PM2.5), status     |
| **Utilities**           | GeoJSON for mapping, CSV for statistical analysis, SHP for GIS platforms  |

---

## Purpose

This dataset is designed to support research and policy-making aimed at reducing air pollution from coal power plants. By providing detailed information on plant operations and emissions, the dataset allows for:

- **Air Quality Monitoring**: Tracking emissions to understand their impact on local and global air quality.
- **Regulatory Compliance**: Assessing compliance with environmental regulations and identifying areas needing improvement.
- **Policy Development**: Informing policy decisions to mitigate the environmental and health impacts of coal power generation.
- **Public Awareness**: Raising awareness about the environmental impacts of coal plants and promoting cleaner energy alternatives.


## 🗺️ **How to Use the Dataset**

### 1. 📥 **Download the Data**

Download the dataset from the repository and navigate to the `data` directory to access the GeoJSON file:

- **`coal_plants_IGP.geojson`**
- **`coal_plants_IGP.shp`**
- **`coal_plants_IGP.csv`**
- **`coal_plants_IGP.xlsx`**

### 2. 🗄️ **Dataset File**

This file contains detailed data on **coal power plants** in the IGP region, including attributes like capacity, emissions, and geospatial coordinates.

```plaintext
data/
│
├── coal_plants_IGP.geojson  # Main dataset with geospatial data
└── coal_plants_IGP.shp # Directory containing visualization maps
└── coal_plants_IGP.csv
```

## 🔧 **How to Load and Visualize Data**

You can visualize the dataset using Python libraries like `geopandas` and `matplotlib`. Here's a quick guide:

You can also look at the **Data Exploration And Analysis.ipynb** for reference.

### Step 1: Install dependencies

```bash
pip install geopandas matplotlib folium
```

### Step 2: Load and visualize the data

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON data
gdf = gpd.read_file('data/coal_plants_IGP.geojson')

# Plot the data
gdf.plot(marker='o', color='red', markersize=5, figsize=(10, 10))
plt.title("Coal Plants in IGP Region")
plt.show()
```

### Step 3: Interactive Map with Folium

```python
import folium

# Create a map centered on the IGP region
m = folium.Map(location=[24.5, 83], zoom_start=5)

# Add markers for each plant
for _, row in gdf.iterrows():
    folium.Marker(
        location=[row['lat'], row['long']],
        popup=f"{row['plnt_nm']} ({row['country']})",
        icon=folium.Icon(color="red")
    ).add_to(m)

```

## 🔮 **Expected Updates**

We plan to continuously update the dataset to include:
- **Newly built plants** and upcoming plants.
- **Decommissioning statuses** for obsolete plants.
- **Monthly emission data** for more accurate environmental impact analysis.
- **Historical trends** in capacity and production.

---

## 📊 **Key Insights & Visualizations**

The repository contains various interactive maps and visualizations highlighting:
- The **distribution of coal plants** across the region.
- **Emission statistics** (NOx, SOx, PM10, PM2.5).
- Power generation capacities compared across Pakistan, India, and Bangladesh.



![Power Plant Distribution](https://github.com/user-attachments/assets/326e0352-cd18-4752-b536-e324b2631109) | ![Emissions Bar Graph](https://github.com/user-attachments/assets/a865a166-268e-4784-a945-0f20ae69ba3c
) 

---

## 📋 **Contributing**

We welcome contributions to expand and refine this dataset! Whether you have access to more recent data or can help visualize the data better, feel free to submit a **Pull Request**.

1. Fork the repository 🍴
2. Create your feature branch (`git checkout -b feature/your-feature`) 🌱
3. Commit your changes (`git commit -m 'Add some feature'`) 💡
4. Push to the branch (`git push origin feature/your-feature`) 🚀
5. Open a Pull Request 🤝

---

## 🔗 **References**

- **Particulate Matter $\ (PM_{2.5})\$ and $\ (PM_{10})\$:**
   - Emissions per unit: $\ 0.16-0.22 \text{ g/KWh}\$ for PM2.5
   - Emissions per unit: $\ 0.29-0.45 \text{ g/KWh}\$ for PM10
   - Source: [India Air Quality - Coal Power Plants Emissions](https://www.indiaairquality.info/wp-content/uploads/docs/2014-08-AE-Emissions-Health-Coal-PPs-India.pdf)

- **Sulfur Dioxide $\ (SO_2)\$:**
   - Emissions per unit: $\ 7.20  \text{ g/KWh}\$
   - Source: [US EPA - Emissions Inventory Conference](https://www3.epa.gov/ttnchie1/conference/ei20/session5/mmittal.pdf)

- **Nitrogen Oxides $\ ((NO_x)\$:**
   - Emissions per unit: $\ 4.22 - 4.38 \text{ g/KWh}\$
   - Source: [US EPA - Emissions Inventory Conference](https://www3.epa.gov/ttnchie1/conference/ei20/session5/mmittal.pdf)
- **Data Sources**
   - [India Coal Power Plants Database - Source Watch](http://www.sourcewatch.org/index.php/SourceWatch:GNU_Free_Documentation_License)
   - [GEM](https://globalenergymonitor.org/projects/global-coal-plant-tracker/)
 
---
## 📞 **Contact Information**

- **Project Lead**: [hassanaftabsheikh](https://github.com/hassanaftabsheikh)
- **Email**: hassan.sheikh@smithschool.ox.ac.uk
- **Website**: [APAD WORLD](https://apad.world/)

Feel free to reach out for any questions or collaborations! ✉️

---

> 🌱 **"Sustainability begins with awareness"** - Help us spread the word about the environmental impacts of coal power generation in the IGP region.

---

