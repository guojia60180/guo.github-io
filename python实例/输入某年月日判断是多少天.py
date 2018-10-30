#Author guo
'''
x=input("请输入某年某月某天格式为19950819")
year=x[0:4]
print(type (year))
date=x[4:]
print(date)
year=int(year)
print(year,type (year))
date=int(date)
print(date)
'''
#定义是否为闰年
def isleapyear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))

Dofm=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0

year=int(input('year:'))
month=int(input('month:'))
day=int(input('day:'))
if isleapyear(year):
    Dofm[2]+=1
for i in range(month):

    res=res+Dofm[i]
print(res+day)

