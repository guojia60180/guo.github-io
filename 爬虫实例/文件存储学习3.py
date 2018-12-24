#Author guo
#csv文件存储

'''
文件以某种换行符分隔，最常见的是逗号和制表符只作为分隔
所有的记录都有完全相同的字段序列，相当于一个结构化表的纯文本形式
比Excel更加简洁
'''

import csv

with open('data.csv','w')as csvfile:#打开csv文件，指定打开方式，w，获得文件句柄
    writer=csv.writer(csvfile)#调用CSV库的writer（）方法初始化写入对象，传入该句柄
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',22])
    writer.writerow(['10003','Jordan',21])

#写入的文本默认以，号来隔开
#writer=csv.writer(csvfile,delimiter='')#修改列与列之间的分隔符，可以使用delimiter参数

#一般情况下，爬虫爬取的都是结构化的数据，一般会用字典的形式表现出来
#csv库中也提供了字典的写入方式
# fieldnames=['id','name','age']
# writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
# writer.writeheader()写入头文件信息
#完成字典的导入

#读取csv信息

with open('data.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)

#另外可以通过pandas来读取csv文件

import pandas#速度比较慢效率比较低，但是出来的格式之类的都很好，一个相对成熟的方式进行的产生的数据
df=pandas.read_csv('data.csv')
print(df)