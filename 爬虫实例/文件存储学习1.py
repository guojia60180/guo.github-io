#Author guo
#知乎，利用request把网页源码获取下来，利用pyquery进行解析，接下来提取标题
#回答者，回答保存文本

import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/explore'
headers={
    'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_3)AppleWebKit/573.36 (KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}#设置代理头，防止出现问题
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    questions=item.find('h2').text()
    author=item.find('.author-link-line').text()#找到author-link-line标签，把中间的说明文档写出来这样来的到
    answer=pq(item.find('.content').html()).text()#同样找到相关的内容
    file=open('explore.txt','a',encoding='utf-8')#叠加的方式，使得不会被覆盖
    file.write('\n'.join([questions,author,answer]))#把这些重合起来，并输出到文档里
    file.write('\n'+'='*50+'\n')#在问题的提出过程中，每一个要加入一个50个等于号的情况来作为间隔符
    file.close()

#打开文件的方式
'''
with open('explore.txt','a',encoding='utf-8')as file:
    file.write('\n'.join([questions,author,answer])
    file.write('\n'+'='*50+'\n')
'''

