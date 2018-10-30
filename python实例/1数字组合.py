#Author guo
#1,2,3,4组合出互不相同且无重复的三位数

total=0
for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
            if((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total=total+1

print(total)