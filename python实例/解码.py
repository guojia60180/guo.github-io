#Author guo
#加密铭文解密

#每位数字加5，和除以10的余数代替，第一位与第四位交换，第二位与第三位交换

n=input()
n=str(n)
a=[]
for i in range(4):
    a.append(int(n[i])+5)
a[0],a[3]=a[3],a[0]

print(''.join('%s'%s for s in a))