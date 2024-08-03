# Asset-Data Repository Structure

## Repository Overview

This repository contains data related to various assets that contribute to pollution, categorized pollution data, and population exposure risk calculated based on these assets. The repository is organized into three main folders:

1. **Asset Data**
2. **Pollution Data**
3. **Population Exposure Risk**

### Folder Structure

#### 1. Asset Data

This folder contains subfolders for each asset type that contributes to pollution. Each subfolder contains data specific to that asset, such as its geographical location, operational details, and other relevant information.

- `Asset Data/`
  - `Brick Kiln/`
  - `Cement/`
  - `Steel/`
  - `Marble and Granite/`
  - `Transport/`
  - `Open burning sites/`
  - `Coal/`
  - `Oil/`
  - `Gas/`
  - `Pulp and paper industry/`
  - `Chemical industry/`
  - `Crop stubble burning (seasonal)/`

#### 2. Pollution Data

This folder contains data on various pollutants. The subfolders are organized based on the type of pollutant. Each subfolder contains data related to the specific pollutant, including its concentration levels across different regions.

- `Pollution Data/`
  - `PM2.5/`
  - `PM10/`
  - `SO2/`
  - `NOx/`

#### 3. Population Exposure Risk

This folder contains data related to the population exposure risk to pollutants, calculated based on the assets listed in the Asset Data folder. The calculations use a decay function to estimate the risk levels. A README file is included in this folder to explain the decay function and the calculation process.

- `Population Exposure Risk/`
  - `README.md` (Explanation of the decay function and risk calculation methodology)
  - `Brick Kiln/`
  - `Cement/`
  - `Steel/`
  - `Marble and Granite/`
  - `Transport/`
  - `Open burning sites/`
  - `Coal/`
  - `Oil/`
  - `Gas/`
  - `Pulp and paper industry/`
  - `Chemical industry/`
  - `Crop stubble burning (seasonal)/`

---

### README.md (for Population Exposure Risk folder)

#### Population Exposure Risk Calculation

This folder contains the calculated metrics for population exposure to pollutants from various assets. The exposure risk is estimated using a decay function, which models how pollutant concentration diminishes with distance from the source.

#### Decay Function

The decay function is defined as:

\[ C(x) = C_0 \times e^{-\lambda x} \]

Where:
- \( C(x) \) is the pollutant concentration at distance \( x \) from the source.
- \( C_0 \) is the initial pollutant concentration at the source.
- \( \lambda \) is the decay rate, which depends on the pollutant type and environmental factors.
- \( x \) is the distance from the source.

**Note:** The decay function described is commonly used in environmental science and air pollution modeling to estimate how pollutant concentration decreases with distance from the source.
#### Calculation Process

1. **Identify Asset**: Determine the asset type and its location.
2. **Pollutant Data**: Use the relevant pollutant data from the `Pollution Data` folder.
3. **Apply Decay Function**: Apply the decay function to estimate pollutant concentration at various distances from the asset.
4. **Estimate Exposure Risk**: Combine the pollutant concentration with population data to estimate exposure risk.

#### File Structure

Each asset type has its folder within the `Population Exposure Risk` directory, containing calculated exposure risk data. The structure mirrors the `Asset Data` folder for ease of reference.





