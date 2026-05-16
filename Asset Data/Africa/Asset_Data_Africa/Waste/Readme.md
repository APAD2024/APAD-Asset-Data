# **Waste Facilities in Africa**

---

# **Table of Contents**

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Citation](#citation)

---

## Overview

This dataset provides an asset-level geospatial inventory of **waste management facilities across Africa**, including waste incineration plants, open dumpsites, and controlled landfills with combustion activity.

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Facility type (e.g., incineration, open burning, landfill)
- Operational status
- Waste throughput capacity (tonnes/year)
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

**Emissions = Waste Throughput × Emission Factor**

---

## File Structure

### Available Formats

- `.geojson`

### Column Names

`id, name, type, fuel, region, country, status, capacity_tonnes, emfpm10, pm10_t_yr, emfpm25, pm25_t_yr, emfso2, so2_t_yr, emfnox, nox_t_yr, source`

### Column Description

| Field | Description |
|-------|-------------|
| id | Unique facility identifier |
| name | Facility name |
| type | Facility type (e.g., incineration, open burning, landfill) |
| fuel | Waste type or fuel category |
| region | Administrative region |
| country | Country |
| status | Operational status |
| capacity_tonnes | Waste throughput capacity (tonnes/year) |
| emfpm10 | PM10 emission factor (tonnes pollutant / tonne waste) |
| pm10_t_yr | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (tonnes pollutant / tonne waste) |
| pm25_t_yr | Annual PM2.5 emissions (tonnes/year) |
| emfso2 | SO2 emission factor (tonnes pollutant / tonne waste) |
| so2_t_yr | Annual SO2 emissions (tonnes/year) |
| emfnox | NOx emission factor (tonnes pollutant / tonne waste) |
| nox_t_yr | Annual NOx emissions (tonnes/year) |
| source | Data source or reference for facility record |


## Citation

If you use this dataset:

APAD (2025).
*Waste Facilities Emissions Dataset – Africa.*

### **License**

This dataset is released under:

* [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)
* [![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)

You are free to use, share, remix, and build upon the data with attribution.
