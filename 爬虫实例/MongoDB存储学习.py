#Author guo
import pymongo
client=pymongo.MongoClient(host='127.0.0.1',port=27017)

db=client.test#以test数据库进行选取

#每个数据库中包含很多集合，类似于表

collection=db.students
#声明了一个collection对象

#插入数据

student={
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student1={
    'id':'20170202',
    'name':'guo',
    'age':22,
    'gender':'male'
}
result=collection.insert([student,student1])
print(result)#5c222bcbcba2254434923fa1 每条数据都有一个_id属性来唯一标识
#如果没有显式的指明该属性，MongoDB会产生一个ObjectId类型的id属性

#查询

result=collection.find_one({"name":"guo"})
print(type(result))
print(result)#find_one只返回单个结果，返回类型是字典类型

from bson.objectid import ObjectId
result=collection.find_one({'_id':ObjectId('5c222ceccba2254bfcf01739')})
print(result)#利用bson 查询id，返回结果是字典类型的，如果查询不存在，则返回None

result=collection.find({"name":"guo"})
print(type(result))#<class 'pymongo.cursor.Cursor'>
for x in result:
    print(x)
#find产生的是一个cursor类型的数据，是一个生成器
#需要遍历产生所有结果，每个结果分别都是字典类型

#带有选择性的查找方案
'''
$lt 小于
$gt 大于
$lte 小于等于
$gte 大于等于
$ne 不等于
$in 在范围内[20,23]
$nin
'''
print("查找年龄大于20的")
result=collection.find({"age":{'$gt':20}})#查找大于20的,其中查找的类型是一个字典类型的进行查找的
for y in result:
    print(y)

#利用正则表达式的查找

print("查找名字以w开头的")
result=collection.find({"name":{"$regex":"^w.*"}})#查找，以regex的方式进行查找
for z in result:
    print(z)

'''
功能符号查找

$exists 属性是否存在 {"name":{"$exists":True}} name 属性存在
$type {"age":{"$type":"int"}}
$mod  {"age":{"$mod":[5,0]}} 模5余0
$text {"$text":{"$search":"Mike"}} text类型的属性中包含Mike字符串的
$where {"$where":"obj.fans_couny==obj.follows_count"} 高级查找
'''

