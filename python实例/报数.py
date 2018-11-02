#Author guo
#n个人围成一圈
#从第一个人开始报数，从1到3
#凡报到3的人退出圈子

nmax=100
n=int(input("请输入参加的总人数："))
num=[]
for i in range(n):
    num.append(i+1)

i=0
k=0
m=0

while m<n-1:
    if num[i]!=0:
        k=k+1
    if k==3:
        num[i]=0
        k=0
        m=m+1
    i=i+1
    if i==0:
        i=0

i=0
while num[i]==0:
        i=i+1

print(num[i])