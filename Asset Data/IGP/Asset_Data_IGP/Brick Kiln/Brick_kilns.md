# Brick Kilns in IGP Region Using AI

<div style="background-color: #f0f8ff; color: #333; padding: 20px; border-radius: 10px;">

This repository provides a comprehensive geospatial analysis of brick kiln operations in the Indo-Gangetic Plain (IGP) region (Bangladesh, India, and Pakistan), focusing on their environmental and public health impacts. Using low-resolution satellite imagery, we have mapped and analyzed brick kiln sites, estimating their production and emissions. This dataset represents a pioneering effort to understand the spatial distribution of brick kilns and their contribution to air pollution in the region.

</div>

---

## **Table of Contents**

1. [Overview](#overview)  
2. [Brick Production Calculation](#brick-production-calculation)  
   - [Table for Total Production](#table-for-pakistan-india-and-bangladesh)  
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
- **Preliminary emissions estimates** for pollutants such as $PM10$, $PM2.5$, $NOx$, and $SOx$.
- **Exposure risk assessments**, including proximity to sensitive areas such as schools, hospitals, and residential populations within a 1 km radius of each kiln.

---

## **Brick Production Calculation**

---

### **Table for Pakistan India and Bangladesh**

Thank you for clarifying! Let's recalculate everything based on **11,272 kilns** while scaling down the total production of **45 billion bricks** for **18,000 kilns**. Here's the step-by-step breakdown:

---

### Step 1: Annual Production per Kiln  
**Annual Production per Kiln** = \( \frac{45 \text{ billion bricks}}{18,000 \text{ kilns}} = 2.5 \text{ million bricks/kiln} \)  

---

### Step 2: Total Annual Production for 11,272 Kilns  
**Total Annual Production for 11,272 Kilns** = \( 11,272 \times 2.5 \text{ million bricks} = 28.18 \text{ billion bricks} \)  

---

### Step 3: Daily Production per Kiln  
- **Total Daily Production** = \( \frac{28.18 \text{ billion bricks}}{215 \text{ operational days}} \)  
  \( = 131.02 \text{ million bricks/day} \)  
- **Daily Production per Kiln** = \( \frac{131.02 \text{ million bricks/day}}{11,272 \text{ kilns}} \)  
  \( \approx 11,625 \text{ bricks/day} \)  

---

### Updated Table  

| **Metric**                            | **Pakistan (PAK)**            | **India (IND)**             | **Bangladesh (BAN)**        |
|---------------------------------------|--------------------------------|-----------------------------|-----------------------------|
| **Annual Production (total kilns)**   | 45 billion bricks (18,000)    | 250 billion bricks (10 lakh) | 15 billion bricks (5,000)  |
| **Identified Kilns for Analysis**     | 11,272 kilns                  | 34,466 kilns               | 4,760 kilns                |
| **Annual Production (identified kilns)** | 28.18 billion bricks         | 8.617 billion bricks       | 14.28 billion bricks       |
| **Daily Production per Kiln**         | 11,625 bricks/day             | 11,635 bricks/day          | 13,778 bricks/day          |
| **Daily Brick Weight per Kiln**       | 36,204 kg/day                 | 34,905 kg/day              | 41,334 kg/day              |
| **Operational Days per Year**         | 215 days                      | 215 days                   | 215 days                   |
| **Seasonal Brick Weight per Kiln**    | \(36,204 \times 215 = 7,783,860\ kg\) | \(34,905 \times 215 = 7,504,575\ kg\) | \(41,334 \times 215 = 8,896,810\ kg\) |

---

## **File Structure**

- Check the .xlsx files for more information
  
### **Data Formats**

The dataset is available in the following formats:

- **GeoJSON** (`.geojson`)
- **Shapefile** (`.shp`)
- **CSV** (`.csv`)
- **XLSX** (`.xlsx`)

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
