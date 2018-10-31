#Author guo
#求一个3×3的矩阵的对角线元素之和

mat=[[1,2,3],[3,4,5],[4,5,6]]
res=0
for i in range (len(mat)):#注意这里的len（mat）的值为3
    res=res+mat[i][i]

print(res)