#Author guo
#求1+2！+3！等的和
#两个思路 利用标准库函数 math  自己写一个阶乘函数
import math
total=0
for i in range(1,21):
    total=total+math.factorial(i)

print(total)
res=1
#第二种实现
for i in range (20,1,-1):
    res=res*i+1
print(res)

#第三种实现lamda函数
from functools import reduce
n=3
total1=0
for e in range (n):

    fac=reduce(lambda x,y:x*y,range(1,n+1))
    total1=total+fac
print(total1)