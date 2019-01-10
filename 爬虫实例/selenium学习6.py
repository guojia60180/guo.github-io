#Author guo
#延时等待
#需要延时等待一段时间，确保已经加载出来了
#主要有两种 隐式等待 显式等待

#隐式等待 如果selenium没有在DOM中找到节点，继续等待，超出设定时间后，抛出找不到节点的异常
#当查找几点而没有立即出现时，隐式等待将等待一段时间后再查找DOM，默认时间是0

from selenium import webdriver

browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input=browser.find_element_by_class_name('zu-top-add-question')
print(input)

#只固定了一个时间，前页加载的时间会受到网络条件的影响
#显式等待，指定查找的节点，指定一个等待的时间，如果在这个时间内，加载出来了这个节点，就返回查找结点
#如果规定时间内没有加载出该结点，则抛出超时异常

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait#指出最长等待时间
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
wait=WebDriverWait(browser,10)#最长等待时间
input=wait.until(EC.presence_of_element_located((By.ID,'q')))#传入等待的条件 代表结点出现 参数是节点的定位元组
button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))#改为可以点击
print(input,button)#如果十秒内没有加载出来则抛出异常