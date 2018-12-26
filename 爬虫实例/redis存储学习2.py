#Author guo
#字符串操作

from redis import StrictRedis

redis=StrictRedis(host='127.0.0.1',port=6379,db=0,password='root')

print(redis.mget(['Name','age']))#得到多个value值
#返回多个键对应的value值
redis.set('name','Hello')
redis.setrange('name',6,'World')#在修改后的hello6位偏移处，字符串

#批量赋值
redis.msetnx({'name2':'DDDD','name3':'james'})
#前提是键不存在时

redis.substr('name',1,4)#返回name的字符串1



