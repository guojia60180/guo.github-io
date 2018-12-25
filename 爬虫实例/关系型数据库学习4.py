#Author guo
import pymysql
#一个更加通用的sql使用，利用字典来传入数据，实现动态长度等等的传入
db=pymysql.connect(host='127.0.0.1',user='root',password='root',db='spider')
cursor=db.cursor()

sql='select *from students where age>=20'

try:
    cursor.execute(sql)
    print('count',cursor.rowcount)#rowcount是数据的个数，在这个里面是四条
    one=cursor.fetchone()#获取结果的第一条数据
    print('one',one)
    results=cursor.fetchall()#得到所有的数据二重元组
    #注意，fetch有一个内部指针，偏移指向查询结果，最开始指向第一个数据，
    print('results',results)
    print('results type',type(results))
    #fetchall结果将以元组的形式返回，如果数据量大，占的开销会非常高
    for row in results:
        print(row)

except:
    print('error')