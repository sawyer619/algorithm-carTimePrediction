# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:36:09 2016

@author: ying
"""
import MySQLdb
import pandas as pd
from pandas import DataFrame 
import numpy as np
from numpy import array

# 20140803_train.txt
# 打开数据库连接
conn = MySQLdb.connect(host="localhost",user="root",passwd="songying",db="cartimepre")
# 使用cursor()方法获取操作游标
cursor = conn.cursor()

sql = """
select * from 20140803_train where id_car=2788 order by time;
"""
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
data = array(results)
print data.shape

newdata = DataFrame(data)
columns = ['carID', 'latitude','longitude','passenger','time']
newdata.columns = columns
newdata.to_csv('E:/algorithm_carPredict/data/2788x_03.txt', index=False)
# 使用 fetchone() 方法获取一条数据库。

# 关闭数据库连接
conn.close()