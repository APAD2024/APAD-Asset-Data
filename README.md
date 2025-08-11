## Asset-Data Repository Structure

### Repository Overview

This repository contains data related to various assets that contribute to pollution, categorized pollution data, and population exposure risk calculated based on these assets. The repository is organized into three main folders:

1. **Asset Data**
2. **Pollution Data**
3. **Population Exposure Risk**

### Study Area Overview

The study focuses on two major regions: the Indo-Gangetic Plain (IGP) in South Asia extending until Nepal and selected countries in Africa. The study area includes several countries and their respective areas, as detailed below.

## **Indo-Gangetic Plain (IGP) - South Asia**

### Countries Included:

| **Country**   | **Area Covered (sq km)** |
|---------------|--------------------------|
| **India**     | xx Km²            |
| **Bangladesh**| xx Km²              |
| **Pakistan**  | xx Km²              |
| **Nepal**     | xx Km²              |

### Total Area Covered in IGP: **xxxx Km²**

## **Study Areas in Africa**

### Countries Included:

| **Country**   | **Area Covered (sq km)** |
|---------------|--------------------------|
| **DRC**       | 2,345,000 Km²            |
| **Ghana**     | 238,533 Km²              |
| **Nigeria**   | 923,768 Km²              |
| **Uganda**    | 241,551 Km²              |
| **Kenya**     | 581,309 Km²              |

### Total Area Covered in parts of Africa: **4,330,161 Km²**

## **Asset Data**

This folder contains subfolders for each asset type that contributes to pollution. Each subfolder contains data specific to that asset, such as its geographical location, operational details, capacity, and other relevant information.

## Asset Data

This folder contains subfolders for each asset type that contributes to pollution. Each subfolder contains data specific to that asset, such as its geographical location, operational details, name-plate capacity, and other relevant information.

- `Asset Data/`
  - **Brick Kiln**: A type of kiln used for burning bricks, releasing pollutants such as particulate matter (PM), carbon monoxide (CO), and volatile organic compounds (VOCs) into the atmosphere, contributing to air pollution and negative health effects. 
  $$ 
  PM_{2.5} = 10-30 \space \mu g/m^3 
  $$
  ![Brick Kiln](https://example.com/brick-kiln.jpg)
  - **Boilers**: Devices used for generating steam or hot water, emitting pollutants like particulate matter (PM), sulfur dioxide (SO2), and nitrogen oxides (NOx) due to combustion of fossil fuels, contributing to air pollution and acid rain. 
  $$ 
  SO_2 = 10-50 \space ppb 
  $$
  ![Boilers](https://example.com/boilers.jpg)
  - **Cement Plants**: Industrial facilities that produce cement, releasing large amounts of particulate matter (PM), including PM2.5, and greenhouse gases like carbon dioxide (CO2) into the atmosphere, contributing to air pollution and climate change. 
  $$ 
  CO_2 = 500-1000 \space g/kg 
  $$
  ![Cement Plants](https://example.com/cement-plants.jpg)
  - **Steel Plants**: Industrial facilities that produce steel, emitting pollutants like particulate matter (PM), carbon monoxide (CO), and volatile organic compounds (VOCs) into the atmosphere, contributing to air pollution and negative health effects. 
  $$ 
  PM_{10} = 20-50 \space \mu g/m^3 
  $$
  ![Steel Plants](https://example.com/steel-plants.jpg)
  - **Marble and Granite Processing**: Facilities that process marble and granite, releasing particulate matter (PM) and other pollutants into the atmosphere, contributing to air pollution and negative health effects. 
  $$ 
  PM_{2.5} = 5-15 \space \mu g/m^3 
  $$
  ![Marble and Granite Processing](https://example.com/marble-granite-processing.jpg)
  - **Transport**: A sector contributing to air pollution through emissions from vehicles and other transportation modes, releasing pollutants like particulate matter (PM), carbon monoxide (CO), and volatile organic compounds (VOCs) into the atmosphere. 
  $$ 
  CO = 100-500 \space ppb 
  $$
  ![Transport](https://example.com/transport.jpg)
  - **Open burning sites**: Areas where waste is burned, releasing pollutants like particulate matter (PM), carbon monoxide (CO), and volatile organic compounds (VOCs) into the atmosphere, contributing to air pollution and negative health effects. 
  $$ 
  VOCs = 10-50 \space ppb 
  $$
  ![Open burning sites](https://example.com/open-burning-sites.jpg)
  - **Coal Plants**: Industrial facilities that burn coal to generate electricity or heat, emitting pollutants like particulate matter (PM), sulfur dioxide (SO2), and nitrogen oxides (NOx) into the atmosphere, contributing to air pollution, acid rain, and climate change. 
  $$ 
  NO_x = 50-100 \space ppb 
  $$
  ![Coal Plants](https://example.com/coal-plants.jpg)
  - **Oil Refineries**: Industrial facilities that refine oil, releasing pollutants like particulate matter (PM), sulfur dioxide (SO2), and nitrogen oxides (NOx) into the atmosphere, contributing to air pollution and negative health effects. 
  $$ 
  SO_2 = 20-50 \space ppb 
  $$
  ![Oil Refineries](https://example.com/oil-refineries.jpg)
  - **Gas Processing**: Facilities that process natural gas, releasing pollutants like methane (CH4) and other pollutants into the atmosphere, contributing to climate change and air pollution. 
  $$ 
  CH_4 = 10-50 \space ppb 
  $$
  ![Gas Processing](https://example.com/gas-processing.jpg)
  - **Pulp and Paper Mills**: Industrial facilities that produce pulp and paper, emitting pollutants like particulate matter (PM), sulfur dioxide (SO2), and volatile organic compounds (VOCs) into the atmosphere, contributing to air pollution and negative health effects. 
  $$ 
  PM_{10} = 10-30 \space \mu g/m^3 
  $$
  ![Pulp and Paper Mills](https://example.com/pulp-paper-mills.jpg)
  - **Chemical Plants**: Industrial facilities that produce chemicals, releasing pollutants like particulate matter (PM), volatile organic compounds (VOCs), and other pollutants into the atmosphere, contributing to

## **Pollution Data**

This folder contains data on various pollutants. The subfolders are organized based on the type of pollutant. Each subfolder contains data related to the specific pollutant, including its concentration levels across different regions.

- `Pollution Data/`
  - **PM2.5**: Particulate matter with a diameter of 2.5 micrometers or less, contributing to air pollution and health risks. ![PM2.5](https://example.com/pm25.jpg)
  - **PM10**: Particulate matter with a diameter of 10 micrometers or less, contributing to air pollution and health risks. ![PM10](https://example.com/pm10.jpg)
  - **SO2**: Sulfur dioxide, a gas contributing to air pollution and acid rain. ![SO2](https://example.com/so2.jpg)
  - **NOx**: Nitrogen oxides, gases contributing to air pollution and ground-level ozone formation. ![NOx](https://example.com/nox.jpg)

## **Population Exposure Risk**

This folder contains data related to the population exposure risk to pollutants, calculated based on the assets listed in the Asset Data folder. The calculations use a decay function to estimate the risk levels. A README file is included in this folder to explain the decay function and the calculation process.

- `Population Exposure Risk/`
  - `README.md` (Explanation of the decay function and risk calculation methodology)

### How can this dataset be used?

This pollution assets dataset is designed to support a wide range of applications related to environmental monitoring and analysis:

* Climate Researchers can utilize this data to study pollution trends over time across the Indo-Gangetic Plain (IGP) and Africa, providing insights into how these regions are impacted by various pollution sources.
* Geographic Information System (GIS) developers can use this dataset to create detailed visualizations and interactive maps that show pollution distribution.
* Policy makers can use this dataset to make informed decisions regarding pollution control and environmental protection measures.
* The dataset can help identify areas in need of regulation and the effectiveness of existing policies.
* A visualization dashboard derived from this dataset will be useful for informing the general public about pollution levels in their local areas.

### Novelty of this dataset

* It offers extensive data on pollution distribution across two critically important and diverse regions—IGP and Africa—where pollution monitoring has historically been challenging due to limited infrastructure and data availability.
* The dataset has the potential to be transformed as longitudinal data for long-term analysis, enabling the study of pollution trends over an extended period.
* This dataset is processed and ready to be integrated into cloud-based workflows, making it easily accessible for a wide audience, including researchers, developers, and the general public.

### Licensing

This dataset is released under a Creative Commons (CC) license, allowing for broad use while ensuring proper attribution.

### Data Sources:

* Administrative Boundaries - Global Administrative Areas (2024). University of California, Berkely. [digital geospatial data]. Available online: https://gadm.org/data.html [license](https://gadm.org/license.html).
* Pollution Data (PM 2.5) - Atmospheric Composition Analysis Group (V6.GL.02 version) 0.01 x 0.01 [data](https://sites.wustl.edu/acag/datasets/surface-pm2-5/#V6.GL.02):
Shen, S., Li, C., van Donkelaar, A., Jacobs, N., Wang, C., Martin, R. V. “Enhancing Global Estimation of Fine Particulate Matter Concentrations by Including Geophysical a Priori Information in Deep Learning.” (2024) ACS ES&T Air. DOI: 10.1021/acsestair.3c00054
