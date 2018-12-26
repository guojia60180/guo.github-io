#Author guo
from redis import StrictRedis

redis=StrictRedis(host='127.0.0.1',port=6379,db=0,password='root')#或者可以使用连接pool的方法进行连接

redis.set('name','Bob')#调用set方法，设置一个键值对
print(redis.get('name'))#获取并打印
redis.set('age',22)
print(redis.get('age'))
print(redis.exists('name'))#是否存在键名
print(redis.type('name'))#键的类型b'string'
print(redis.keys('n*'))#获取所有以n开头的键[b'name']
print(redis.randomkey())#随机获取一个键
redis.rename('name','Name')
print(redis.dbsize())#获取当前数据库大小
#redis.expire('name',2) 将name的过期时间设置为2s
print(redis.ttl('name'))#获取过期时间
#move（name,db）移动到别的数据库
#flushdb（）删除当前选择数据库中的所有键
#flushall（） 删除所有数据库中所有的键
