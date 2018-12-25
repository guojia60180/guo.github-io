#Author guo
import pymysql
#一个更加通用的sql使用，利用字典来传入数据，实现动态长度等等的传入
db=pymysql.connect(host='127.0.0.1',user='root',password='root',db='spider')
cursor=db.cursor()
data={
    'id':'5123131',
    'name':'guo',
    'age':22
}#构建一个字典的形式
table='students'#选择该表
keys=','.join(data.keys())#调用join方法扩充
values=','.join(['%s']*len(data))#*法作为扩充
sql='insert into {table}({keys}) VALUES ({values}) on duplicate key update id=%s,name=%s,age=%s'.format(table=table,keys=keys,values=values)#把值都传入进去
#duplicate 可以用来对数据进行更新
try:#利用try except来试错的传入数据
    if cursor.execute(sql,tuple(data.values())):
        print('successful input')
        db.commit()
except:
    print('failed to input')
    db.rollback()

sql='update students set age=%s where name=%s'
try:
    cursor.execute(sql,(25,'Bob'))
    db.commit()
except:
    db.rollback()
db.close()

