
# Coal Power Plants in the Indo-Gangetic Plain (IGP)

<img width="784" height="349" alt="{CA05EE8C-426D-4E63-9D08-8140F9DE583B}" src="https://github.com/user-attachments/assets/82553262-a1bf-412d-8b15-561cb8344463" />

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

This dataset provides an asset-level geospatial inventory of **coal-fired power plants across the Indo-Gangetic Plain (IGP)**, covering:

* Bangladesh
* India
* Pakistan

The dataset includes:

* Plant geolocation (EPSG:4326 – WGS 84)
* Installed capacity (MW)
* Unit-level operational status
* Annual electricity production (kWh/year)
* Annual emissions (tonnes/year) for:

  * PM2.5
  * PM10
  * SO2
  * NOx

The objective of this dataset is to support:

* Air quality analysis
* Emission inventory development
* Regulatory assessment
* Climate and health impact modelling

All emissions are calculated using standardized emission factors applied to annual electricity generation.

---

## File Structure

### Available Formats

- `.csv`
- `.geojson`
- `.xlsx`

### Column Names

`id, name, lat, lon, type, fuel, region, country, status, capacities, capacity_power, prod_kw, emfpm10, pm10_t_yr, emfpm25, pm25_t_yr, emfso2, so2_t_yr, emfnox, nox_t_yr`

---

### Field Description

| Field          | Description                   |
| -------------- | ----------------------------- |
| id             | Unique plant identifier       | 
| name           | Power plant name              | 
| lat, lon           | GPS coordinates                    |
| type           | Asset type (coal plant)       |
| fuel           | Primary fuel type (if available) | 
| region         | Administrative region         | 
| country        | Country                       |
| status         | Unit-level operational status |
| capacities     | Individual unit capacities (MW)    | 
| capacity_power | Total installed capacity (MW)  |
| prod_kw        | Annual electricity production (kWh/year   ) |         
| emfpm10        | PM10 emission factor (t pollutant / 1,000 t production equivalent) |
| pm10_t_yr      | Annual PM10 emissions (tonnes/year)         | 
| emfpm25        | PM2.5 emission factor (t pollutant / 1,000 t production equivalent)  |
| pm25_t_yr      | Annual PM2.5 emissions ( tonnes/year)     |
| emfso2         | SO2 emission factor (t pollutant / 1,000 t production equivalent |
| so2_t_yr       | Annual SO2 emissions  ( tonnes/year)        |
| emfnox         | NOx emission factor (t pollutant / 1,000 t production equivalent)          |
| nox_t_yr       | Annual NOx emissions  (tonnes/year)        |

---

## Production Basis

Annual electricity production is calculated using installed capacity:

Electricity Production (kWh/year) =

capacity_power × 1000 × 24 × 365

Where:

* 1000 converts MW to kW
* 24 = hours per day
* 365 = days per year

If capacity factors are applied in future updates:

Production_adj = capacity_power × 1000 × 24 × 365 × CF

Currently, full-capacity annual production is assumed unless specified.

---

## Emission Factors

Emission factors are derived from:

* India Air Quality – Coal Power Plants Emissions
* US EPA – Emissions Inventory Conference

The following normalized emission factors are used:

| Pollutant | EF      | Unit                                        | Notes                      |
| --------- | ------- | ------------------------------------------- | -------------------------- |
| PM2.5     | 0.00019 | t pollutant / 1,000 t production equivalent | Average of 0.16–0.22 g/kWh |
| PM10      | 0.00037 | t pollutant / 1,000 t production equivalent | Average of 0.29–0.45 g/kWh |
| SO2       | 0.0072  | t pollutant / 1,000 t production equivalent | 7.20 g/kWh                 |
| NOx       | 0.0043  | t pollutant / 1,000 t production equivalent | Average of 4.22–4.38 g/kWh |

Equivalent g/kWh values:

* PM2.5: 0.16–0.22 g/kWh
* PM10: 0.29–0.45 g/kWh
* SO2: 7.20 g/kWh
* NOx: 4.22–4.38 g/kWh

---

## Emission Estimation

### Standard Calculation Method

Emissions (tonnes/year) =

(EF (g/kWh) × Electricity Production (kWh/year)) ÷ 1,000,000

Where:

* EF is in grams per kWh
* 1,000,000 converts grams to tonnes

---

### Dataset Implementation Method

In this dataset:

Emissions (tonnes/year) =

EF_normalized × prod_kw

Where:

* EF_normalized is stored in normalized form
* prod_kw is annual electricity production

---

### Example: Barapukuria Power Station

capacity_power = 525 MW

Electricity Production:

525 × 1000 × 24 × 365
= 4,599,000,000 kWh/year

PM10:

0.00037 × 4,599,000,000 ÷ 1,000,000
= 85.0815 tonnes/year

Which matches the dataset value.

---

## Data Processing Workflow

1. Acquisition of plant-level capacity and unit data
2. Spatial verification and coordinate validation
3. Calculation of annual electricity production
4. Application of standardized emission factors
5. Export to CSV, GeoJSON, and XLSX formats

---

## References

- India Air Quality – Coal Power Plants Emissions
[https://www.indiaairquality.info/wp-content/uploads/docs/2014-08-AE-Emissions-Health-Coal-PPs-India.pdf](https://www.indiaairquality.info/wp-content/uploads/docs/2014-08-AE-Emissions-Health-Coal-PPs-India.pdf)

- US EPA – Emissions Inventory Conference

- Global Energy Monitor – Global Coal Plant Tracker

---

## Citation

If you use this dataset:

APAD (2025).
*Coal Power Plants Emissions Dataset – Indo-Gangetic Plain (IGP).*

### **License**

This dataset is released under:

* [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)
* [![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)

You are free to use, share, remix, and build upon the data with attribution.

