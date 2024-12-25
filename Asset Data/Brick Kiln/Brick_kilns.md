# Brick Kilns in IGP Region Using AI

<div style="background-color: #f0f8ff; color: #333; padding: 20px; border-radius: 10px;">

This repository provides a comprehensive geospatial analysis of brick kiln operations in the Indo-Gangetic Plain (IGP) region (Bangladesh, India, and Pakistan), focusing on their environmental and public health impacts. Using low-resolution satellite imagery, we have mapped and analyzed brick kiln sites, estimating their production and emissions. This dataset represents a pioneering effort to understand the spatial distribution of brick kilns and their contribution to air pollution in the region.

</div>

---

## **Table of Contents**

1. [Overview](#overview)  
2. [Brick Production Calculation](#brick-production-calculation)  
   - [Step 1: Total Production for "n" Kilns](#step-1-total-production-for-n-kilns)  
   - [Step 2: Daily Production per Kiln](#step-2-daily-production-per-kiln)  
   - [Updated Production & Emissions Calculation](#updated-production--emissions-calculation)  
3. [File Structure](#file-structure)  
   - [Main Dataset](#1-main-dataset)  
   - [Estimates Dataset](#2-estimates-dataset)  
4. [Funding Sources](#funding-sources)  
5. [Distribution Density](#distribution-density)  
6. [Citation](#citation)

---

## **Overview**

This dataset is the first open sourced geospatial mapping of brick kiln sites in the IGP region, providing invaluable insights into the distribution and environmental impact of these sites. Brick kilns are significant contributors to air pollution, and their emissions pose severe public health risks. This repository includes:

- **Precise geolocation of brick kilns**, standardized in CRS $EPSG:4326 (WGS 84)$.
- **Preliminary emissions estimates** for pollutants such as $PM10, PM2.5, NOx, and SOx$.
- **Exposure risk assessments**, including proximity to sensitive areas such as schools, hospitals, and residential populations within a 1 km radius of each kiln.

---

## **Brick Production Calculation**

---

### **Table for Pakistan (PAK), India (IND), and Bangladesh (BAN)**

| **Metric**                            | **Pakistan (PAK)**            | **India (IND)**             | **Bangladesh (BAN)**        |
|---------------------------------------|--------------------------------|-----------------------------|-----------------------------|
| **Annual Production (total kilns)**   | 45 billion bricks (18,000)    | 250 billion bricks (10 lakh) | 15 billion bricks (5,000)  |
| **Identified Kilns for Analysis**     | 11,277 kilns                  | 34,466 kilns               | 4,760 kilns                |
| **Annual Production (identified kilns)** | 28.293 billion bricks         | 8.617 billion bricks | 14.28 billion bricks       |
| **Daily Production per Kiln**         | 12,068 bricks/day             | 11,635 bricks/day | 13,778 bricks/day          |
| **Daily Brick Weight per Kiln**       | 36,204 kg/day                 | 34,905 kg/day | 41,334 kg/day              |
| **Operational Days per Year**         | 215 days                      | 215 days                   | 215 days                   |
| **Seasonal Brick Weight per Kiln**    | $\(36,204 \times 215 = 7,783,860\ kg\)$ | $\(34,905 \times 215 = 7,504,575\ kg\)$ | $\(41,334 \times 215 = 8,896,810\ kg\)$ |

---

## **File Structure**

### **1. Main Dataset**

This dataset includes the primary geolocation data of brick kilns in the region:

| **Column**       | **Description**                                          |
|------------------|----------------------------------------------------------|
| `id`             | Unique identifier for each brick kiln site               |
| `lat`            | Latitude in decimal degrees                              |
| `lon`            | Longitude in decimal degrees                             |
| `state`          | Administrative state/region                              |
| `type`           | Classification (e.g., FCBK or ZigZag kiln)              |
| `schools1km`     | Number of schools within a 1 km radius                   |
| `hosp1km`        | Number of hospitals within a 1 km radius                 |
| `pop1km`         | Estimated population within a 1 km radius                |

### **2. Estimates Dataset**

Supplementary dataset for production and emission estimates:

| **Column**        | **Description**                                          |
|-------------------|----------------------------------------------------------|
| `avg_bricks`      | Average daily kiln operation                             |
| `dailyprod(kg)`   | Daily production in kilograms                            |
| `seasonprod(kg)`  | Seasonal production in kilograms                         |
| `pm2.5d(kg)`      | Daily PM2.5 emissions in kilograms                       |
| `pm10d(kg)`       | Daily PM10 emissions in kilograms                        |
| `noxd(kg)`        | Daily NOx emissions in kilograms                         |
| `soxd(kg)`        | Daily SOx emissions in kilograms                         |
| `pm2.5s(kg)`      | Seasonal PM2.5 emissions in kilograms                    |
| `pm10s(kg)`       | Seasonal PM10 emissions in kilograms                     |
| `noxs(kg)`        | Seasonal NOx emissions in kilograms                      |
| `soxs(kg)`        | Seasonal SOx emissions in kilograms                      |

### **Data Formats**

The dataset is available in the following formats:

- **GeoJSON** (`.geojson`)
- **Shapefile** (`.shp`)
- **CSV** (`.csv`)

---

## **Funding Sources**

This project was funded by:

- **Amazon Web Services (AWS)**  
- **Smith School of Enterprise and The Environment, University of Oxford**

---
## **Special Gratitude**

We want to extend our heartfelt gratitude to @DozBoyd and her team for generously sharing valuable data that significantly contributed to our work on developing a model for detecting brick kilns. Your contributions have been instrumental in enabling us to expand data coverage for the whole of Indian Gangetic Plain (IGP). 

The brick kiln data for whole of India prepared by @DozBoyd and her team is accessible with the following link: [Access the Data](https://geo-ai.undp.org.in/)


## **Distribution Density**

Below are two visualizations showing the distribution density of brick kilns in the IGP region:

**Figure 1: Brick Kiln Density Map**

![Brick Kiln Density Map](all.png)

**Figure 2: Proximity to Sensitive Areas (1km radius)**

![Proximity to Sensitive Areas](proximity_final.png)

---
