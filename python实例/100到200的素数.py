#Author guo
#判断100到200之间有多少个素数
#判断素数的方法：用一个数分别取除2到sqrt
#能被整除，此数不是素数
import math
for i in range(100,200):
    flag=0
    for j in range(2,round(math.sqrt(i))+1):
        if i%j==0:
            flag=1
            break
    if flag:
        continue
    print(i)

