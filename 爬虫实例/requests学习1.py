#Author guo
import requests

r=requests.get("https://www.baidu.com")#与urlopen相同
print(type(r))#看类型<class 'requests.models.Response'>
print(r.status_code)#状态信息 200
print(type(r.text))#响应体类型str
print(r.text)#响应体内容
print(r.cookies)#cookies类型是cookiejar
#同时可以实现post。put。delete等请求

data={
    'name':'guo',
    'age':22
}
r=requests.get("http://httpbin.org/get",params=data)
print(r.text)#是json格式的str 转化为字典若不是json的就会报错

