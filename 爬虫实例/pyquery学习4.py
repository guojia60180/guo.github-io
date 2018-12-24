#Author guo
#节点操作

#提供一系列方法，对节点进行动态修改
#为某个节点添加一个class 移除某个节点等
#为提供信息带来极大的便利

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
li=doc('.item-0.active')
print(li)#选中第三个li节点
li.removeClass('active')
print(li)
li.addClass('active')
print(li)#动态的改变class的属性

li.attr('name','link')#调用attr（）来修改属性，第一个参数是属性名，第二个参数是属性值
print(li)
li.text('change item')#修改节点内部内容
print(li)
li.html('<span>changed item</span>')#修改节点内部内容
print(li)
#调用attr后，li节点多个不存在的属性name，值为link，调用text（）方法
#传入文本后，li节点内部文本改为传入的字符串文本
#调用html（）方法，传入HTML文本后，li节点的内部变为HTML文本

#attr（）只传入第一个参数的属性名，获取这个属性，传入第二个参数，可以用来修改属性名

wrap=doc('.wrap')
print(wrap.text())#尝试提取wrap节点的内容
wrap.find('p').remove()
print(wrap.text())

#选中p节点，调用remove方法移除，再利用text（）方法提取