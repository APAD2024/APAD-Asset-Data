# **Coal Plants in Africa**

---

# **Table of Contents**

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Citation](#citation)

---

## Overview

This dataset provides an asset-level geospatial inventory of **coal-fired power plants across Africa**.

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Plant type and fuel type
- Operational status
- Installed capacity (MW)
- Production estimates (kWh/year)
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

**Emissions = Energy Generated × Emission Factor**

---

## File Structure

### Available Formats

- `.csv`
- `.geojson`

### Column Names

`id, name, lat, lon, type, fuel, region, country, status, capacities, capacity_power, prod_kw, emfpm10, pm10_t_yr, emfpm25, pm25_t_yr, emfso2, so2_t_yr, emfnox, nox_t_yr, source`

### Column Description

| Field | Description |
|-------|-------------|
| id | Unique facility identifier |
| name | Plant name |
| lat, lon | GPS coordinates (WGS 84) |
| type | Plant type (e.g., subcritical, supercritical) |
| fuel | Primary fuel (coal) |
| region | Administrative region |
| country | Country |
| status | Operational status |
| capacities | Capacity description or unit breakdown |
| capacity_power | Installed capacity (MW) |
| prod_kw | Estimated annual electricity production (kWh/year) |
| emfpm10 | PM10 emission factor (g/kWh) |
| pm10_t_yr | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (g/kWh) |
| pm25_t_yr | Annual PM2.5 emissions (tonnes/year) |
| emfso2 | SO2 emission factor (g/kWh) |
| so2_t_yr | Annual SO2 emissions (tonnes/year) |
| emfnox | NOx emission factor (g/kWh) |
| nox_t_yr | Annual NOx emissions (tonnes/year) |
| source | Data source or reference for facility record |


## Citation

If you use this dataset:

APAD (2025).
*Coal Plants Emissions Dataset – Africa.*

### **License**

This dataset is released under the **Open Data Commons Attribution License v1.0 (ODC-BY 1.0)**.

[![License: ODC-BY 1.0](https://img.shields.io/badge/License-ODC__BY_1.0-brightgreen.svg)](https://opendatacommons.org/licenses/by/1-0/)

You are free to use, share, remix, and build upon the data with attribution.
