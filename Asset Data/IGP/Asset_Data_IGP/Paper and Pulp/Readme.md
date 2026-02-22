# Paper & Pulp Plants in the Indo-Gangetic Plain (IGP)


<img width="790" height="344" alt="{D97685D1-35BC-4DC0-BE9A-139FB402BA34}" src="https://github.com/user-attachments/assets/368efafa-0bb3-45ed-bf5a-95a423668d66" />

---

## Table of Contents

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

This dataset provides an asset-level geospatial inventory of **paper and pulp production facilities across the Indo-Gangetic Plain (IGP)**, covering:

- Bangladesh  
- India  
- Pakistan  

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Facility type (Paper / Paper & Pulp)
- Operational status
- Annual production capacity (tonnes/year)
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

All emissions are calculated using:

**Emissions = Production Capacity × Emission Factor**

---

## File Structure

### Available Formats

- `.csv`
- `.geojson`
- `.xlsx`

### Column Names

`id, name, lat, lon, type, fuel, region, country, status, capacity_tonnes, emfpm10, pm10_t_yr, emfpm25, pm25_t_yr, emfso2, so2_t_yr, emfnox, nox_t_yr`

---

### Field Description

| Field | Description |
|-------|------------|
| id | Unique plant identifier |
| name | Plant name |
| lat, lon | GPS coordinates |
| type | Facility type (Paper / Paper & Pulp) |
| fuel | Primary fuel (if available) |
| region | Administrative region |
| country | Country |
| status | Operational status |
| capacity_tonnes | Annual production capacity (tonnes/year)|
| emfpm10 | PM10 emission factor (t pollutant / t production) |
| pm10_t_yr | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (t pollutant / t production) |
| pm25_t_yr | Annual PM2.5 emissions (tonnes/year)| 
| emfso2 | SO2 emission factor (t pollutant / t production)| 
| so2_t_yr | Annual SO2 emissions (tonnes/year)|
| emfnox | NOx emission factor (t pollutant / t production) |
| nox_t_yr | Annual NOx emissions (tonnes/year) | 

---

## Production Basis

Production capacity is expressed in **tonnes per year**.

Capacity values were derived from:

- Quader (2012) for Bangladesh mills  
- Supplementary verification via public sources and industry data  

Where required, **Metric Ton (MT)** values were converted to **Tonnes (t)**:

1 MT = 1 tonne  

Production basis used in emission calculation:

Production_year = capacity_tonnes

---

## Emission Factors

Emission factors are derived from:

- EMEP/EEA Guidebook 2023  
- Bordado & Gomes (1997)  
- Empirical scaling relationships  

Tier 2 emission factors (EMEP) were used for both:

- Kraft process  
- Acid Sulfide process  

All factors originally reported in **kg/Mg** were converted:

1 Mg = 1 tonne  

Final normalized factors are expressed as:

**tonnes pollutant / tonne production**

---

### Paper & Pulp (General)

| Pollutant | EF | Unit | EF Normalized (t/t) | Notes |
|------------|----|------|--------------------|------|
| PM2.5 | 0.975 | tonne/000 tonnes | 0.000975 | Tier 2 |
| SO2 | 5 | tonne/000 tonnes | 0.005 | |
| NOx | 2.5 | tonne/000 tonnes | 0.0025 | |
| PM10 | 1.3 | tonne/000 tonnes | 0.0013 | |

---

### Paper Only (Empirical Scaling Applied)

In Bordado & Gomes (1997), only total PM = 0.315 kg/Mg was reported.

Using empirical relationships:

PM10 = 0.6 × PM  
PM2.5 = 0.65 × PM10  

Final normalized values:

| Pollutant | EF | Unit | EF Normalized (t/t) |
|------------|----|------|--------------------|
| PM2.5 | 0.12285 | tonne/000 tonnes | 0.00012285 |
| SO2 | 0.43 | tonne/000 tonnes | 0.00043 |
| NOx | 0.53 | tonne/000 tonnes | 0.00053 |
| PM10 | 0.189 | tonne/000 tonnes | 0.000189 |

---

## Emission Estimation

### Standard Formula

Emissions (tonnes/year) =  

EF_normalized × capacity_tonnes  

Where:

- EF_normalized = tonnes pollutant / tonne production  
- capacity_tonnes = tonnes/year  

---

### Example: Amber Super Paper Ltd

capacity_tonnes = 16,093.74  

PM10 EF = 0.000189  

PM10 =  
0.000189 × 16,093.74  

= 3.0417 tonnes/year  

Which matches the dataset value.

---

## Data Processing Workflow

1. Acquisition of plant-level capacity and unit data
2. Spatial verification and coordinate validation
3. Calculation of annual production
4. Application of standardized emission factors
5. Export to CSV, GeoJSON, and XLSX formats

--- 

## References

- EMEP/EEA Guidebook 2023 – Pulp & Paper  
https://www.eea.europa.eu/en/analysis/publications/emep-eea-guidebook-2023/part-b-sectoral-guidance-chapters/2-industrial-processes-and-product-use/2-h-other-industry-production/2-h-1-pulp-and/@@download/file  

- Bordado, J. C., & Gomes, J. F. (1997).  
Pollutant atmospheric emissions from Portuguese Kraft pulp mills.  
Science of the Total Environment, 208(1–2), 139–143.

### Data Sources

Capacity data for Bangladesh:

- Quader, M. (2012).  
Paper Sector in Bangladesh: Challenges and Scope of Development.  
Journal of Chemical Engineering, 26(1), 41–46.  
https://doi.org/10.3329/jce.v26i1.10181  

- Additional capacity verification via public industry records.

---

## Citation

If you use this dataset:

APAD (2025).  
*Paper & Pulp Plants Emissions Dataset – Indo-Gangetic Plain (IGP).*  

### **License**

This dataset is released under:

* [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)
* [![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)

You are free to use, share, remix, and build upon the data with attribution.
