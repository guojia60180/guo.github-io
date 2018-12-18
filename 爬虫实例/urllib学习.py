#Author guo
import urllib.request
response=urllib.request.urlopen('https://www.baidu.com')#完成抓取源代码
#具有很多参数data
#print(type(response))
#<class 'http.client.HTTPResponse'>类对象 因此包含很多方法

print(response.status)#返回结果的状态码200表示成功，404表示网页未找到，500表示服务器内部错误

print(response.getheaders())#响应的头信息

print(response.getheader('Server'))#传递一个参数获得值，看服务器使用什么搭建的
#python.org 是NGINX 百度隐藏了自己的BWS/1.1

print(response.read().decode("utf-8"))

