#Author guo
import selenium
from selenium import webdriver
#API没有提供的功能利用JS的方式来实现
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#将进度条拉到底
#browser.execute_script('alert("To Buttom")')#弹出alert提示框

logo=browser.find_element_by_id('zh-top-link-logo')
print(logo)#<selenium.webdriver.remote.webelement.WebElement (session="39550cf0bdcdf2cd6dbb2cdba3892d03", element="0.5660686560484232-1")>
print(logo.get_attribute('class'))#zu-top-link-logo 找到类名属性
print(logo.text)#与bs4和get_text()方法相同 将其文本值打印出来

input=browser.find_element_by_class_name('zu-top-add-question')
print(input.id)#获取节点id
print(input.location)#获取相对位置
print(input.tag_name)#获取标签名称
print(input.size)#获取节点的大小（宽高）

