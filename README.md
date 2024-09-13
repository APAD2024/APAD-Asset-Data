# Asset-Data Repository Structure

## Repository Overview

This repository contains data related to various assets that contribute to pollution, categorized pollution data, and population exposure risk calculated based on these assets. The repository is organized into three main folders:

1. **Asset Data**
2. **Pollution Data**
3. **Population Exposure Risk**

### 1. Brief Introduction

# Study Area Overview

The study focuses on two major regions: the Indo-Gangetic Plain (IGP) in South Asia and selected countries in Africa. The study area includes several countries and their respective provinces and districts, as detailed below.

## **Indo-Gangetic Plain (IGP) - South Asia**

### Countries Included:
- **India**
- **Bangladesh**
- **Pakistan**

| **Country**   | **States/Regions**                           | **Notable Districts**                   | **Area Covered (sq km)** |
|---------------|----------------------------------------------|-----------------------------------------|--------------------------|
| **India**     | ______________________ | _______ |
| **Bangladesh**| ______________________                     | _____________________        | _______                  |
| **Pakistan**  | Punjab, Sindh, Balochistan, Azad Kashmir, FATA, Islamabad                               | Lahore, Faisalabad, Multan, Hyderabad, Bahawalpur...  | 521919.57 Km²                  |

### Total Area Covered in IGP: **______ square kilometers**

### Environmental and Industrial Focus:
The Indo-Gangetic Plain is a major agricultural and industrial zone, with a high density of brick kilns, coal plants, and other sources of air pollution, making it an ideal area for studying the effects of emissions on air quality, including PM2.5 levels.

### Environmental and Industrial Focus:
These regions in Africa represent a mix of urban industrial areas and rapidly growing cities, where coal-fired power plants, transportation, and industrial emissions contribute significantly to air pollution. These areas provide an important contrast to the IGP for assessing air quality and pollution sources.


#### 2. Asset Data

This folder contains subfolders for each asset type that contributes to pollution. Each subfolder contains data specific to that asset, such as its geographical location, operational details, name-plate capacity, and other relevant information.

You can check the asset layers through [gist](https://gist.github.com/khizerzakir)

- `Asset Data/`
  - `Brick Kiln/`
  - `Cement/`
  - `Steel/`
  - `Marble and Granite/`
  - `Transport/`
  - `Open burning sites/`
  - `Coal/`
  - `Oil/`
  - `Gas/`
  - `Pulp and paper industry/`
  - `Chemical industry/`
  - `Crop stubble burning (seasonal)/`

#### 3. Pollution Data

This folder contains data on various pollutants. The subfolders are organized based on the type of pollutant. Each subfolder contains data related to the specific pollutant, including its concentration levels across different regions.

- `Pollution Data/`
  - `PM2.5/`
  - `PM10/`
  - `SO2/`
  - `NOx/`

#### 4. Population Exposure Risk

This folder contains data related to the population exposure risk to pollutants, calculated based on the assets listed in the Asset Data folder. The calculations use a decay function to estimate the risk levels. A README file is included in this folder to explain the decay function and the calculation process.

- `Population Exposure Risk/`
  - `README.md` (Explanation of the decay function and risk calculation methodology)
  - `Brick Kiln/`
  - `Cement/`
  - `Steel/`
  - `Marble and Granite/`
  - `Transport/`
  - `Open burning sites/`
  - `Coal/`
  - `Oil/`
  - `Gas/`
  - `Pulp and paper industry/`
  - `Chemical industry/`
  - `Crop stubble burning (seasonal)/`

### How can this dataset be used?

This pollution assets dataset is designed to support a wide range of applications related to environmental monitoring and analysis:

Climate Researchers can utilize this data to study pollution trends over time across the Indo-Gangetic Plain (IGP) and Africa, providing insights into how these regions are impacted by various pollution sources. In addition, Geographic Information System (GIS) developers can use this dataset to create detailed visualizations and interactive maps that show pollution distribution. This can be particularly valuable for understanding spatial patterns and identifying pollution hotspots. That in return, can be leverage by the policy makers to make informed decisions regarding pollution control and environmental protection measures. The dataset can help identify areas in need of regulation and the effectiveness of existing policies. Last and most importantly, a visualization dashboard derived from this dataset will be useful for informing the general public about pollution levels in their local areas. It can help raise awareness and drive community engagement in environmental issues.

### Novelty of this dataset

It offers extensive data on pollution distribution across two critically important and diverse regions—IGP and Africa—where pollution monitoring has historically been challenging due to limited infrastructure and data availability.
The dataset has the potential to be transformed as longitudinal data for long-term analysis, enabling the study of pollution trends over an extended period. 
Last, this dataset is processed and ready to be integrated into cloud-based workflows, making it easily accessible for a wide audience, including researchers, developers, and the general public.

### Licensing

This dataset is released under a Creative Commons (CC) license, allowing for broad use while ensuring proper attribution.










