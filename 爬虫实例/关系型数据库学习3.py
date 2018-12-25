#Author guo
import pymysql
#一个更加通用的sql使用，利用字典来传入数据，实现动态长度等等的传入
db=pymysql.connect(host='127.0.0.1',user='root',password='root',db='spider')
cursor=db.cursor()

table='students'
condition='age>30'

sql='delete from {table} where {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    print('删除成功')
    db.commit()
except:
    db.rollback()

db.close()