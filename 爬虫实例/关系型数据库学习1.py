#Author guo
import pymysql

db=pymysql.connect(host='127.0.0.1',user='root',password='root',port=3306)#通过connect（）方法声明一个连接对象db
cursor=db.cursor()#用游标进行执行
cursor.execute('select version()')#execute（）执行语句 或得当前版本
data=cursor.fetchone()#利用fetchone获得第一条数据
print('Database Version:',data)
cursor.execute("create DATABASE if not exists spider DEFAULT CHARACTER SET utf8")#创建一个数据库名字为spider
db.close()
#Database Version: ('5.7.18-log',)并且创建一个数据库，名字时spider
#
#创建表的操作
chart=pymysql.connect(host='127.0.0.1',user='root',password='root',port=3306,db='spider')#连接数据库且选择数据库spider
cursor=chart.cursor()#声明一个游标
sql='create table if not exists students (id VARCHAR(255) NOT NULL ,name VARCHAR(255) NOT NULL ,age INT NOT NULL ,PRIMARY KEY(id))'
cursor.execute(sql)


#向表中插入数据
id='20120001'
user='Bob'
age=20

sql='insert into students(id,name,age) values(%s,%s,%s)'#创建sql语句
try:
    cursor.execute(sql,(id,user,age))#传入值到sql语句中，并且提交
    chart.commit()#提交到数据库
except:
    chart.rollback()#提交回滚
cursor.execute('select *from students')#查询该students表
x=cursor.fetchall()#找到表的所有数据
print(x)#打印
chart.close()
#涉及事务ACID 事务确保数据的一致性，要么发生了，要么没有发生
#原子性，一致性，隔离性，持久性
#原子性，发生就发生不能这一半发生，另外一部分没有发生
#一致性 要么发生了，要么没发生
#隔离性 两个事务之间，事务内部操作及使用数据对并发的其他事务是隔离的，并发执行的事务之间不会发生干扰
#持久性 事务一旦提交，更改操作=都必须视为一个事务