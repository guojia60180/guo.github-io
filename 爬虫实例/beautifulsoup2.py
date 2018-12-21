#Author guo
#关联选择

#先选择一个节点，以它为基准再选择它的子节点，父节点，兄弟节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.p.contents)#既包含文本，也包含节点，最后以列表的方式统一返回
#列表中每一个元素都是p的直接子节点 第一个a中包含孙子节点span
#contents包含的都是直接子节点

print(soup.p.children)
for i,child in enumerate (soup.p.children):
    print(i,child)
#调用子节点来选择，返回类型是生成器类型的

print(soup.p.descendants)
for i,child in enumerate (soup.p.descendants):
    print(i,child)
#得到所有的子孙节点
#会查询所有的子节点的子节点，循环查找所有的子孙节点

#调用父节点
print(soup.p.parent)
#得到p的父节点是</body>
#parent找的是直接父节点

print(list(enumerate(soup.p.parents)))#是生成器的属性
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
#同时列出数据和数据下标

print('Next Sibling', soup.a.next_sibling)#获取下一个兄弟元素
print('Prev Sibling', soup.a.previous_sibling)#获取上一个兄弟元素
print('Next Siblings', list(enumerate(soup.a.next_siblings)))#返回后面的兄弟节点
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))#返回前面的兄弟节点

#抓取信息主要靠.string 和attrs[]
#调用string来获取文本
#调用attrs来获取属性
#如果返回的是多个节点的生成器，则转化为列表后，取出某个元素，再调用string来活动文本，调用attrs[]来获得属性



