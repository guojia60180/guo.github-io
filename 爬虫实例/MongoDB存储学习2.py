#Author guo
import pymongo
client=pymongo.MongoClient(host="127.0.0.1",port=27017)
db=client.test
collection=db.students

results=collection.find()
for result in results:
    print(result)

count=collection.find().count()
print(count)#统计符合条件的条数

results=collection.find().sort('age',pymongo.ASCENDING)#根据年龄的升序排列
print([result['name'] for result in results])
#降序传入DESCENDING

results=collection.find().sort('age',pymongo.ASCENDING).skip(2).limit(5)#利用skip方法偏移几个位置比如忽略前两个元素
print([result['name'] for result in results])#利用limit方法只产生5个
#最好不要使用大的偏移量来查找数据，会导致内存溢出
#最好是使用id的查询方式单独查询

 #数据更新 update（）

condition={'name':'guo'}
student=collection.find_one(condition)
student['age']=25
result=collection.update(condition,student)
print(result)

#{'$inc':{'age':1}} 年龄加1 符合该条件使得年龄加1 前面是condition


#删除
#remove

result=collection.remove({'name':'Jorden'})#符合条件的所有数据都会被删除
print(result)

result=collection.delete_one({'name':'guo'})#删除第一个符合条件的数据
print(result)
result=collection.delete_many({'name':"guo"})#删除所有符合的数据 可以调用delete_count 来获取删除的个数

'''
此外MongoDB还具有索引等功能，create_index(),create_indexs(),drop_index()等方法
'''