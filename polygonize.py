import rasterio as rio
import geopandas as gpd

def polygonize(ras):
  ras = rio.open(study_dir)
  geojson = []
  for shape, value in features.shapes(ras.read(1), transform=ras.transform):
      for poly in shape['coordinates']:
          geojson.append(pg(poly))
  g = gpd.GeoDataFrame(geometry=geojson)
  return g
