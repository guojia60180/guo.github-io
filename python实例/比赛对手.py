#Author guo
#乒乓球比赛，各出三个人进行比赛
#甲队abc
#乙队xyz

#a不和x c不和xz比

a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
c=c-set(['x','z'])
a=a-set(['x'])

for i in a:
    for j in b:
        for k in c :
            if len(set((i,j,k)))==3:
                print('a:%s,b:%s,c:%s'%(i,j,k))