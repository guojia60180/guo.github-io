#Author guo
#使用按位&
#使用按位|

#按位异或^

a=0o77#
x=bin(a)
print(x)
print(bin(a^3))
print(bin(a^3^7))
#设置一个低四位全为1，其余全为0的数
b=1<<4
print(~b)