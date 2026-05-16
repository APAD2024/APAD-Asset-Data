# **Paper and Pulp Mills in Africa**

---

# **Table of Contents**

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Citation](#citation)

---

## Overview

This dataset provides an asset-level geospatial inventory of **paper and pulp production facilities across Africa**.

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Facility type (e.g., pulp mill, paper mill, integrated)
- Primary fuel used
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


## File Structure

### Available Formats

- `.csv`

### Column Names

`id, name, lat, lon, type, fuel, region, country, status, capacity_tonnes, emfpm10, pm10_t_yr, emfpm25, pm25_t_yr, emfso2, so2_t_yr, emfnox, nox_t_yr, source`

### Column Description

| Field | Description |
|-------|-------------|
| id | Unique facility identifier |
| name | Mill name |
| lat, lon | GPS coordinates (WGS 84) |
| type | Facility type (e.g., pulp, paper, integrated) |
| fuel | Primary fuel used |
| region | Administrative region |
| country | Country |
| status | Operational status |
| capacity_tonnes | Production capacity (tonnes/year) |
| emfpm10 | PM10 emission factor (tonnes pollutant / tonne product) |
| pm10_t_yr | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (tonnes pollutant / tonne product) |
| pm25_t_yr | Annual PM2.5 emissions (tonnes/year) |
| emfso2 | SO2 emission factor (tonnes pollutant / tonne product) |
| so2_t_yr | Annual SO2 emissions (tonnes/year) |
| emfnox | NOx emission factor (tonnes pollutant / tonne product) |
| nox_t_yr | Annual NOx emissions (tonnes/year) |
| source | Data source or reference for facility record |

## Citation

If you use this dataset:

APAD (2025).
*Paper and Pulp Mills Emissions Dataset – Africa.*

### **License**

This dataset is released under:

* [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)
* [![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)

You are free to use, share, remix, and build upon the data with attribution.
