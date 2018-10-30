#Author guo
#输入三个整数x,y,z 把这三个数按大小排序

#说道排序有很多方法，python自己的函数sort就是一种，Timsort是结合了合并排序（merge sort）和插入排序（insertion sort）而得出的排序算法
#另外比较多的是快排
#这里通过不同的方式写一下

raw=[]
#输入部分 利用append 把所输入的数字添加到列表中
for i in range(3):
    x=int(input('please input three integer to sort:'))
    raw.append(x)
#排序部分
for i in range (len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)

#sort是在原位重新排列列表，而sorted()是产生一个新的列表。

raw2=[]
for i in range(3):
    x=int(input('please input three integer to sort:'))
    raw2.append(x)
print(raw2)
raw2.sort()
print(raw2)
print(sorted(raw2))

#快速排序实现
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1
raw3=[]
for i in range(3):
    x=int(input('please input three integer to sort:'))
    raw3.append(x)
quick_sort(raw3,0,len(raw3)-1)
print(raw3)