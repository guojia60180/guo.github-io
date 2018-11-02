#Author guo
#输入数组，最大的与第一个元素交换，最小的与最后一个元素减缓

li=[3,2,4,56,1,4,5,434]
li[-1],li[li.index(min(li))]=li[li.index(min(li))],li[-1]

m=li[0]
ind=li.index(max(li))
li[0]=li[ind]
li[ind]=m

print(li)