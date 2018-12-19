#Author guo
#请求知乎中一段话 获取相关内容

import requests
import re

#抓取知乎现在的问题选项
headers={
    'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac Os X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'

}
r=requests.get("https://www.zhihu.com/explore",headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(pattern,r.text)
print(titles)