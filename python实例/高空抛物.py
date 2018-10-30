#Author guo
#球从100m落下，每次落地后为原来的一半，求他在第十次落地时
#共经过多少米
#第十次反弹多高

high=100
total=100
for i in range(10):
    high=high/2
    total=total+high*2
    print(high)
print(total)