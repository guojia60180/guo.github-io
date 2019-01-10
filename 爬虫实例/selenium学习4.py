#Author guo
#动作链
#交互作用都是针对某个节点进行的
#还有一些操作，他们没有特定的执行对象，比如鼠标拖拽，键盘按键
#这些通过动作链来执行

from selenium import webdriver
from selenium.webdriver import ActionChains

url='https://www.runoob.com/try/try.php?filename=jquery-api-droppable'
browser=webdriver.Chrome()
browser.get(url)

browser.switch_to.frame('iframeResult')#switch_to.frame()用来切换层的，有时候页面元素会定位不到
source=browser.find_elements_by_css_selector('#draggable')#选择源节点
target=browser.find_elements_by_css_selector('#droppable')#选择目的节点
actions=ActionChains(browser)#实例化一个动作
actions.drag_and_drop(source,target)#拖拽操作实行
actions.perform()#展示

