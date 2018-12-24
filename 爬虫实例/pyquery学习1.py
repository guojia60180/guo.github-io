#Author guo
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
#doc=pq(filename='demo.html')#可以文件的方式直接传递文件名解析
print(doc('li'))#选择URL可以选择所有的li节点

#基本的CSS选择的方法
print(doc('#container .list li'))#选取id为contaniner的节点，再从内部的class为list的节点内部的所有的li节点，打印输出
print(type(doc('#container .list li')))#类型是pyquery类型

#查询函数和jquery相同
items=doc('.list')
print(type(items))
print(items)
lis=items.find('li')
print(type(lis))
print(lis)
#find查找范围时节点的所有子孙节点，如果只查找子节点，可以用children()方法

#parent（）方法获取某个节点的父节点
container= items.parent()
print(type(container))#<class 'pyquery.pyquery.PyQuery'>还是该类型的
print(container)
#获得祖先节点可以使用parents（）方法

#兄弟节点
li=doc('.list .item-0.active')
print(li.siblings())#兄弟节点，向其中传入CSS选择器就可以从所有兄弟节点中挑选出符合条件的节点了

