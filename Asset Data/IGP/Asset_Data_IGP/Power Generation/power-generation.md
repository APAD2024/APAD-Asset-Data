
# Emission Factors (EFs) for Furnace Oil and Natural Gas  

---

## 1. Overview

This document summarizes the emission factors (EFs) used to estimate atmospheric emissions from:

- **Furnace oil (residual fuel oil / heavy fuel oil)**
- **Natural gas**

These factors follow the **U.S. EPA AP-42** methodology, the global standard for stationary combustion emissions.

The goal is to provide **consistent, traceable pollutant EFs** for emissions modeling in power plants and industry.

---

## 2. Furnace Oil Emission Factors (g/L)

Source: **EPA AP-42, Chapter 1.3: Fuel Oil Combustion**  
https://www.epa.gov/sites/default/files/2020-09/documents/1.3_fuel_oil_combustion.pdf

Using South Asian furnace oil with **Sulfur = 3.5%**, the PM factor from AP-42:

```
A = 1.12S + 0.37 = 4.29 lb/1000 gal
```

Converted to **g/L**, the furnace oil EFs used are:

| Pollutant | EF (g/L) | Source |
|-----------|----------|--------|
| **PM₂.₅** | **2.404** | AP-42 Table 1.3-5 |
| **PM₁₀** | **9.6** | Derived (≈4× PM₂.₅) |
| **SO₂** | **73.43 g/L** | AP-42 formula (157 × S) |
| **NOₓ** | **5.63 g/L** | AP-42 Table 1.3-1 |
| **CO**  | **0.60 g/L** | AP-42 Table 1.3-1 |

**PM controls** (ESPs, bag filters) typically remove ~95%, so PM emissions may be multiplied by **0.05** post-control.

---

## 3. Natural Gas Emission Factors (g/m³)

Source: **EPA AP-42, Chapter 1.4: Natural Gas Combustion**  
https://www3.epa.gov/ttn/chief/ap42/ch01/final/c01s04.pdf

The EPA provides gas EFs in **lb per 10⁶ scf**.  
Conversion used:

```
g/m³ = (lb/10⁶ scf) × 0.016
```

Final EFs for natural gas (uncontrolled small boiler):

| Pollutant | EF (g/m³) | Source |
|-----------|-----------|--------|
| **NOₓ** | **1.60** | AP-42 Table 1.4-1 |
| **CO**  | **1.34** | AP-42 Table 1.4-1 |
| **PM₂.₅** | **0.122** | AP-42 Table 1.4-2 |
| **PM₁₀** | **0.122** | Same (all PM <1 µm) |
| **SO₂** | **0.0096** | AP-42 Table 1.4-2 |

---


## 5. Units Used

| Fuel | EF Unit | Why |
|------|---------|------|
| **Furnace oil** | g/L | Liquid fuel (density ~0.99 kg/L) |
| **Natural gas** | g/m³ | Gaseous fuel measured volumetrically |

**Important:** Gas is *never* converted to litres. Oil and gas use separate unit systems.

---

## 6. How to Apply These EFs

### Furnace oil:
```
t/yr = L/year × EF(g/L) ÷ 1,000,000
```

### Natural gas:
```
t/yr = m³/year × EF(g/m³) ÷ 1,000,000
```

Fuel consumption must match EF units.

---

## References

1. **EPA AP-42, Chapter 1.3 – Fuel Oil Combustion**  
   https://www.epa.gov/sites/default/files/2020-09/documents/1.3_fuel_oil_combustion.pdf  

2. **EPA AP-42, Chapter 1.4 – Natural Gas Combustion**  
   https://www3.epa.gov/ttn/chief/ap42/ch01/final/c01s04.pdf  

3. **IPCC 2006 Guidelines – Stationary Combustion**  
   https://www.ipcc-nggip.iges.or.jp/public/2006gl/

---
