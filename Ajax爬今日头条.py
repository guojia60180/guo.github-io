#Author guo
import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool
def get_page(offset):#request获取页面的参数
    params={
        'offset':offset,
        'format':'json',
        'keyword':'车',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis'
    }#把url的参数都赋值上
    url='https://www.toutiao.com/search_content/?'+urlencode(params)#转换参数为url
    try:
        reponse=requests.get(url)#get方法得到响应
        if reponse.status_code==200:
            return reponse.json()#将结果转化为json格式
    except requests.ConnectionError:
        return None#链接失败报错

def get_images(json):#构造一个生成器
    if json.get('data'):
        data=json.get('data')
        for item in data:#每一个对象链接
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


def save_image(item):#存取图片
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        reponse=requests.get(item.get('image'))
        if reponse.status_code==200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(reponse.content).hexdigest(),'jpg')#作为摘要返回为16进制字符
            if not os.path.exists(file_path):#如果存在
                with open(file_path,'wb')as f:
                    f.write(reponse.content)
            else:
                print('Aleadydownload',file_path)
    except requests.ConnectionError:
        print('save failed')

def main(offset):#主函数
    json = get_page(offset)#第一个函数得到解析页面json形式传给json
    for item in get_images(json):#通过images函数获取
        #print(item)#可以选择不要
        save_image(item)


GROUP_START = 0#宏定义起始点页面数
GROUP_END = 1#宏定义结束的页面数

if __name__ == '__main__':
    pool = Pool()#利用进程池进行爬取
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)#线程池进行映射，groups进行赋值offset
    pool.close()
    pool.join()#线程运算