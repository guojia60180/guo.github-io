#Author guo
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy='127.0.0.1:9743'#在本地9743端口上建立HTTP代理服务
#如果是需要认证的代理proxy='username:password@127.0.0.1:9743'
proxy_handler=ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener=build_opener(proxy_handler)#创建一个opener，相当于已经设置好代理隐藏了真实ip
try:
    response=opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# 借助proxyhandler设置代理，参数是字典类型，键名是协议类型，键值是代理
# 当请求连接是https，会调用http代理，生效的代理是127.0.0.1:9743

import socket
import socks
from urllib import request
from urllib.error import URLError

socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9745)
socket.socket=socks.socksocket

try:
    response=request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

#加载本地的SOCKS5代理，运行在8742
#[WinError 10061] 由于目标计算机积极拒绝，无法连接。
#出现这种情况是因为没有花钱