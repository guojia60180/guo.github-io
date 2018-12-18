#Author guo
from urllib import request,parse

url="http://httpbin.org/post"
headers={
    "User-Agent":"Mozilla/4.0(compatible;MSIE 5.5;Windows NT)",#伪装自己是火狐
    "Host":"httpbin.org"
}
dict={
    "name":"Germey"
}
data=bytes(parse.urlencode(dict),encoding="utf-8")#传入的data数据必须是byte比特流形式的
req=request.Request(url=url,data=data,headers=headers,method="POST")#指出请求方式是Post
#利用request.Requesr 来完成请求的构造
reponse=request.urlopen(req)

print(reponse.read().decode('utf-8'))