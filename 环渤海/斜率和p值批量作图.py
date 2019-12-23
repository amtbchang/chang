# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:24:09 2019

@author: ThinkPad
"""


import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt

path_p_value = r'I:\环渤海\未来气象\analysis\气象插值数据\插值图\斜率'
list_p = [i for i in os.listdir(path_p_value) if i.endswith('tif')]


for i in range(len(list_p)):
    with rasterio.open(path_p_value + os.sep + list_p[i]) as src:#read raster file
        #print(src.read(1))
        arr = src.read(1)
        arr[arr == 255] = np.nan
        arr[arr > 10] = 0
        #arr[arr <= 0.05] = 2
        #arr[np.where((0.05>arr) | (arr < 1))] = 0.95
        #plt.subplots_adjust(right=0.99, left=0.125, bottom=0.14, top=0.975)##消除白边
        plt.imshow(arr[:,:],cmap='rainbow', alpha=0.8,)# range!vmin=0.0, vmax=2,
        plt.text(850,900,'%s'%(list_p[i][:-4]))
        plt.colorbar()
        plt.savefig(path_p_value+os.sep+'png'+os.sep+list_p[i][:-4]+'.png',bbox_inches='tight')
        plt.close()