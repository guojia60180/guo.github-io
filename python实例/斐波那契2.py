#Author guo
#有一个分数序列：2/1,3/2,5/3
a=2.0
b=1.0
s=0
for n in range(1,21):
    s=s+a/b
    a,b=a+b,a
print(s)