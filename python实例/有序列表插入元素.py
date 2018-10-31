#Author guo
#有一个已经排好序的数组，现在输入一个数，把它插入数组中

#插入排序的思想

lis=[1,10,100,1000,10000,100000,1000000]
for i in range (2):
    n=int(input("请输入要插入的值"))

    lis.append(n)
for i in range(len(lis)):

    for j in range(i,len(lis)):
        if lis[i]>lis[j]:
            lis[i],lis[j]=lis[j],lis[i]

print(lis)
#插入+排序的方法来使用的
#可以使得题目更加简单
