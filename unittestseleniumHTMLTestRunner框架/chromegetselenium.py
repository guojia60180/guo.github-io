#Author guo

from selenium import webdriver

browser=webdriver.Chrome()

browser.maximize_window()

browser.get('http://www.baidu.com')

def baiducase1():
    title=browser.title
    return title

def baiducase2():
    jg=browser.find_element_by_id('jgwab').text
    return jg

