#Author guo
#pyquery选择结果可能是多个节点，类型都是pyquery类型，不会返回beautifulsoup那样的列表形式
from pyquery import PyQuery as pq
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
doc=pq(html)
li=doc('.item-0.active')
print(li)
print(str(li))#对于单个节点的结果，可以直接输出打印，也可以直接转化为字符串

#对于多个节点的结果，需要用遍历来获取
lis=doc('.li').items()#调用items方法生成一个生成器，遍历得到li节点对象
#每个li节点还可以调用前面方法进行选择，查询祖先节点等
print(type(lis))
for li in lis:
    print(li,type(li))
