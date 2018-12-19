#Author guo
#post请求

import requests
data={
    'name':'guo','age':22
}
r=requests.post("http://httpbin.org/post",data=data)
print(r.text)
'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "22", 
    "name": "guo"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "15", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.19.1"
  }, 
  "json": null, 
  "origin": "113.140.11.123", 
  "url": "http://httpbin.org/post"
}'''