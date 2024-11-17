from qgis.core import (
    QgsProject,
    QgsVectorFileWriter,
    QgsVectorLayer,
)

import os

# Set the output directory for the files
output_dir = r"D:\ERASMUS\France_Sem3\side projects\APAD_oxford\Final_Dataset_Folder\APAD-Asset-Data\Asset Data\IGP-Boundary\IGP_PAK - geojson_csv"

# Get all active vector layers
layers = [layer for layer in QgsProject.instance().mapLayers().values() if isinstance(layer, QgsVectorLayer)]

# Loop through each layer and export to CSV and GeoJSON
for layer in layers:
    layer_name = layer.name()
    csv_path = os.path.join(output_dir, f"{layer_name}.csv")
    geojson_path = os.path.join(output_dir, f"{layer_name}.geojson")
    
    # Export to CSV
    QgsVectorFileWriter.writeAsVectorFormat(
        layer, 
        csv_path, 
        "UTF-8", 
        layer.crs(), 
        "CSV", 
        layerOptions=['GEOMETRY=AS_XYZ']
    )
    
    # Export to GeoJSON
    QgsVectorFileWriter.writeAsVectorFormat(
        layer, 
        geojson_path, 
        "UTF-8", 
        layer.crs(), 
        "GeoJSON"
    )
    
    print(f"Exported {layer_name} to CSV and GeoJSON.")

print("Export completed.")
