#Author guo
#将一个列表逆序
#两种实现 依次交换位置，调用列表方法

lis=[1,10,100,1000,10000]
for i in range (int(len(lis)/2)):
    lis[i],lis[len(lis)-1-i]=lis[len(lis)-1-i],lis[i]
print(lis)

lis1=[1,10,100,1000,10000]
lis1.reverse()
print(lis1)
