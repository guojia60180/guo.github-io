#Author guo
from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>Hello</p>','lxml')#使用lxml解析器解析
#print(soup.p.string)
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')#使用lxml解析器解析
print(soup.prettify())#以标准的缩进格式输出 （可以自动更正格式 是在初始化对象时就进行了补全）
print(soup.title)
print(type(soup.title))#<class 'bs4.element.Tag'>这个很重要的类型
print(soup.head)
print(soup.title.string)#可以直接选中title结点进行匹配.string 属性就可以得到里面的文本了
print(soup.p)#当选择节点时，选择的是第一个节点，其他后面的节点都会忽略

#提取信息

print(soup.title.name)#name属性获取节点的名称 title节点，调用name就可以得到节点的名称
print(soup.p.attrs)#字典形式，把节点的所有属性和属性值组成一个字典
print(soup.p.attrs['name'])#把其中的一个字典key值输入，得到输出的value值

#嵌套选择
html='''
<html><head><title>The Dormouse's story</title></head>
<body>
'''
soup=BeautifulSoup(html,'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)
#每次返回的类型相同，打印了输出类型




