# Asset-Data Repository

### Repository Overview

This repository contains data related to various assets contributing to pollution and population exposure risk calculated based on these assets. The repository is organized into three main folders:

1. **Asset Data**
2. **Asset Data CSVs**
3. **Population Exposure Risk**

---

### Folder Structure

1. **Asset Data**
   - Contains subfolders for each asset type contributing to pollution.
   - Each subfolder includes data specific to that asset, such as geographical location, operational details, name-plate capacity, and other relevant information.

   - **Subfolders:**
     - **Africa**: Data specific to pollution assets located in African countries.
     - **IGP**: Data specific to pollution assets located in the Indo-Gangetic Plain.
     - **assets_adm_3**: Administrative data related to asset locations and classifications.

2. **Asset Data CSVs**
   - Contains all CSV files for the assets, providing detailed information on each asset type, including emissions data and operational metrics.

3. **Population Exposure Risk**
   - Contains data related to the population exposure risk to pollutants, calculated based on the assets listed in the Asset Data folder.
   - Includes a README file explaining the decay function and the calculation process.
   - Will be populated with exposure risk maps in the future.

---

### Study Area Overview

The study focuses on two major regions: the Indo-Gangetic Plain (IGP) in South Asia extending until Nepal and selected countries in Africa. The study area includes several countries and their respective areas, as detailed below.

## **Indo-Gangetic Plain (IGP) - South Asia**

### Countries Included:

| **Country**   | **Area Covered (sq km)** |
|---------------|--------------------------|
| **India**     | xx Km²                   |
| **Bangladesh**| xx Km²                   |
| **Pakistan**  | xx Km²                   |
| **Nepal**     | xx Km²                   |

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

---

## **Asset Data**

This folder contains subfolders for each asset type that contributes to pollution. Each subfolder contains data specific to that asset, such as its geographical location, operational details, name-plate capacity, and other relevant information.

### Asset Types

- **Brick Kiln**: Emits pollutants such as particulate matter (PM), carbon monoxide (CO), and volatile organic compounds (VOCs).
- **Boilers**: Generates steam or hot water, emitting pollutants like PM, sulfur dioxide (SO2), and nitrogen oxides (NOx).
- **Cement Plants**: Produces cement, releasing particulate matter (PM) and greenhouse gases like carbon dioxide (CO2).
- **Steel Plants**: Produces steel, emitting pollutants like PM, carbon monoxide (CO), and VOCs.
- **Marble and Granite Processing**: Releases particulate matter (PM) and other pollutants.
- **Transport**: Contributes to air pollution through emissions from vehicles.
- **Open Burning Sites**: Releases pollutants from waste burning.
- **Coal Plants**: Emits pollutants like PM, SO2, and NOx.
- **Oil Refineries**: Releases pollutants like PM, SO2, and NOx.
- **Gas Processing**: Emits methane (CH4) and other pollutants.
- **Pulp and Paper Mills**: Produces pulp and paper, emitting PM, SO2, and VOCs.

---

## **Asset Data CSVs**

This folder contains all CSV files for the assets, providing detailed information on each asset type, including emissions data and operational metrics.

---

## **Population Exposure Risk**

This folder contains data related to the population exposure risk to pollutants, calculated based on the assets listed in the Asset Data folder. The calculations use a decay function to estimate the risk levels. A README file is included in this folder to explain the decay function and the calculation process.

### How can this dataset be used?

This pollution assets dataset supports a wide range of applications related to environmental monitoring and analysis:

- **Climate Researchers**: Study pollution trends over time across the IGP and Africa.
- **GIS Developers**: Create visualizations and interactive maps showing pollution distribution.
- **Policy Makers**: Make informed decisions regarding pollution control and environmental protection measures.
- **Public Awareness**: Inform the general public about pollution levels in their local areas.

---

### Novelty of this dataset

- **Extensive Coverage**: Offers comprehensive data on pollution distribution across the IGP and Africa, regions where pollution monitoring has historically been challenging due to limited infrastructure and data availability.
- **Cloud Integration Ready**: The dataset is processed and ready to be integrated into cloud-based workflows, making it easily accessible for a wide audience, including researchers, developers, and the general public.

---

### Licensing
This dataset is released under a Creative Commons (CC) license, allowing for broad use while ensuring proper attribution.

---

### Data Sources

 - **Administrative Boundaries**: Global Administrative Areas (2024). University of California, Berkeley. [digital geospatial data]. Available online: GADM license.
 - **Pollution Data (PM 2.5)**: Atmospheric Composition Analysis Group (V6.GL.02 version) 0.01 x 0.01 data: Shen, S., Li, C., van Donkelaar, A., Jacobs, N., Wang, C., Martin, R. V. “Enhancing Global Estimation of Fine Particulate Matter Concentrations by Including Geophysical a Priori Information in Deep Learning.” (2024) ACS ES&T Air. DOI: 10.1021/acsestair.3c00054.

---

### Data Collection Process

The data collection process for this repository involves several key steps, utilizing advanced AI models and collaboration with various organizations to ensure comprehensive and accurate data:

- **Data Sourcing**:
Data is sourced from reputable organizations and research groups, including Climate Trace and GEM (Global Environmental Monitoring). These sources provide foundational data on pollution assets and environmental conditions.
- **Data Integration**:
Our team processes and integrates the sourced data, adding value by refining and enhancing the datasets. This includes correcting inconsistencies, filling gaps, and ensuring that the data is relevant to the study areas.
- **Quality Assurance**:
A rigorous quality assurance process is implemented to verify the accuracy and reliability of the data. This includes cross-referencing with other datasets, and peer reviews.
- **Data Hosting**:
Once the data is processed and validated, it is hosted on our dashboard, making it accessible for researchers, policymakers, and the general public. The dashboard provides interactive visualizations and tools for users to explore the data effectively.
- **Continuous Updates**:
The dataset is continuously updated as new data becomes available or as methodologies improve. This ensures that users have access to the most current and relevant information regarding pollution and exposure risks.

---

For any questions or further information, please refer to the contact details provided in the repository or reach out to our team directly.
