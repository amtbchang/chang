import os
import pandas as pd

path1 = r'I:\环渤海\未来气象\analysis\mp_85_pr_r.csv'
path_xy = r'I:\环渤海\county_xy.xls'

dt_xy = pd.read_excel(path_xy, index_col='Climate')
dt = pd.read_csv(path1, engine='python',index_col='id')
#dt_xy.head(5)

path = r'I:\环渤海\未来气象\analysis'
for dirpath,filename,filenames in os.walk(path):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.csv' and ('_r'  in filename) :   #          
            filepath = os.path.join(dirpath,filename)
            dt = pd.read_csv( filepath, engine='python',index_col='id')
            dt2=pd.merge(dt_xy, dt, left_index=True,right_index=True)
            dt2.to_excel(r'I:\环渤海\未来气象\analysis\气象插值数据\斜率数据xls\%s.xls'%(filename[:-4]))
