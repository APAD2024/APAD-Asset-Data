# Coal Plant Dataset

## Description

The Coal Plant dataset is a comprehensive collection of data detailing various aspects of coal power plants for Indian Gangetic Plain (IGP) and some of the African countries. This dataset includes information on plant locations, capacities, emissions, operational status, and other relevant attributes. The primary goal of this dataset is to enable the monitoring and analysis of air pollution and its impact on the environment and public health.

## Dataset Contents

- **Plant Information**: Names, locations (latitude and longitude), and operational status of coal power plants.
- **Capacity**: Generation capacity of each plant, measured in megawatts (MW).
- **Emissions**: Data on various emissions, including CO2, SO2, NOx, and particulate matter.
- **Fuel Types**: Types of coal used, such as bituminous, sub-bituminous, lignite, etc.
- **Operational Data**: Year of commissioning, planned retirement dates, and other operational metrics.

## Some Pre-Processing

- Using different datasets to filter, combine, and create the new dataset.
***Steps to pre-process data for "IND"
- Load the CSV files for coal_igp and coal_india.
- Filter coal_igp for rows where the country is 'India'.
- Find matching coal plants from coal_igp in coal_india based on a common identifier (e.g., plant name or ID).
- Retain the matching records in coal_india, along with any other records that don't match.
- Multiply the units column by the capacity column to create a new column with the total capacity.
- 
## Purpose

This dataset is designed to support research and policy-making aimed at reducing air pollution from coal power plants. By providing detailed information on plant operations and emissions, the dataset allows for:

- **Air Quality Monitoring**: Tracking emissions to understand their impact on local and global air quality.
- **Regulatory Compliance**: Assessing compliance with environmental regulations and identifying areas needing improvement.
- **Policy Development**: Informing policy decisions to mitigate the environmental and health impacts of coal power generation.
- **Public Awareness**: Raising awareness about the environmental impacts of coal plants and promoting cleaner energy alternatives.

## Future Enhancements
We are continuously working to expand and enhance the Coal Plant dataset. Future updates will include:

- **Historical Data**: Adding historical emissions and operational data to analyze trends over time.
- **Health Impact Studies**: Integrating data on public health outcomes related to air pollution from coal plants.
- **Economic Analysis**: Providing insights into the economic impacts of coal plant operations, including costs of emissions and potential savings from alternative energy sources.
- **Geospatial Analysis Tools**: Developing tools for advanced geospatial analysis of coal plant impacts on surrounding environments.

## Contribution and Feedback

We welcome contributions and feedback from the community to improve and expand this dataset. Please feel free to open issues or submit pull requests on our [GitHub repository](https://github.com/APAD2024/APAD-Asset-Data).

## Contact
For any questions, suggestions, or collaboration inquiries, please contact us at [apad.world.proj@gmail.com](mailto:apad.world.proj@gmail.com).

## License
TBD

## Citation
If you use this dataset in your research or projects, please cite it as follows:
```
TBD
```

We are excited to see how this dataset will be used to drive meaningful action towards cleaner air and a healthier environment. Stay tuned for more updates and resources!
