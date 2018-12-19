#Author guo
import requests
import re

#抓取二进制数据得到视频图片等

r=requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
with open('favorite.ico','wb') as f:
    f.write(r.content)
#存取github的图标