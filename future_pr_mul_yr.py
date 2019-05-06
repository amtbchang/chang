# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:47:53 2019

@author: ThinkPad
"""

from netCDF4 import Dataset
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt

    

ds = gdal.Open(r'G:\china_geodata\China_soil_1km\ChinaSoil_1km.tif')
prj = ds.GetProjection()
#tr = ds.GetGeoTransform()
tr = (0,2.5, 0.0, 90, 0.0, -2)
#write tif
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
import os
dir_name = r'H:\future_clim\pr\4.5\GISS-E2-R'
filename = os.listdir(dir_name)
name = []
for i in filename:
    if i.endswith('.nc'):
        name.append(i)
path = []
for i in range(4):
    path.append(dir_name + os.sep + name[i])

for j in range(4):
    if j < 1:
        for i in range(240):
            writeTiff(Dataset(path[j], 'r')['pr'][i, ::-1, :]*3600*24*30,144, 90, 1,tr, prj,dir_name+'//'+'GFDL4.5_pr_%d.tif'%(j*240+i+1))
    else:
        for i in range(300):
            writeTiff(Dataset(path[j], 'r')['pr'][i, ::-1, :]*3600*24*30,144, 90, 1,tr, prj,dir_name+'//'+'GFDL4.5_pr_%d.tif'%((j-1)*300+240+i+1))
        
#单位kg /m/s ->3600*24*30*, tem -273.15
