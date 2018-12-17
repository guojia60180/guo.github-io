#Author guo
'''from selenium import webdriver
browser=webdriver.Chrome()
driver.maximize_window()
'''
from bs4 import BeautifulSoup #解析网页xml
soup=BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)
