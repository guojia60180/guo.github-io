#Author guo
#将一个整数分解质因数
#测试用例
#输入90 打印90=2*3*3*5

#从2开始向本身遍历能整除就是最小质数
target=int(input('please input an interger'))
print(target,'=',end='')

if target<0:
    target=abs(target)
    print('-1*',end='')
flag=0
if target<=1:
    print(target)
    flag=1
while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i,end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target=target/i
            break