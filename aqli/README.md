# AQLI Data Processing


**Reference**: [Air Quality Life Index (AQLI) - University of Chicago](https://www.aqli.org/)

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support

## Installation & Setup

### 1. Create Virtual Environment
```bash
# Navigate to the project directory
cd aqli

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate.ps1

# Activate virtual environment (macOS/Linux)
source venv/bin/activate
```
### 2. Install Dependencies
```bash
# Install required packages from requirements.txt
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
# Test if packages are installed correctly
python -c "import geopandas; import pandas; print('All packages installed successfully!')"
```
## Project Files

### Main Script
- **`join_gadm_pm.py`** - Main script that joins GADM administrative boundaries with PM2.5 data

### Data Files
- **`India_gadm2.shp`** - GADM Level 2 administrative boundaries for India (shapefile)
- **`pm2.csv`** - PM2.5 air quality measurements by administrative district
- **`aqli_india.geojson`** - AQLI reference geospatial data for India

### Output
- **`joined_gadm_pm.geojson`** - Generated output file combining GADM boundaries with PM2.5 data

## Usage

### Running the Main Script
```bash
# Ensure virtual environment is activated
.\venv\Scripts\activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Run the join script
python join_gadm_pm.py
```

The script will:
1. Read the GADM shapefile with administrative boundaries
2. Read the PM2.5 CSV file with air quality data
3. Join the datasets on their ID columns
4. Output a combined GeoJSON file for visualization and analysis

## Dependencies

The project uses the following Python packages:
- **geopandas** - Working with geospatial data and shapefiles
- **pandas** - Data manipulation and analysis
- **shapely** - Geometric operations
- **fiona** - Reading/writing spatial data formats
- **pyogrio** - OGR/GDAL Python bindings
- **pyproj** - Cartographic projections and coordinate transformations

For complete dependency list, see `requirements.txt`.

## Data Dictionary

### PM2.5 CSV Columns
- `level` - Administrative level (2 = district)
- `id` - Unique identifier for the district
- `name0` - Country name
- `name1` - State/Province name
- `name` - District name
- `population` - District population
- `pm2023` - PM2.5 concentration (μg/m³) for 2023
- `population_weighted_exposure` - Weighted exposure metric
- `normalised_exposure` - Normalized exposure index

### GADM Shapefile Columns
- `ID_2` - Unique identifier matching pm2.csv `id` column
- `geometry` - Geographic boundaries (polygons)
- Other administrative fields

## References

- **AQLI**: https://www.aqli.org/
- **AQLI Research**: https://www.energy-policy.uchicago.edu/research-and-data/air-quality-life-index-aqli
- **GADM Database**: https://gadm.org/
- **PM2.5 Data**: World Health Organization Air Quality Guidelines

## Troubleshooting

### Virtual Environment Issues
```bash
# If activation fails, try:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate:
.\venv\Scripts\activate.ps1
```

### Package Installation Issues
```bash
# Update pip first
python -m pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

## Support
For issues with the scripts contact us and for AQLI data, visit: https://www.aqli.org/contact
