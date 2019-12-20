# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:03:00 2019

@author: ThinkPad
"""

##rasterio 
##extract rif by mask
import fiona
import os
import rasterio
import rasterio.mask

path = r"I:\环渤海\未来气象\analysis\气象插值数据\插值图\环渤海斜率插值图"
outpath = r'I:\环渤海\未来气象\analysis\气象插值数据\插值图\斜率'

# open mask file
with fiona.open(r"I:/环渤海/gis_map/related_province.shp", "r") as shapefile:##mask shp file
    features = [feature["geometry"] for feature in shapefile]
    
for dirpath,filename,filenames in os.walk(path):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.tif':
            
            filepath = os.path.join(dirpath,filename)
            inRaster = filepath
#open tif by masked
            with rasterio.open(inRaster) as src:#read raster file
                print(src.read(1))
                out_image, out_transform = rasterio.mask.mask(src, features,
                                                                    crop=True)
                out_meta = src.meta.copy()
                out_image[out_image<-100] = 255
                #plt.imshow(out_image[0,:,:])
                
                
                
                
            out_meta.update({"driver": "GTiff",
                             "height": out_image.shape[1],
                             'nodata': 255,
                             "width": out_image.shape[2],
                             "transform": out_transform})
            
            #write the masked raster to a new file.
            with rasterio.open(outpath + os.sep + filename,
                               "w", **out_meta) as dest:#write raster file
                dest.write(out_image)