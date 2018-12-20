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

result = html.xpath('//ul/a')
print(result)

result=html.xpath('//a[@href="link4.html"]/../@class')#先选中herf属性是这个的a节点，找其父节点，然后找class属性
print(result)

result = html.xpath('//li[@class="item-0"]')
print(result)#进行属性匹配的得到返回的两个匹配到的元素

result = html.xpath('//li[@class="item-0"]/a/text()')#一种是先选取a节点再获取文本
print(result)

result = html.xpath('//li[@class="item-0"]//text()')#另一种//获取该文本内所有字符
print(result)


