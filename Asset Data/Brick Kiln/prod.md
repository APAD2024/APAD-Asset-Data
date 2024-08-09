
## Estimating Emissions Per Kiln

### 1. Given Data:
   - **Emission Factors:**
     - PM10: 9.7 g/kg
     - PM2.5: 6.8 g/kg
     - SOx: 4.6 g/kg
     - NOx: 4.7 g/kg
     - CO: 90 g/kg
   - **Brick Production per Kiln:** 6,894 bricks/day
   - **Weight of Each Brick:** 3 kg

### 2. Total Brick Weight per Day:
Since each brick weighs approximately 3 kg, the total weight of bricks produced per day by one kiln is:
   $\text{Total Brick Weight} = \text{Number of Bricks} \times \text{Weight per Brick} = 6,894 \times 3  \text{kg}$

   $\text{Total Brick Weight} = 20,682 \text{kg}$

### 3. Calculate Emissions for Each Pollutant:
To calculate the total emissions of each pollutant, multiply the emission factor by the total weight of bricks produced.

#### a. PM10 Emissions:

$\text{PM10 Emissions} = \text{Emission Factor} \times \text{Total Brick Weight} = 9.7 \text{g/kg} \times 20,682 \text{kg}$

$\text{PM10 Emissions} = 200,615.4 \text{g} = 200.6154  \text{kg/day}$

#### b. PM2.5 Emissions:

$\text{PM2.5 Emissions} = 6.8 \text{g/kg} \times 20,682  \text{kg} = 140,637.6  \text{g} = 140.6376  \text{kg/day}$

#### c. SOx Emissions:

$\text{SOx Emissions} = 4.6 \text{g/kg} \times 20,682 \text{kg} = 95,137.2 \text{g} = 95.1372  \text{kg/day}$

#### d. NOx Emissions:

$\text{NOx Emissions} = 4.7  \text{g/kg} \times 20,682 \text{kg} = 97,207.4 \text{g} = 97.2074 \text{kg/day}$

#### e. CO Emissions:

$\text{CO Emissions} = 90 \text{g/kg} \times 20,682 \text{kg} = 1,861,380 \text{g} = 1,861.38 \text{kg/day}$

### 4. Annual Emissions (assuming the kiln operates 365 days/year):
Multiply the daily emissions by 365 to get the annual emissions.

#### a. PM10 Annual Emissions:

$\text{PM10 Annual Emissions} = 200.6154 \text{kg/day} \times 365 = 73,224.621 \text{kg/year}$

#### b. PM2.5 Annual Emissions:

$\text{PM2.5 Annual Emissions} = 140.6376 \text{kg/day} \times 365 = 51,632.724 \text{kg/year}$

#### c. SOx Annual Emissions:

$\text{SOx Annual Emissions} = 95.1372 \text{kg/day} \times 365 = 34,725.078 \text{kg/year}$

#### d. NOx Annual Emissions:

$\text{NOx Annual Emissions} = 97.2074  \text{kg/day} \times 365 = 35,473.701  \text{kg/year}$

#### e. CO Annual Emissions:

$\text{CO Annual Emissions} = 1,861.38  \text{kg/day} \times 365 = 679,402.7 \text{kg/year}$

This calculation assumes continuous operation without downtime and a consistent production rate.


---

## Estimating Concentration and Emission Rate

To estimate the concentration and emission rate based on the given formula and assumptions from "Assessment of air pollutant emissions from brick kilns" by [Rajarathnam, U, et al., (2014)](https://doi.org/10.1016/j.atmosenv.2014.08.075)

### Given Formula:
- **Emission Rate (ER):**
  
  $ER\text{(g/h)} = \frac{S \text{(mg/m}^3\text{)}}{Q_S \text{(m}^3\text{/h)}}$
  where:
  - \( S \) is the concentration of the pollutant in the fuel gas (mg/m³).
  - $(Q_S)$ is the flow rate of the flue gas (m³/h).

- **Fuel Unit Mass-Based Emission Factor (EFm):**
  
  $EF_m \text{(g/kg)} = \frac{ER \text{(g/h)}}{F \text{(kg/h)}}$
  where:
  - \( F \) is the fuel consumption rate (kg/h).

### Assumptions:
1. **Fuel Consumption Rate:** Assume the kiln consumes 100 kg of fuel per hour (this value can be adjusted based on real data).
2. **Flow Rate of Flue Gas $(Q_S)$:** Assume a flow rate of 500 m³/h (this value can be adjusted based on real data).

### Calculating Emission Rate (ER):

Let’s assume that the concentration of PM10 in the fuel gas is \( S = 200 \text{mg/m}^3 \) (this is an assumed value for demonstration purposes only).

$ER \text{(g/h)} = \frac{S \text{(mg/m}^3\text{)}}{Q_S\text{(m}^3\text{/h)}} = \frac{200  \text{mg/m}^3}{500 \text{m}^3\text{/h}} = \frac{200 \text{mg/m}^3}{500\text{m}^3\text{/h}}$

First, convert mg to g:

$ER \text{(g/h)} = \frac{200 \text{mg/m}^3 \times 1 \text{g/1000 mg}}{500 \text{m}^3\text{/h}} = \frac{0.2 \text{g/m}^3}{500  \text{m}^3\text{/h}} = 0.0004\text{g/h}$

So, the emission rate \( ER \) is 0.0004 g/h.


These values are based on the assumptions made and can be adjusted according to real data. If the actual flow rate of fuel gas, fuel consumption rate
