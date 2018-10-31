#Author guo
n=input("please input any")
a=0
b=len(n)-1
flag=True
while a<b:
    if n[a]!=n[b]:
        print("bushi")
        flag=False
        break
    a,b=a+1,b-1
if flag:
    print("shihuiwen")