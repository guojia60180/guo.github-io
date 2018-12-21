#Author guo
#CSS选择器

#只需要调用select()方法，传入相应的CSS选择器就可以
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))#选择panel元素下的panel-heading元素
print(soup.select('ul li'))#选择ul节点下的所有li节点
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))#打印输出列表中元素类型

for ul in soup.select('ul'):
    print(ul.select('li'))#支持嵌套选择

#获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])#获取属性，尝试获取每个ul节点的id属性

#获取文本

for li in soup.select('li'):
    print('Get Text:',li.get_text())
    print('String',list.string)#与string方法相同输出

'''
总结一下
1.使用xlms解析库，必要时使用html.parser
2.节点选择筛选功能弱，但是速度快
3.使用find或者find_all 查询匹配单个结果或者多个结果
4.如果使用CSS选择器熟悉，可以使用select方法进行选择
'''