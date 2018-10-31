#Author guo
#利用递归函数调用，将所输入的5个字符，相反的顺序打印出来

def recieve(string):
    if len(string)!=1:
        recieve(string[1:])
    print(string[0],end='')

recieve(input("请输入输入的字符串"))