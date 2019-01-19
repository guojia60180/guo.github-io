#Author guo
from selenium import webdriver

proxy='127.0.0.1:9743'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
browser=webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')

#如果是认证代理会比较复杂
#需要在本地创建一个mainfest.json文件和background.js脚本来设置认证代理
#运行代码后本地会生成一个proxy_auth_plugin.zip文件来保存当前设置

