#Author guo

#异常处理

#会报错 使用try except来捕获异常

from selenium import webdriver

browser=webdriver.Chrome()

#browser.find_element_by_id('hello')
#报错selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"hello"}

from selenium.common.exceptions import TimeoutException,NoSuchElementException#时间和无节点的异常处理

try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('timeout')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('NO element')

finally:
    browser.close()