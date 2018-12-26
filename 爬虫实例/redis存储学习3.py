#Author guo
from redis import StrictRedis

redis=StrictRedis(host='127.0.0.1',port=6379,db=0,password='root')

#列表操作

#提供列表存储，列表内的元素可以重复，可以从两端存储

redis.rpush('list',1,2,3)#向键为list的末尾加入1，2,3
print(redis.lpush('list',0))#返回列表大小。头部加入0
print(redis.llen('list'))#求列表大小
print(redis.lrange('list',1,20))#返回name列表中，保留索引荣1,20的所有
#切片处理
print(redis.ltrim('list',1,5))
redis.lpop('list')#返回并删除list中左边第一个元素
redis.rpop('list')#返回并删除list中右边第一个元素

#集合操作
redis.sadd('tags','books','tea','coffee')#向键为tags的集合插入三个参数
redis.srem('tags','books')#删除数据
redis.scard('tags')#返回集合中元素的个数
#交集并集等很多方法
print(redis.smembers('tags'))#返回集合中的所有元素

#有序集合操作
#有序集合比集合多一个分数字段，利用它可以对集合中的数据进行排序

redis.zadd('grade',100,'Bob',98,'Mike')#添加的元素是一个类似字典型的
#redis.zrem()删除一个元素
print(redis.zrank('grade','Mike'))#返回该集合中的排名
#注意无zmemeber的方法


#散列操作
redis.hset('price','cake',5)#向键为price的散列表中添加映射关系，cake的值为5
redis.hsetnx('price','book',6)
print(redis.hget('price','cake'))#获取该映射所对应的值
redis.hmset('price',{'banana':2,'pear':6})
#批量增加映射
redis.hlen('price')#获取映射的个数
print(redis.hkeys('price'))#获取所有的映射名
print(redis.hvals('price'))#获取所有的映射值
print(redis.hgetall('price'))#获取所有的映射与映射值，一一对应
