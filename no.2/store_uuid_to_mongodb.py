#usr/bin/python
#encoding=utf-8

import pymongo
import uuid
#连接到mongodb,这里的mongodb在本地运行，默认监听27017端口
connection = pymongo.Connection('localhost', 27017)
#连接到指定数据库，不存在即创建
db = connection.python_study
#指定collection，不存在即创建
collection = db.uuid

for i in range(200):
    #向指定的collection中插入数据
    collection.insert({"id": i, "value": uuid.uuid4()})

