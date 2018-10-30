#Author guo
#一个数恰好等于它的因子之和，这个数就是完数
#6=1+2+3

def fac(num):
    target=int(num)
    res=set()#利用集合保障其中没有重复元素
    for i in range (1,num):
        if num%i==0:
            res.add(i)
            res.add(num/i)
    return res

for i in range (2,1001):
    if i==sum(fac(i))-i:#保障完成不加其自身
        print(i)