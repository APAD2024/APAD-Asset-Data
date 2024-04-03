**Calculation of Air Pollution Emissions from a Coal Power Plant**

**Introduction:**
This document outlines the methodology for calculating air pollution emissions, specifically particulate matter ($\PM_2.5\$ and $\PM_10\$), sulfur dioxide ($\SO_2\$), and nitrogen oxides ($\NOx\$) from a coal-fired power plant. The calculations are based on emission factors provided in various sources for coal power plants in India.

**Emission Factors:**

1. **Particulate Matter (PM2.5 and PM10):**
   - Emissions per unit: $\ 0.16-0.22 \text{ g/kWh}\$ for PM2.5
   - Emissions per unit: $\ 0.29-0.45 \text{ g/kWh}\$ for PM10
   - Source: [India Air Quality - Coal Power Plants Emissions](https://www.indiaairquality.info/wp-content/uploads/docs/2014-08-AE-Emissions-Health-Coal-PPs-India.pdf)

3. **Sulfur Dioxide ($\SO_2\$):**
   - Emissions per unit: $\ 7.20  \text{ g/kWh}\$
   - Source: [US EPA - Emissions Inventory Conference](https://www3.epa.gov/ttnchie1/conference/ei20/session5/mmittal.pdf)

4. **Nitrogen Oxides (NOx):**
   - Emissions per unit: $\ 4.22 - 4.38 \text{ g/kWh}\$
   - Source: [US EPA - Emissions Inventory Conference](https://www3.epa.gov/ttnchie1/conference/ei20/session5/mmittal.pdf)

**Calculation Methodology:**
To estimate the total annual emissions of each pollutant, the following steps are taken:

1. **Electricity Production Calculation:**
   Electricity production (kWh) is calculated based on the capacity of the power plant for one hour and then extrapolated for a year.
   $$\text{Electricity Production (kWh)} = \text{Capacity (MW)} \times 1000 \times 1 \text{ hour/day} \times 365 \text{ days/year}$$
   For example, if the power plant has a capacity of 30 MW:
   $$\text{Electricity Production (kWh)} = 30 \, \text{MW} \times 1000 \times 1 \, \text{hour/day} \times 365 \, \text{days/year} = 30,000 \times 365 \, \text{MWh/year}$$
   
   $$\text{Electricity Production (kWh)} = 10,950,000 \, \text{kWh/year}$$

3. **Emissions Calculation:**
   Once the electricity production is determined, emissions for each pollutant are calculated by multiplying the emissions per unit (g/kWh) by the total electricity production (kWh) and converting to tonnes per annum assuming full capacity operation for a year.
   
   For $\PM_2.5\$ and PM10:

   $$\text{Emissions (tonnes/annum)} = \left( \text{Emissions per unit (g/kWh)} \times \text{Electricity Production (kWh)} \right) \times \frac{1}{1,000,000}$$
   
   For SO2 and NOx:
   $$\text{Emissions (tonnes/annum)} = \left( \text{Emissions per unit (g/kWh)} \times \text{Electricity Production (kWh)} \right) \times \frac{1}{1,000,000}$$
   
**Conclusion:**
This methodology provides a framework for estimating air pollution emissions from a coal-fired power plant based on emission factors and electricity production. The calculated emissions can be useful to estimate emissions for other pollution assets, like cement factory, paper plants and more. 
