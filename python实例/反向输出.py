#Author guo
#给定正整数，求几位数，逆序打印数字

n=int(input("输入正整数："))
n=str(n)
print('%d位数'%len(n))
print(n[::-1])
