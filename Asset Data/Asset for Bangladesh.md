# Asset for Bangladesh

This repository provides an overview to the listed assets in the workbook. Bangladesh is among the most polluted (especially air pollution) in the world. In the effort to determine some of the major assets and industries that contribute to the deterioration of the environment, APAD tries to establish a database along with the associated emission estimates. 

There are 6 major assets:

1. Brick Kilns
2. Coal Plants
3. Cement Plants
4. Steel Plants
5. Furnace Oil
6. Paper and Pulp

Although brick kilns top the list numerically, other assets significantly contributes to the total emissions. In the following section, we will provide a quick overview of the estimation protocol to receive critical feedback and assistance to achieve precise estimations. 

## Schema

### Cement, Paper, Coal, Steel Plants Schema

#### Each facility asset uses the following columns:

- **id**: Unique identifier for each facility.
- **name**: Facility name.
- **lat/lon**: Latitude and longitude for geospatial location.
- **type**: Facility type (integrated, grinding for cement; Paper, Pulp; zigzag/fcbk - brick kilns).
- **fuel**: Primary energy or fuel used (coal, natural gas, biomass).
- **region/country**: Administrative and geographic context.
- **status**: Operational status (operating, construction, and others)
- **capacity**: Installed production or generation capacity.
- **emfpm10, emfpm25, emfso2, emfnox**: Emission factors for particulate matter (PM10, PM2.5), sulfur dioxide (SO2), and nitrogen oxides (NOx), typically per unit output or energy.
- **pm10, pm25, so2, nox**: Calculated total annual emissions for each pollutant, commonly in tonnes/year.

### Brick Kiln Schema

#### Brick kilns utilize specific columns for both geospatial/social context and detailed emissions:

- **id, lat, lon, type, state**: Unique location and identification.
- **schools1km, hosp1km, pop1km**: Proximity impacts and affected population.
- **avg_bricks, seasonprod(bricks)**: Average and seasonal brick production, essential for estimating annual output.
- **emf_coal(pm2.5), emf_coal(pm10), emf_coal(nox), emf_coal(so2)**: Emission factors per brick from coal burning.
- **emf_biomass(pm2.5), emf_biomass(pm10), emf_biomass(nox), emf_biomass(so2)**: Similar factors for biomass firing.
- **pm2.5d(kg), pm10d(kg), so2d(kg), noxd(kg) and seasonal forms (pm2.5s_c(kg), and so on)**: Detailed daily and seasonal emission estimates based on kiln type and fuel.

## Production Calculation

**Production Estimate**: Production estimate is typically based on facility capacity and operational days.

#### Brick Kilns


| **Metric**                            | **Pakistan (PAK)**            | **India (IND)**             | **Bangladesh (BAN)**        |
|---------------------------------------|--------------------------------|-----------------------------|-----------------------------|
| **Annual Production (total kilns)**   | 45 billion bricks (18,000)    | 250 billion bricks (10 lakh) | 15 billion bricks (5,000)  |
| **Identified Kilns for Analysis**     | 11,272 kilns                  | 34,466 kilns               | 4,760 kilns                |
| **Annual Production (identified kilns)** | 28.18 billion bricks         | 8.617 billion bricks       | 14.28 billion bricks       |
| **Daily Production per Kiln**         | 11,625 bricks/day             | 11,635 bricks/day          | 13,778 bricks/day          |
| **Daily Brick Weight per Kiln**       | 36,204 kg/day                 | 34,905 kg/day              | 41,334 kg/day              |
| **Operational Days per Year**         | 215 days                      | 215 days                   | 215 days                   |
| **Seasonal Brick Weight per Kiln**    | \(36,204 \times 215 = 7,783,860\ kg\) | \(34,905 \times 215 = 7,504,575\ kg\) | \(41,334 \times 215 = 8,896,810\ kg\) |


#### Coal Plants

Electricity production (KWh/year) is calculated based on the capacity of the power plant for 24 hours and then extrapolated for a year.

$$\text{Electricity Production (KWh/year)} = \text{Capacity (MW)} \times 1000 \times 24 \text{ hours/day} \times 365 \text{ days/year}$$

For example, if the power plant has a capacity of 30 MW:

$$\text{Electricity Production (KWh/year)} = 30 \ \text{MW} \times 1000 \times 24 \ \text{hours/day} \times 365 \ \text{days/year} = 30,000 \times 24 \times 365 \ \text{KWh/year}$$
$$\text{Electricity Production (KWh/year)} = 26,280,0000 \ \text{KWh/year}$$

#### All the other assets

The capacity is pre-estimated in tonnes per year.


## Emissions


| Asset Type   | Pollutant           | Emission Factor Unit         | Typical Value                  | Emission Calculation Formula                                                                                                                                       |
|--------------|---------------------|-----------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Coal Plant   | PM2.5               | g/KWh                       | 0.16–0.22                     | \( \text{E} = \text{EF} \times \text{Annual Generation} \div 1{,}000{,}000 \) <br> (\( \text{E} \): tonnes/yr, EF: g/KWh, Generation: KWh/yr)                    |
|              | PM10                | g/KWh                       | 0.29–0.45                     | Same as above                                                                                                              |
|              | SO2                 | g/KWh                       | 7.20                          | Same as above                                                                                                              |
|              | NOx                 | g/KWh                       | 4.22–4.38                     | Same as above                                                                                                              |
| Brick Kiln   | PM2.5 (coal)        | g/brick or kg/season        | 6.8 (daily), x (seasonal)     | \( \text{E} = \text{EF} \times \text{Bricks} \div 1{,}000 \) (if EF in g/brick); or seasonal total from CSV                 |
|              | PM10 (coal)         | g/brick or kg/season        | 9.7 (daily), x (seasonal)     | Same as above                                                                                                              |
|              | SO2 (coal)          | g/brick or kg/season        | 4.6 (daily), x (seasonal)     | Same as above                                                                                                              |
|              | NOx (coal)          | g/brick or kg/season        | 4.7 (daily), x (seasonal)     | Same as above                                                                                                              |
|              | PM2.5 (biomass)     | g/brick or kg/season        | 0.404 (daily), x (seasonal)   | Same as above                                                                                                              |
|              | PM10 (biomass)      | g/brick or kg/season        | 0.404 (daily), x (seasonal)   | Same as above                                                                                                              |
|              | NOx (biomass)       | g/brick or kg/season        | 0.72 (daily), x (seasonal)    | Same as above                                                                                                              |
|              | SO2 (biomass)       | g/brick or kg/season        | 3.19 (daily), x (seasonal)    | Same as above                                                                                                              |
| Cement       | PM10                | g/tonne                     | 69.2                          | \( \text{E} = \text{EF} \times \text{Capacity} \div 1{,}000 \) (Capacity in tonnes)                                        |
|              | PM2.5               | g/tonne                     | 22.4                          | Same as above                                                                                                              |
|              | SO2                 | g/tonne                     | -                       | Same as above where available                                                                                              |
|              | NOx                 | g/tonne                     | -                        | Same as above where available                                                                                              |
| Steel        | PM10                | g/tonne                     | -          | \( \text{E} = \text{EF} \times \text{Capacity} \div 1{,}000 \) (Capacity in tonnes)                                        |
|              | PM2.5               | g/tonne                     | -                        | Same as above                                                                                                              |
|              | SO2                 | g/tonne                     | -                        | Same as above                                                                                                              |
|              | NOx                 | g/tonne                     | -                        | Same as above                                                                                                              |
| Paper        | PM10                | g/tonne                     | 0.315                         | \( \text{E} = \text{EF} \times \text{Capacity} \div 1{,}000 \) (Capacity in tonnes)                                        |
|              | PM2.5               | g/tonne                     | 0.315                         | Same as above                                                                                                              |
|              | SO2                 | g/tonne                     | 0.43                          | Same as above                                                                                                              |
|              | NOx                 | g/tonne                     | 0.53                          | Same as above                                                                                                              |

