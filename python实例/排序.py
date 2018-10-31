#Author guo
raw=[]
for i in range(10):
    x=int(input("请以此输入十个数字"))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]

print(raw)