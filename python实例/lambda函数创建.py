#Author guo

Max=lambda x,y:x*(x>=y)+y*(y>x) #利用真假来判断 真为1 假为0
Min=lambda x,y:x*(x<=y)+y*(y<x)

a=int(input('1'))
b=int(input('2'))

print(Max(a,b))
print(Min(a,b))