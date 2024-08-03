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





