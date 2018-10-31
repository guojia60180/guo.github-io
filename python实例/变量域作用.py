#Author guo
#学习使用auto定义变量的用法
#python 中的变量作用域

i=0
n=0
def dummy():
    i=0
    print(i)
    i=i+1

def dummy2():
    global n
    print(n)
    n=n+1
print('函数内部的同名向量')
for j in range(20):
    print(i)
    dummy()
    i=i+1

print('globa 声明同名变量')
for k in range(20):
    print(n)
    dummy2()
    n=n+1