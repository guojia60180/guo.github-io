#Author guo
#使用random模块

import random
print(int(random.uniform(10,20)))
t=int(input("想生成随机数的列表位数"))
lis=[]
for i in range (t):
    lis.append(int(random.uniform(1,10)))
    print(lis)
print(lis)
