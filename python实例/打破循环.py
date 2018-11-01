#Author guo
#求输入数字的平方，平方运算后小于50退出

while True:
    try:
        n=float(input("输入一个数字："))
    except:
        print('输入有错')
        continue
    dn=n**2
    print('平方为',dn)
    if dn<50:
        print('平方小于50')
        break