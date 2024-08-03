---

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


