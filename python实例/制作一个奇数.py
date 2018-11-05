#Author guo
#求0-7所能组成的奇数个数

sum=4
s=4
for j in range(2,9):
    print(sum)
    if j<=2:
        s=s*7
    else:
        s=s*8
    sum=sum+s
print('sum=%d'%s)

#组成一位的4个
#两位的7*4
#三位的784
#四位的788*4
