#Author guo
import requests
import re
from requests.exceptions import RequestException#加入错误处理
import json #进行数据存储
import time#为了每一段时间加载一页
def get_page(url):#输入头信息，代理
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac Os X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'

        }
        response=requests.get(url=url,headers=headers)
        if response.status_code==200:#返回值200表示正常连接
            return response.text
        return None
    except RequestException:
        return response.status_code
def parse_page(html):
    # <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
    pattern1=re.compile('<meta name="keywords.*?content=(.*?)>',re.S)
    pattern2=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
#正则表达式取出实现数据
    item1=re.findall(pattern1,html)
    item2=re.findall(pattern2,html)
    #print(item1)
    #print(item2)
    for item in item2:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3])>3 else '',
            'time':item[4].strip()[5:] if len(item[4])>5 else '',
            'score':item[5].strip()+item[6].strip()
        }#标准化输出，可以用awk来进行优化
def write2file(content):
    with open ("猫眼爬取结果.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
#文件输出部分，把文件转换为txt
def main(offset):#设置偏移量来对不同的URL进行
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_page(url)
    for item in parse_page(html):
        print(item)
        write2file(item)
    #print(html)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(2)


