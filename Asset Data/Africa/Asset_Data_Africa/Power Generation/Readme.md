# **Power Generation Facilities in Africa**

---

# **Table of Contents**

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Citation](#citation)

---

## Overview

This dataset provides an asset-level geospatial inventory of **power generation facilities across Africa**, covering thermal plants burning fossil fuels such as furnace oil, natural gas, diesel, and coal.

The dataset includes:

- Plant geolocation (EPSG:4326 – WGS 84)
- Plant type and primary fuel
- Operational status
- Installed capacity (MW) and capacity factor
- Estimated fuel volume consumed
- Annual emissions (tonnes/year) for:
  - PM2.5
  - PM10
  - SO2
  - NOx
  - CO

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

- `.csv` — all plants in a single table
- `.geojson` — the same plants split by fuel: `power_africa_gas`, `power_africa_oil`, `power_africa_biofuel`

### Column Names

`id, name, lat, lon, type, fuel, state, country, status, capacity_power, units, capacity_factor, fuel_volume, unit, emfpm10, pm10_t_yr, emfpm25, pm25_t_yr, emfso2, so2_t_yr, emfnox, nox_t_yr, emfco, co_t_yr, source`

### Column Description

| Field | Description |
|-------|-------------|
| id | Unique facility identifier |
| name | Plant name |
| lat, lon | GPS coordinates (WGS 84) |
| type | Plant type (e.g., thermal, gas turbine, diesel generator) |
| fuel | Primary fuel (e.g., furnace oil, natural gas, diesel, coal) |
| state | Sub-national administrative unit |
| country | Country |
| status | Operational status |
| capacity_power | Installed capacity (MW) |
| units | Unit label for capacity_power (e.g., MW) |
| capacity_factor | Fraction of time plant operates at full capacity (0–1) |
| fuel_volume | Estimated annual fuel consumption |
| unit | Unit for fuel_volume (e.g., tonnes, m³) |
| emfpm10 | PM10 emission factor (g/kWh) |
| pm10_t_yr | Annual PM10 emissions (tonnes/year) |
| emfpm25 | PM2.5 emission factor (g/kWh) |
| pm25_t_yr | Annual PM2.5 emissions (tonnes/year) |
| emfso2 | SO2 emission factor (g/kWh) |
| so2_t_yr | Annual SO2 emissions (tonnes/year) |
| emfnox | NOx emission factor (g/kWh) |
| nox_t_yr | Annual NOx emissions (tonnes/year) |
| emfco | CO emission factor (g/kWh) |
| co_t_yr | Annual CO emissions (tonnes/year) |
| source | Data source or reference for facility record |

---


## Citation

If you use this dataset:

APAD (2025).
*Power Generation Facilities Emissions Dataset – Africa.*

### **License**

This dataset is released under the **Open Data Commons Attribution License v1.0 (ODC-BY 1.0)**.

[![License: ODC-BY 1.0](https://img.shields.io/badge/License-ODC__BY_1.0-brightgreen.svg)](https://opendatacommons.org/licenses/by/1-0/)

You are free to use, share, remix, and build upon the data with attribution.
