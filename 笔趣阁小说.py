#Author guo
import requests
import re

# 定义下载小说的类
class download_novel(object):

    def __init__(self, url):
        self.url = url

    #1 获取所有章节的url
    def get_urls(self):
        req = requests.get(self.url).text
        novel_urls = re.findall(r'<dd><a href ="(.*?)">(.*?)</a></dd>',req)[12:]  #去掉前11个更新的章节url
        return novel_urls

    #2 获取每个章节的内容
    def get_content(self, novel_urls):
        html = requests.get(novel_urls).text
        novel_content = re.findall(r'<div id="content" class="showtxt">(.*?)</div>',html)[0]
        novel_content = novel_content.replace('&nbsp;','')
        novel_content = novel_content.replace('<br />','')
        novel_content = novel_content.replace('【感谢大家一直以来的支持，这次起-点515粉丝节的作家荣耀堂和作品总选举，希望都能支持一把。另外粉丝节还有些红包礼包的，领一领，把订阅继续下去！','')
        novel_content = novel_content.replace('请记住本书首发域名：www.biqukan.com。笔趣阁手机版阅读网址：m.biqukan.com','')
        novel_content = novel_content.replace(novel_urls,'')
        return novel_content

    #3 写入文件
    def write_novel(self):
        novel_urls = self.get_urls()
        with open('灵山.txt','w', encoding='utf-8') as f:
            for web in novel_urls:
                novel_title = web[1]
                novel_urls = web[0]
                if 'http' not in web:
                    novel_urls = 'http://www.biqukan.com%s' % web[0]
                novel_content = self.get_content(novel_urls)
                print(novel_urls)
                f.write(novel_title + '\n')
                f.write(novel_content + '\n\n')

# 实例
if __name__ == '__main__':
    url = 'http://www.biqukan.com/24_24889/'
    a = download_novel(url)
    a.write_novel()