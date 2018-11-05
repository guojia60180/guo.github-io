#Author guo
class student:
    x=0
    c=0
def f(stu):
    stu.x=20
    stu.c='c'

a=student()
a.x=3
a.c='b'
print(a.x,a.c)
f(a)
print(a.x,a.c)