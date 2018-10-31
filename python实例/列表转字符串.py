#Author guo
#按逗号分隔列表

L=[1,2,3,4,5]
print(L)
print(','.join(str(n) for n in L))
for n in L:
    print(n,end='')
