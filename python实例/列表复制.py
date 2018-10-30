#Author guo
#将一个列表的数据复制到另一个列表中

#使用列表切片[:]或者使用copy模块
import copy
a=[1,2,3,4]
b=a#赋值
c=a[:]#浅拷贝
d=copy.copy(a)#浅拷贝
e=copy.deepcopy(a)#深拷贝
'''
浅拷贝

所谓的浅拷贝就是拷贝指向对象的指针,意思就是说:拷贝出来的目标对象的指针和源对象的指针指向的内存空间是同一块空间.
浅拷贝只是一种简单的拷贝,让几个对象公用一个内存,然而当内存销毁的时候,指向这个内存空间的所有指针需要重新定义,不然会造成野指针错误

深拷贝

所谓的深拷贝指拷贝对象的具体内容,其内容地址是自助分配的,拷贝结束之后,内存中的值是完全相同的,但是内存地址是不一样的,两个对象之间相互不影响,也互不干涉.

浅拷贝类似影子，深拷贝类似克隆人
'''
