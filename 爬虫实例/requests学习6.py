#Author guo
import requests

s=requests.get('http://httpbin.org/cookies/set/number/123456789')
r=requests.get('http://httpbin.org/cookies')
print(r.text)
#请求网址并设置了一个cookie值，名称叫做number值是123456789
#随后请求了现在的cookie
#发现并不相同

#利用session来完成该方法
s=requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r=s.get('http://httpbin.org/cookies')
print(r.text)
#利用session完成在模拟一个会话不同担心cookie的问题
