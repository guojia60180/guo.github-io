#Author guo
'''from selenium import webdriver
browser=webdriver.Chrome()
driver.maximize_window()
'''
from bs4 import BeautifulSoup #解析网页xml
soup=BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)
# from PIL import Image
# import tesserocr
# print(tesserocr.image_to_string(Image.open('test.png')))
# print(tesserocr.image_to_string(Image.open('test-european.jpg'), lang='fra'))