# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 18:56:44 2016

@author: ying
"""

import pandas as pd
from math import radians, cos, sin, asin, sqrt

fileData = './data/20140803_train.txt'
data = pd.read_csv(fileData, header = None)
data.columns = ['carID', ' latitude', 'longitude', 'passenger', 'time']

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

def Distance(one):
    #dis = sqrt((one[1] - 30.684124)**2 + (one[2] - 104.050485)**2)
    #dis = haversine(one[2], one[1], 104.050485, 30.684124)
    dis = haversine(one[2], one[1], 104.050485, 30.684124)
    
    if(dis <= 5):
        print dis
        return one
        
    else:
        return [None, None, None, None, None]

new = data.apply(Distance, axis=1)
new1 = new.dropna(how='any')
new1.to_csv('lu1_0803.csv')
