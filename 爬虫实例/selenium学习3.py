#Author guo
import requests
from selenium import webdriver
import time

browser=webdriver.Chrome()
headers={

    'Cookie':'Q8qA_2132_smile=13D1; Q8qA_2132_nofavfid=1; UM_distinctid=166b9c1629f434-0b990ac3c34c7a-5c11301c-1fa400-166b9c162a0f22; Q8qA_2132_saltkey=Pl0F71n7; Q8qA_2132_lastvisit=1544749912; Q8qA_2132_lastcheckfeed=284413%7C1544753587; Q8qA_2132_auth=d128FINfP4k8bvkQ0w1F7NYr7CLIT%2FlQf3IKDQqXMPzZRgij%2FKeW2Yjmsor3S4bwrnXCpZsimQVkoFxUo67RDpvml8Y; Q8qA_2132_myrepeat_rr=R0; Q8qA_2132_home_readfeed=1547039869; Q8qA_2132_sid=cbl3Qf; Q8qA_2132_lip=10.170.70.216%2C1547084105; Q8qA_2132_st_t=284413%7C1547103989%7C4312655570d51304600c275b159e8c28; Q8qA_2132_forum_lastvisit=D_548_1539421065D_165_1540263491D_546_1544516624D_110_1546849268D_217_1546932489D_13_1546932588D_145_1546936087D_106_1547022648D_72_1547103989; Q8qA_2132_ulastactivity=fdb6jHVkBW7qtrV3asjRh3Eho16hlRCFYmEC2MNB4VdgRRVf9gwM; Q8qA_2132_visitedfid=110D72D548D217D554D555D108D144D94D561; Q8qA_2132_st_p=284413%7C1547106060%7C4b34f68bdf1c640b2260d146460ded3e; Q8qA_2132_viewid=tid_984028; Q8qA_2132_sendmail=1; Q8qA_2132_checkpm=1; Q8qA_2132_lastact=1547106462%09misc.php%09patch'
}
browser.get('http://bt.neu6.edu.cn/member.php?mod=logging&action=login&referer=http%3A%2F%2Fbt.neu6.edu.cn%2Fplugin.php%3Fid%3Dneubt_resourceindex%26page%3D2')#请求一个网址url

input=browser.find_element_by_name('username')
input.send_keys('小小吓下')

time.sleep(2)
inputpw=browser.find_element_by_name('password')
inputpw.send_keys('guojia60180')
time.sleep(2)
button=browser.find_element_by_name('loginsubmit')

#button=browser.find_element_by_class_name('btn-search')
button.click()
time.sleep(5)
#print(browser.page_source)

browser.get('https://npupt.com/login.php')
input=browser.find_element_by_name('username')
input.send_keys('xiaoxiaoxia')

time.sleep(2)
inputpw=browser.find_element_by_name('password')
inputpw.send_keys('406334')
time.sleep(2)
button=browser.find_element_by_id('loginbtn')

#button=browser.find_element_by_class_name('btn-search')
button.click()
time.sleep(5)

browser.close()