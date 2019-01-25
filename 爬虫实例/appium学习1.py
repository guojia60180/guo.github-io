#Author guo
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'
# desired_caps['platformVersion'] = '6.0.1'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'G6' # 连接多个设备才有用
# desired_caps['app'] = r'e:\apk\toutiao.apk'#如果已经安装好软件乐意不需要，这边填写的是apk在电脑上的路径
desired_caps['appPackage'] = 'com.android.chrome' # app的包名，唯一标志app
desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity t81' # 对应安卓应用的操作界面
desired_caps['unicodeKeyboard'] = True # 安装一个中文的输入法
desired_caps['resetKeyboard'] = True #
desired_caps['noReset'] = True # 清除元素数据，跳过初始页面
desired_caps['newCommandTimeout'] = 6000
desired_caps['automationName'] = 'uiautomator2'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.android.chrome:id/url_bar").click()
time.sleep(1)
# driver.find_element_by_id("com.wali.knights:id/search").click()
# time.sleep(2)
# driver.find_element_by_id("com.wali.knights:id/search_edit").clear()
# driver.find_element_by_id("com.wali.knights:id/search_edit").send_keys('appium test')

# driver.find_element_by_id("float_search_or_cancel").click()
# driver.find_element_by_id("floating_action_button").click()

driver.quit()