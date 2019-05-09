# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:04:19 2019

@author: ThinkPad
"""

import os
import numpy as np
from osgeo import gdal

def writeTiff(im_data,im_width,im_height,im_bands,im_geotrans,im_proj,path):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    elif len(im_data.shape) == 2:
        im_data = np.array([im_data])
    else:
        im_bands, (im_height, im_width) = 1,im_data.shape
        #创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(path, im_width, im_height, im_bands, datatype)
    if(dataset!= None):
        dataset.SetGeoTransform(im_geotrans) #写入仿射变换参数
        dataset.SetProjection(im_proj) #写入投影
    for i in range(im_bands):
        dataset.GetRasterBand(i+1).WriteArray(im_data[i])
    del dataset
    

ds = gdal.Open(r'G:\china_geodata\China_soil_1km\ChinaSoil_1km.tif')
prj = ds.GetProjection()
tr = (-180, 0.0833333, 0.0, 88.5, 0.0, -0.0833333)
dir_name = r'H:\manure数据\ManNitProCrpRd'

for i in os.listdir(dir_name)[-35:]:
    data = np.loadtxt(dir_name + os.sep + i)
    data[data==-9999] = np.nan
    writeTiff(data/100, 4320, 2124,1,tr, prj,r'H:\manure数据\manure_apl'+os.sep+i[:6]+'.tif')
 