#Author guo
#选型卡管理

import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')#调用js开启一个选项卡
print(browser.window_handles)#获取当前所有的选项卡返回的是选项卡列表
browser.switch_to_window(browser.window_handles[1])#切换选项卡 利用switch_to_window跳转选项卡
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])#切换至选项卡1
browser.get('https://www.zhihu.com')