#Author guo
#Author guo
import lxml
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)#自动修正html文本
result = etree.tostring(html)#结果是bytes格式的
print(result.decode('utf-8'))#decode方法变为string

#如果用txt进行解析，则会多一个头
'''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
'''

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//*')#取出全部的
print(result)
result=html.xpath('//li')
print(result)
for result1 in result:
    print(result1)#输出所有的li节点

result=html.xpath('//li/a')
print(result)
for result1 in result:
    print(result1)#输出所有的li节点a子节点
#//获取子孙节点 /获取子节点

#属性获取
html = etree.parse('./test.html', etree.HTMLParser())
print('属性获取')
result=html.xpath('//li/a/@href')
print(result)
#@获得节点的href值

#属性多值匹配
#属性有两个值

text='''
<li class='li li-first'><a href='link.html'>first item</a></li>
'''

html=etree.HTML(text)
result=html.xpath('//li[@class="li"]/a/text()')
print(result)#输出【】无法完成匹配

#使用contains（）函数
result=html.xpath('//li[contains(@class,"li")]/a/text()')#contains 第一个传入属性名称，第二个参数传入属性值
print(result)

#多属性匹配
#利用and相连

#按顺序选择
#插入索引
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

