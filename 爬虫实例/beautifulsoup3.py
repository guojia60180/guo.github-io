#Author guo
#方法选择器

#API find_all(name.attrs,recursive,text,**kwargs)

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
print(soup.find_all(name='ul'))#返回时列表格式的，长度为2
print(type(soup.find_all(name='ul')[0]))#每个元素都是bs4.element.Tag类型的

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))#由于是Tag类型的，因此可以进行嵌套查询

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)#通过string方法逐个的把li标签下的内容打印出来

print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
#查询时是attrs参数，参数类型是字典类型，查询id是list-1的节点，看符合条件的元素个数
#对于class来说，python是关键字，所以不能直接使用
import re
print(soup.find_all(text=re.compile('link')))
#可以通过正则表达式处理节点文本的组成
