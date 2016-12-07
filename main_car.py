# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:47:43 2016

@author: ying
"""

import pandas as pd
from math import radians, cos, sin, asin, sqrt

fileData = 'E:/algorithm_carPredict/data/20140803_train.txt'
#fileData = './data/20140803_train.txt'
data = pd.read_csv(fileData, header = None, nrows=None)
data.columns = ['carID', ' latitude', 'longitude', 'passenger', 'time']


sqrt((30.683857-30.684124)**2+(104.049011-104.050485)**2)


def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000
#a = haversine(104.126179, 30.650675, 104.126196, 30.650675)    

def Distance(one):
    #dis = sqrt((one[1] - 30.684124)**2 + (one[2] - 104.050485)**2)
    #dis = haversine(one[2], one[1], 104.050485, 30.684124)
    dis = haversine(one[2], one[1], 104.050485, 30.684124)
    
    if(dis <= 10000):
        print dis
        return one
        
    else:
        return [None, None, None, None, None]
new = data.apply(Distance, axis=1)

x = data.loc[data['carID']==1,:]
x = x.sort_values(by='time')
x.to_csv('E:/algorithm_carPredict/data/1x.txt', index=False)

fileTest = 'E:/algorithm_carPredict/data/20140803_train.txt'
test = pd.read_csv(fileTest, header = None)

a = [i for i in range(1,31691)]
b = [1800 for i in range(1,31691)]
c = pd.DataFrame(dict(a=a,b=b))
c.columns = ['pathid','time']
c.to_csv('E:/algorithm_carPredict/ans_test.csv', header=True, index=False)

#encoding=utf-8
import re
import sys
import pandas as pd
import math

df1 = pd.read_csv("E:/algorithm_carPredict/data/predPaths_test.txt", header=None, names=["pathid","taxi_id","lat","lon","busy","dtime"])

df1["time"]=1
df2=df1.groupby('pathid').agg({'time':'count'})
df2=df2.reset_index()
df2['time']=df2['time']*20
df2.to_csv("E:/algorithm_carPredict/out.csv",index=False)
