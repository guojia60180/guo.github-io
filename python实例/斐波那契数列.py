#Author guo
#实现斐波那契数列fibonacci sequence
#从1,1开始，后面每一项是前两项的和
#图方便就递归实现，图性能就循环

#循环实现

def Fibonacci_Loop(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a + b
        n -= 1
    return result_list
x=int(input("请输入要得到的数"))
print(Fibonacci_Loop(x))

#递归实现
def Fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
print()
print(Fib(x))

#yeild迭代实现
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))
print(Fibonacci_Yield(x))