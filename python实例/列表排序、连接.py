#Author guo
#列表排序、连接
#排序可用sort方法。连接用extend方法或者+

a=[2,6,8]
b=[7,0,4]
a.extend(b)
c=sorted(a)
a.sort()
print(c)
print(a)