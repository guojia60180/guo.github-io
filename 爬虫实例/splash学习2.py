#Author guo
#execute 强大的接口，与lua脚本的对接
# function main(splash)
#     return 'hello'
# end
#
# 将此脚本转化为URL编码后的字符串，拼接到execute后面
# 通过lua_source参数传递转码后的Lua脚本，通过execute接口获取最终脚本的执行结果

import requests
from urllib.parse import quote

# lua='''
# function main(splash)
#      return 'hello'
# end
# '''
#
# url='http://192.168.99.100:8050/execute?lua_source='+quote(lua)
# reponse=requests.get(url)
# print(reponse.text)

lua='''
function main(splash,args)
    local treat =require("treat")
    local response=splash:http_get("https://httpbin.org/get")
        return {
            html=treat.as_string(reponse.body),
            url=reponse.url,
            status_response.status
        }
end
'''

url='http://192.168.99.100:8050/execute?lua_source='+quote(lua)
reponse=requests.get(url)
print(reponse.text)
#返回格式是json格式，成功的获得了请求的URL，状态码，网页源代码