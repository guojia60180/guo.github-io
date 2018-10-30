#Author guo
#养兔子
#一对兔子，从出生后第三个月起每一个月都生一对兔子，兔子涨到第三个月后每一个月又生一对兔子
#假设兔子都不死
#问每个月的兔子总数

#迭代计算
#题目感觉有问题

month=int(input('繁殖第几个月'))
month_1=1
month_2=month_3=month_elder=0

for i in range (month):
    month_1,month_2,month_3,month_elder=month_elder+month_3,month_1,month_2,month_elder+month_3
    print('第%d个月共'%(i+1),month_1+month_2+month_3+month_elder,'对兔子')
    print('其中1月兔',month_1)
    print('其中2月兔',month_2)
    print('其中3月兔',month_3)
    print('其中成年兔',month_elder)