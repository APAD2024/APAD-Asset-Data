# **Brick Kilns in the Indo-Gangetic Plain (IGP) Identified Using AI**

<div style="background-color: #f0f8ff; color: #333; padding: 20px; border-radius: 10px;">
This repository presents the first large-scale, AI-enabled geospatial mapping of brick kiln operations across the Indo-Gangetic Plain (IGP)—covering **Bangladesh, India, and Pakistan**.  
Using deep learning applied to satellite imagery, we identify kiln locations, estimate production, and provide annualized emissions for major pollutants.  
This dataset offers vital insights into one of South Asia’s largest unregulated industrial contributors to air pollution.
</div>

---

# **Table of Contents**

1. [Overview](#overview)
2. [Brick Production Calculation](#brick-production-calculation)
3. [File Structure](#file-structure)
4. [Funding Sources](#funding-sources)
5. [Acknowledgments](#special-gratitude)
6. [Distribution Density](#distribution-density)
7. [Citation](#citation)

---

# **Overview**

This dataset provides:

✔ **Geolocation of brick kilns** (lat/lon), standardized to **EPSG:4326 (WGS 84)**

✔ **Baseline emissions for PM₁₀, PM₂.₅, NOₓ, SO₂**

✔ **1 km exposure risk assessment for sensitive sites**

This work accompanies our research paper and data published on Zenodo:

**Paper:** Hamdani, M.S.A., Zakir, K., Kushwaha, N. et al. Brick Kiln Dataset for Pakistan’s IGP Region Using AI. Sci Data 12, 830 (2025). https://doi.org/10.1038/s41597-025-05148-9
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.17897579.svg)](http://dx.doi.org/10.5281/zenodo.17897579)

The dataset is provided in:

* CSV
* GeoJSON
* XLSX

---

# **Brick Production Calculation**

### **Summary Table: Pakistan, India, Bangladesh**

| **Metric**                               | **Pakistan (PAK)** | **India (IND)** | **Bangladesh (BAN)** |
| ---------------------------------------- | ------------------ | --------------- | -------------------- |
| **Annual Production (national)**         | 45B bricks         | 250B bricks     | 15B bricks           |
| **Estimated Total Kilns**                | ~18,000            | ~1,000,000      | ~5,000               |
| **Kilns Identified in Dataset**          | 11,272             | 34,466          | 4,760                |
| **Annual Production (identified kilns)** | 28.18B bricks      | 8.617B bricks   | 14.28B bricks        |
| **Daily Production per Kiln**            | 11,625             | 11,635          | 13,778               |
| **Daily Brick Weight**                   | 36,204 kg          | 34,905 kg       | 41,334 kg            |
| **Operational Days**                     | 215                | 215             | 215                  |
| **Seasonal Weight Output per Kiln**      | 7.78M kg           | 7.50M kg        | 8.90M kg             |

---

# **File Structure**

The repository includes standardized datasets in multiple formats and regional variants.

## **Available Formats**

* `.csv`
* `.geojson`
* `.xlsx`

---

## **1. Main Dataset**

Contains basic geolocation fields.

### **Columns**

| Field        | Description                          |
| ------------ | ------------------------------------ |
| `id`         | Kiln identifier                      |
| `lat`, `lon` | GPS coordinates                      |
| `type`       | Kiln technology (e.g., FCBK, Zigzag) |
| `state`      | State/Province                       |
| `country`    | Country                              |
| `status`     | Operational status                   |

---

## **2. Emission Datasets**

Two different scenarios based on fuel type:

### **A. Coal Emission Dataset — `emissions_coal.*`**

### **B. Biomass Emission Dataset — `emissions_biomass.*`**

### **Columns**

| Field                  | Description                       |
| ---------------------- | --------------------------------- |
| `id`                   | Matches main dataset              |
| `lat`, `lon`           | Coordinates                       |
| `type`                 | Kiln type                         |
| `fuel`                 | Coal or Biomass                   |
| `state`, `country`     | Administrative info               |
| `status`               | Operational                       |
| `capacity_tonnes`      | Annual capacity (where available) |
| `emfpm10`, `pm10_t_yr` | PM₁₀ EF & emissions               |
| `emfpm25`, `pm25_t_yr` | PM₂.₅ EF & emissions              |
| `emfso2`, `so2_t_yr`   | SO₂ EF & emissions                |
| `emfnox`, `nox_t_yr`   | NOₓ EF & emissions                |
| `source`               | Reference for EF or capacity      |

---

# 📁 **Folder Structure**

### **`corrected/` Folder**

Contains corrected datasets for:

* **India (IND)**
* **Pakistan (PAK)**

Includes `.csv`, `.geojson`, `.xlsx`.

---

### **`with_fps/` Folder**

Contains **full point-set (FPS)** datasets for:

* **India**
* **Pakistan**
* **Bangladesh**

This folder includes all kilns detected by the AI workflow.

---

# **Funding Sources**

This research was funded by:

* **Amazon Web Services (AWS)**
* **Smith School of Enterprise and the Environment, University of Oxford**

---

# **Special Gratitude**

We express deep gratitude to **@DozBoyd** and her team for sharing critical datasets and supporting our expansion of brick kiln identification across the IGP.

Their India-wide kiln dataset is available here:
🔗 [https://geo-ai.undp.org.in/](https://geo-ai.undp.org.in/)

---

# **Distribution Density**

### **Figure 1: Brick Kiln Density Map**

![Brick Kiln Density Map](all.png)

### **Figure 2: Proximity to Sensitive Areas**

![Proximity Map](proximity_final.png)

---

# **Citation**

If you use this dataset or code, please cite:

> **Hamdani, M.S.A., Zakir, K., Kushwaha, N. et al. Brick Kiln Dataset for Pakistan’s IGP Region Using AI. Sci Data 12, 830 (2025). https://doi.org/10.1038/s41597-025-05148-9**
> Zenodo. [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.17897579.svg)](http://dx.doi.org/10.5281/zenodo.17897579)
> Dataset available in CSV, GeoJSON, and XLSX formats.
---
