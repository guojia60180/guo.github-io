#Author guo
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1
print(factorial(3))
#通过递归的方法求阶乘