#Author guo
#requests 代理设置更简单，只需要传入proxies参数就可以了

import requests
proxy='127.0.0.1:9743'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy
}
try:
    reponse=requests.get('http://httpbin.org/get',proxies=proxies)
    print(reponse.text)
except requests.exception.ConnectionRefuseError as e:#如果连接报错
    print('Error',e.args)

