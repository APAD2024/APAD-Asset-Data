# **Steel Plants in the Indo-Gangetic Plain (IGP)**

<img width="757" height="342" alt="{F328190B-EF8F-41E2-BA17-0095BA96FFA5}" src="https://github.com/user-attachments/assets/0b7060e3-cd6d-422b-8ee4-46a59f78c2c6" />

---

# **Table of Contents**

1. [Overview](#overview)  
2. [File Structure](#file-structure)  
3. [Production Basis](#production-basis)  
4. [Emission Factors](#emission-factors)  
5. [Emission Estimation](#emission-estimation)  
6. [Data Processing Workflow](#data-processing-workflow)  
7. [References](#references)  
8. [Citation](#citation)  

---

## Overview

This dataset provides an asset-level geospatial inventory of **steel production facilities across the Indo-Gangetic Plain (IGP)**, covering:

- Bangladesh  
- India  
- Pakistan  

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Facility type (Integrated / Secondary steel / Electric Arc Furnace where available)
- Operational status
- Production capacity (tonnes/year)
- Annual emissions (tonnes/year) for:
  - PM2.5  
  - PM10  
  - SO2  
  - NOx  

The objective of this dataset is to support:

* Air quality analysis
* Emission inventory development
* Regulatory assessment
* Climate and health impact modelling

Emissions are calculated using:

**Emissions = Production × Emission Factor**

---

## File Structure

### Available Formats

- `.csv`
- `.geojson`
- `.xlsx`

### Column Names

`id, name, lat, lon, type, fuel, region, country, status, capacity, emfpm10, pm10, emfpm25, pm25, emfso2, so2, emfnox, nox`

### Column Description

| Field | Description |
|-------|------------|
| id | Unique facility identifier |
| name | Plant name |
| lat, lon | GPS coordinates |
| type | Facility type |
| fuel | Primary fuel |
| region | Administrative region |
| country | Country |
| status | Operational status |
| capacity | Production capacity (tonnes/year) |
| emfpm10 | PM10 emission factor (t pollutant / t steel) |
| pm10 | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (t pollutant / t steel) |
| pm25 | Annual PM2.5 emissions (tonnes/year) |
| emfso2 | SO2 emission factor (t pollutant / t steel) |
| so2 | Annual SO2 emissions (tonnes/year) |
| emfnox | NOx emission factor (t pollutant / t steel) |
| nox | Annual NOx emissions (tonnes/year) |

---

## Production Basis

Production is based on **installed crude steel production capacity**:

**Production_year = capacity (tonnes/year)**  

Where plant-specific utilization rates are unavailable, the dataset assumes **capacity-based annual production**.

Capacity values were harmonized to tonnes/year.

---

## Emission Factors

Emission factors are derived from:

Zhang et al. (2023)  
*Iron and Steel Industry Emissions: A Global Analysis of Trends and Drivers*  
Environmental Science & Technology, 57(43)

The study reports **average emission intensities for developing countries**:

- 2.51 tonnes PM2.5 per 1,000 tonnes crude steel  
- 1.44 tonnes SO2 per 1,000 tonnes crude steel  
- 0.47 tonnes NOx per 1,000 tonnes crude steel  

---

### Normalized Emission Factors

Converted to:

**tonnes pollutant / tonne steel**

| Pollutant | EF (tonne/000 tonnes) | EF Normalized (t/t) | Notes |
|------------|----------------------|---------------------|------|
| PM2.5 | 2.51 | 0.00251 | |
| SO2 | 1.44 | 0.00144 | |
| NOx | 0.47 | 0.00047 | |
| PM10* | 3.81 | 0.00381 | Estimated using global PM10:PM2.5 ratio (1.5185 × PM2.5) |

---

### PM10 Estimation Method

PM10 was not directly reported.

It was estimated using:

Global PM10 : PM2.5 ratio = 1.5185  

PM10 EF = 1.5185 × PM2.5 EF  

= 1.5185 × 2.51  
= 3.81 tonne / 1,000 tonnes  

---

## Emission Estimation

### Preferred Method (Normalized Factors)

If EF is expressed as:

**EF_steel = tonnes pollutant / tonne steel**

Then:

**Emissions (tonnes/year) = EF_steel × capacity**

---

### Example

If:

Capacity = 1,000,000 tonnes/year  
PM2.5 EF = 0.00251  

PM2.5 =  
0.00251 × 1,000,000  

PM2.5 = 2,510 tonnes/year  

---

## Data Processing Workflow

1. Acquisition of plant-level steel capacity data  
2. Geospatial validation and coordinate cleaning  
3. Conversion of all capacities to tonnes/year  
4. Application of normalized emission factors (t/t basis)  
5. Estimation of annual emissions  
6. Export to CSV, GeoJSON, and XLSX formats  

---

## References

- Zhang, J., Shen, H., Chen, Y., Meng, J., Li, J., He, J., Guo, P., Dai, R., Zhang, Y., Xu, R., Wang, J., Zheng, S., Lei, T., Shen, G., Wang, C., Ye, J., Zhu, L., Sun, H. Z., Fu, T.-M., Yang, X., Guan, D. & Tao, S. (2023).  
*Iron and Steel Industry Emissions: A Global Analysis of Trends and Drivers.*  
- Environmental Science & Technology, 57(43).  
doi: 10.1021/acs.est.3c05474  

---

## Citation

If you use this dataset:

APAD (2025).  
*Steel Plants Emissions Dataset – Indo-Gangetic Plain (IGP).*  

### **License**

This dataset is released under:

* [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)
* [![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)
