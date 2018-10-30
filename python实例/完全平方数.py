#Author guo
#这是一个错误的程序
# n=0
# for n in range(100):
#     if (((n+1)**2)-(n**2))==68:
#         break
#     else:
#         n=n+1
# print(n)

#示例正确程序
#先计算上限
#然后通过整型判断是否为完全平方数

n=0
while (n+1)**2-n*n<=168:
    n=n+1
print(n)
for i in range ((n+1)**2):
    if i**0.5==int((i**0.5))and (i+168)**0.5==int((i+168)**0.5):
        print(i-100)



