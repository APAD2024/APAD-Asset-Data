# **Cement Plants in the Indo-Gangetic Plain (IGP)**

<img width="770" height="344" alt="{CB7731C1-77C7-462B-9A4F-D09BEA172298}" src="https://github.com/user-attachments/assets/12b171c9-2138-487d-922c-385bfa22baa5" />

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

This dataset provides an asset-level geospatial inventory of **cement production facilities across the Indo-Gangetic Plain (IGP)**, covering:

- Bangladesh  
- India  
- Pakistan  

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Plant type (e.g., grinding / integrated where available)
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
| type | Facility type (grinding / integrated) |
| fuel | Primary fuel used (if available) |
| region | Administrative region |
| country | Country |
| status | Operational status |
| capacity | Production capacity (tonnes/year) |
| emfpm10 | PM10 emission factor (tonnes pollutant / tonne cement) |
| pm10 | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (tonnes pollutant / tonne cement) |
| pm25 | Annual PM2.5 emissions (tonnes/year) |
| emfso2 | SO2 emission factor (tonnes pollutant / tonne cement) |
| so2 | Annual SO2 emissions (tonnes/year) |
| emfnox | NOx emission factor (tonnes pollutant / tonne cement) |
| nox | Annual NOx emissions (tonnes/year) |

---

## Production Basis

Production is based on **installed cement capacity**:

**Production_year = capacity (tonnes/year)**

Where utilization rates are unavailable, the dataset assumes **capacity-based annual production**.

---

## Emission Factors

The following emission factors are applied using a **clinker factor**:

**Clinker factor = 0.95**  
(defined as the ratio of clinker mass to cement mass)

The table below provides:

- EF_clinker (g/tonne clinker or activity basis)
- EF_cement (g/tonne cement) after applying clinker factor
- EF_cement in tonnes pollutant per tonne cement (t/t)

### Emission Factor Table (Sheet1)

| Pollutant | EF_clinker | Unit | Type | Clinker factor | EF_cement (g/tonne cement) | EF_cement (t pollutant / t cement) | Notes |
|----------|------------|------|------|----------------|-----------------------------|------------------------------------|------|
| PM2.5 | 130 | g/tonne | Grinding | 0.95 | 123.5 | 0.0001235 | |
| SO2** | 810 | g/tonne | Grinding | 0.95 | 769.5 | 0.0007695 | |
| NOx** | 520 | g/tonne | Grinding | 0.95 | 494.0 | 0.0004940 | |
| PM10 | 234 | g/tonne | Grinding | 0.95 | 222.3 | 0.0002223 | |
| TSP | 260 | g/tonne | Grinding | 0.95 | 247.0 | 0.0002470 | |
| BC | 3 | g/tonne | Grinding | 0.95 | 2.85 | 0.00000285 | |

\* Clinker factor: ratio of clinker mass to cement mass  
\** Median values from Best Available Techniques (BAT)

---

## Emission Estimation

### Annual Emissions (preferred using t/t factors)

If the emission factor is stored as:

**EF_cement = tonnes pollutant / tonne cement**

Then:

**Emissions (tonnes/year) = EF_cement (t/t) × capacity (t/year)**

Example:

If PM10 EF_cement = 0.0002223 (t/t) and capacity = 1,000,000 t/yr:

PM10 = 0.0002223 × 1,000,000  
PM10 = 222.3 tonnes/year

---

### Optional conversion (if using g/tonne factors)

If emission factor is in g/tonne cement:

**Emissions (tonnes/year) = EF (g/t) × capacity (t/yr) ÷ 1,000,000**

(1,000,000 converts grams to tonnes)

---
## Data Processing Workflow

1. Acquisition of plant-level capacity and unit data
2. Spatial verification and coordinate validation
3. Calculation of annual production
4. Application of standardized emission factors
5. Export to CSV, GeoJSON, and XLSX formats
---

## References

- EMEP/EEA Guidebook 2023 (PM2.5, PM10, TSP, BC):  
  https://www.eea.europa.eu/en/analysis/publications/emep-eea-guidebook-2023/part-b-sectoral-guidance-chapters/2-industrial-processes-and-product-use/2-a-mineral-products/2-a-1-cement-production-2023/@@download/file  

- Best Available Techniques (BAT) for SO2 and NOx (UNECE, 2020):  
  https://unece.org/fileadmin/DAM/env/documents/2020/AIR/WGSR/TFTEI_Cement_final_document-december-2020.pdf  

---

## Citation

If you use this dataset:

APAD (2025).  
*Cement Plants Emissions Dataset – Indo-Gangetic Plain (IGP).*  

### **License**

This dataset is released under:

* [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)
* [![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)

You are free to use, share, remix, and build upon the data with attribution.
