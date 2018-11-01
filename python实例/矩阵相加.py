#Author guo
#计算两个矩阵相加

#创建一个新的矩阵，使用for循环，取出X和Y矩阵对应位置的值，相加后放到新矩阵对应位置后

X=[[12,7,3],[4,5,6],[7,8,9]]
Y=[[5,8,1],[6,7,3],[4,5,9]]

res=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range (len(res)):
    for j in range (len((res[0]))):
        res[i][j]=X[i][j]+Y[i][j]

print(res)
