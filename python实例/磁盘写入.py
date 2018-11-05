from sys import *

filename=input("输入文件名")
fp=open(filename,'w')
ch=input('输入字符串')
while ch!='#':
    fp.write(ch)
    stdout.write(ch)
    ch=input('')

fp.close()