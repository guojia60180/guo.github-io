#Author guo
#n为偶数时，调用函数完成1/2+1/4=。。。。
#n为奇数时，调用函数完成1/1+1/3=。。。。

def peven(n):
    i=0
    s=0.0
    for i in range(2,n+1,2):
        s=s+(1.0)/i
    return s

def podd(n):
    i=0
    s=0.0
    for i in range(1,n+1,2):
        s=s+(1.0)/i
    return s

def dcall(fp,n):#继承前两个函数
    s=fp(n)
    return s

n=int(input('input a number'))
if n%2==0:
    sum=dcall(peven,n)
else:
    sum=dcall(podd,n)

print(sum)
