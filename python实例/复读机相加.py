#Author guo
#求s=a+aa+aaa+aaaa+aa..a的值
#其中a为一个数字

a=input("请输入10以内的一个数字")
n=int(input("加几次"))
res=0
for i in range (n):
    res=res+int(a)
    a=a+a[0]
print('结果是',res)