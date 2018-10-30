#Author guo
#生成水仙数
for i in range(100,1000):
    s=str(i)
    x=int(s[0])
    y=int(s[1])
    z=int(s[2])
    if i==x**3+y**3+z**3:
        print(i)