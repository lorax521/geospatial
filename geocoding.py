# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:04:33 2019

@author: James Raines
"""

import geopandas as gpd
import pandas as pd

addressCSV = r'C:\Users\jrainesi\Downloads\CurrentState-OwnedFuelingLocations.csv'
outputFilePath = r'C:\Users\jrainesi\Downloads\OwnedFuelingLocations_geocoded.shp'
addressFieldName = 'full'

def geocodeCSV(addressCSV, addressFieldName, outputFilePath):

    df = pd.read_csv(addressCSV)
    openmapquest_apiKey = 'fOoEZg8aL0iAgUAwG6YhhRBbjBwQ5qTi' # this one is pretty inaccurate
    arcgis_apiKey = 'SYlBs9Lv9TJRdaw1'

    failed = []
    geoms = pd.DataFrame()
    for address in df[addressFieldName]:
        try:
            geom = gpd.tools.geocode(address, provider='arfcgis')
            geoms = geoms.append(geom.iloc[[0]])
            print('success: ' + address)
        except:
            failed.append(address)
            print('failed: ' + address)
    geoms[addressFieldName] = geoms['address']
    df_wGeoms = df.merge(geoms, how='right')
    gdf = gpd.GeoDataFrame(df_wGeoms)

    gdf.to_file(outputFilePath, driver='ESRI Shapefile')

geocodeCSV(addressCSV, addressFieldName, outputFilePath)