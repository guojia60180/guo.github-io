#Author guo
#利用selenium抓取淘宝产品并使用pyquery解析得到商品的图片，名称价格购买人数
#保存至MongoDB

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
keyword='三只松鼠'

def index_page(page):
#抓取索引页
    print('抓取',page,'页')
    try:
        url='https://s.taobao.com/search?q='+quote(keyword)
        browser.get(url)
        if page>1:
            input=wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-page div.form > input')))
            submit=wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div,form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'mainsrp-pager li.item.active > span'),
            str(page))
        )
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .item .item')))
        get_produce()
    except TimeoutException:
        index_page(page)

def get_produce():
    #提取商品数据
    html=browser.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .item .item').items()
    for item in items:
        product={
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'loaction':item.find('.location').text(),

        }
        print(product)
        save_to_mongo(product)
import pymongo
mongourl='127.0.0.1'
mongodb='taobao'
mongo_collection='products'

client=pymongo.MongoClient(mongourl,port=27017)
db=client[mongodb]
def save_to_mongo(result):
    try:
        if db[mongo_collection].insert(result):
            print('成功存储')

    except Exception:
        print('存储失败')

MAX_page=10
def main():
    for i in range(1,MAX_page+1):
        index_page(i)

main()