import geopandas as gpd
import pandas as pd
import os

def main():
    """Main function to join GADM shapefile with PM2.5 CSV data."""
    
    print("=" * 70)
    print("GADM Shapefile and CSV Data Join Tool")
    print("=" * 70)
    
    # Get file paths from user
    print("\n--- File Paths ---")
    gadm_shp_path = input("Enter the path to the GADM shapefile: ").strip()
    pm_csv_path = input("Enter the path to the CSV file: ").strip()
    output_path = input("Enter the output path for the joined GeoJSON file (default: joined_output.geojson): ").strip()
    
    if not output_path:
        output_path = "joined_output.geojson"
    
    # Validate input files exist
    if not os.path.exists(gadm_shp_path):
        print(f"\nError: Shapefile not found at '{gadm_shp_path}'")
        return
    
    if not os.path.exists(pm_csv_path):
        print(f"\nError: CSV file not found at '{pm_csv_path}'")
        return
    
    # Read the shapefile
    print("\n--- Reading GADM Shapefile ---")
    try:
        gadm_gdf = gpd.read_file(gadm_shp_path)
        print(f"✓ Loaded successfully")
        print(f"  Shape: {gadm_gdf.shape[0]} features, {gadm_gdf.shape[1]} columns")
        print(f"  Columns: {gadm_gdf.columns.tolist()}")
        print(f"\n  First few rows:")
        print(gadm_gdf.head(3))
    except Exception as e:
        print(f"✗ Error reading shapefile: {e}")
        return
    
    # Read the CSV file
    print("\n--- Reading CSV File ---")
    try:
        pm_df = pd.read_csv(pm_csv_path)
        print(f"✓ Loaded successfully")
        print(f"  Shape: {pm_df.shape[0]} rows, {pm_df.shape[1]} columns")
        print(f"  Columns: {pm_df.columns.tolist()}")
        print(f"\n  First few rows:")
        print(pm_df.head(3))
    except Exception as e:
        print(f"✗ Error reading CSV file: {e}")
        return
    
    # Get ID column names from user
    print("\n--- Select ID Columns for Join ---")
    print(f"Shapefile columns: {gadm_gdf.columns.tolist()}")
    print(f"CSV columns: {pm_df.columns.tolist()}")
    
    shapefile_id_col = input("\nEnter the ID column name in the shapefile: ").strip()
    csv_id_col = input("Enter the ID column name in the CSV file: ").strip()
    
    # Validate ID columns exist
    if shapefile_id_col not in gadm_gdf.columns:
        print(f"\n✗ Error: Column '{shapefile_id_col}' not found in shapefile")
        print(f"  Available columns: {gadm_gdf.columns.tolist()}")
        return
    
    if csv_id_col not in pm_df.columns:
        print(f"\n✗ Error: Column '{csv_id_col}' not found in CSV")
        print(f"  Available columns: {pm_df.columns.tolist()}")
        return
    
    # Join the data
    print("\n--- Joining Data ---")
    print(f"Joining on: Shapefile.{shapefile_id_col} = CSV.{csv_id_col}")
    
    try:
        joined_gdf = gadm_gdf.merge(pm_df, left_on=shapefile_id_col, right_on=csv_id_col, how='left')
        print(f"✓ Join successful")
        print(f"  Result shape: {joined_gdf.shape[0]} features, {joined_gdf.shape[1]} columns")
        print(f"  Columns: {joined_gdf.columns.tolist()}")
        
        # Check for unmatched records
        unmatched = joined_gdf[joined_gdf.isnull().any(axis=1)].shape[0]
        if unmatched > 0:
            print(f"  ⚠ Warning: {unmatched} unmatched records (rows with NaN values)")
        
        print(f"\n  First few rows of joined data:")
        print(joined_gdf.head(3))
        
    except Exception as e:
        print(f"✗ Error during join: {e}")
        return
    
    # Save the joined data
    print("\n--- Saving Output ---")
    try:
        joined_gdf.to_file(output_path, driver='GeoJSON')
        print(f"✓ Successfully saved to: {output_path}")
    except Exception as e:
        print(f"✗ Error saving file: {e}")
        return
    
    print("\n" + "=" * 70)
    print("Join operation completed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
