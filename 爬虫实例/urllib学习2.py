#Author guo
from urllib.parse import urlparse
from urllib.parse import *
result=urlparse("http://www.baidu.com/index.html;user?id=5#comment")
#对一个url进行解析
print(type(result),
      result,sep='\n')
#输出结果
# <class 'urllib.parse.ParseResult'>
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
#urlunparse()恢复一个url
#urlspilt 不再单独解析params这一个部分，只返回5个结果
#urljoin 生成连接，可以用两个，补全参数
params={
    'name':'germey',
    'age':'22'
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)
#首先声明了一个字典，然后利用urlencode转换为序列get请求参数

#反序列化
#parse_qs()
#quote()对文中的中文进行了URL的编码

keyword='壁纸'
url="https://www.baidu.com/s?wd="+quote(keyword)
print(url)