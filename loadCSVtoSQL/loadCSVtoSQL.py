# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:06:25 2016

@author: admin110
"""

import MySQLdb

#==============================================================================
# # predPaths_test.txt
# # 打开数据库连接
# conn = MySQLdb.connect(host="localhost",user="root",passwd="songying",db="cartimepre")
# # 使用cursor()方法获取操作游标
# cursor = conn.cursor()
# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS predPaths_test")
# 
# # 使用execute方法执行SQL语句
# sql_createPre = '''
# create table predPaths_test(
# id_path int not null,
# id_car MEDIUMINT not null,
# latitude DOUBLE not null,
# longitude DOUBLE not null,
# state_passenger TINYINT  not null,
# time  DATETIME  not null
# )engine=innodb;
# '''
# cursor.execute(sql_createPre)
# 
# sql_loadData = """
# load data local infile "E:/algorithm_carPredict/data/predPaths_test.txt"
# into table predPaths_test FIELDS TERMINATED BY ',';
# """
# cursor.execute(sql_loadData)
# conn.commit()
# # 使用 fetchone() 方法获取一条数据库。
# 
# # 关闭数据库连接
# conn.close()
#==============================================================================

# 20140803_train.txt
# 打开数据库连接
conn = MySQLdb.connect(host="localhost",user="root",passwd="songying",db="cartimepre")
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS 20140803_train")

# 使用execute方法执行SQL语句
sql_createPre = '''
create table 20140805_train(
id_car MEDIUMINT not null,
latitude DOUBLE not null,
longitude DOUBLE not null,
state_passenger TINYINT  not null,
time  DATETIME  not null
)engine=innodb;
'''
cursor.execute(sql_createPre)

sql_loadData = """
load data local infile "E:/algorithm_carPredict/data/20140805_train.txt"
into table 20140805_train FIELDS TERMINATED BY ',';
"""
cursor.execute(sql_loadData)
conn.commit()
# 使用 fetchone() 方法获取一条数据库。

# 关闭数据库连接
conn.close()