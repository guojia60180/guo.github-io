#Author guo
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')#请求一个网址url
#查找节点
input_first=browser.find_element_by_id('q')#通过元素查找
input_second=browser.find_element_by_css_selector('#q')#CSS
input_third=browser.find_element_by_xpath('//*[@id="q"]')#xpath查找
print(input_first,
      input_second,
      input_third)
lis=browser.find_elements_by_css_selector('.service-bd li')
print(lis)#获取所有的结点并输出
#print(browser.page_source)#输出该网页源码

input=browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(2)
input.clear()
input.send_keys('ipad')
button=browser.find_element_by_class_name('btn-search')
button.click()
#browser.close()#实现浏览器驱动并获取网页源码


