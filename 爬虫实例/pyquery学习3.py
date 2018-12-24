#Author guo
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc=pq(html)
a=doc('.item-0.active a')#选中class为item-0和active的内的a节点
print(a,type(a))
print(a.attr('href'))#调用attr方法来求属性 传入属性的名称
print(a.attr.href)#调用attr的属性来获取属性值
#该方法较大的弊端是只能获取第一个节点的属性

#如果具有多个属性，需要进行遍历
a=doc('a')
for item in a.items():
    print(item.attr('href'))
#调出所有的属性出来

#获取文本
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc=pq(html)
a=doc('.item-0.active a')#选中一个a节点，
print(a)
print(a.text())#调用text方法，获取内部文本信息，忽略节点内部包含的所有HTML，只返回文字内容

#要获取节点内部的HTML文本，就要使用html方法

print(a.html())#<span class="bold">third item</span>显示html信息

#如果选择结果十多个节点，分别返回内容
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc = pq(html)
li = doc('li')
print(li.html())#html方法返回第一个节点li节点内部的HTML文本
#<a href="link2.html">second item</a>
print(li.text())#text方法返回所有li节点内部的纯文本，中间用一个空格分隔开，是字符串形式
#second item third item fourth item fifth item
print(type(li.text()))#text方法不需要遍历就可以获取，将所有节点取文本合并形成一个字符串

