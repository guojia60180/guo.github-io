#Author guo

#极验二维码识别

#使用网站 https://account.geetest.com/login
import time

from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
EMIAL='aads@asda.com'#用户名
PASSWORD='adsasdsad'#密码
BORDER = 6
INIT_LEFT = 60

class CrackGeetest():
    def __init__(self):
        self.url='https://account.geetest.com/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.email = EMIAL
        self.password=PASSWORD
    def __del__(self):
        self.browser.close()
#模拟点击

    def get_geetest_button(self):
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

#识别缺口

    def get_screenshot(self):
        screenshot=self.browser.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        img=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img geetest_absolute')))
        time.sleep(3)
        location=img.location
        size=img.size
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))#裁剪出来
        captcha.save(name)
        return captcha#返回image对象

    def get_slider(self):
        slider=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider

    #slider=self.get_slider()
    #slider.click()#获取第二张照片

    #对比像素，如果两个相同，对比下一个像素点，像素点不同，则当前位置为缺口位置

    def is_pixel_equal(self,image1,image2,x,y):
        pixel1=image1.load()[x,y]
        pixel2=image2.load()[x,y]
        threshold=60
        if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold:
            return True
        else:
            return False
    def get_gap(self,image1,image2):#获取接口的偏移量
        left=60
        for i in range (left,image1.size[0]):
            for j in range (image1.size[1]):
                if not self.is_pixel_equal(image1,image2,i,j):
                    left=i
                    return left#比较两张图RGB的绝对值是否均小于定义的阈值，绝对值在阈值内，则认为代表像素点相同

#模拟拖动 人机识别重要方式，拖动时需要先加速度高，然后逐渐减慢的过程

    def get_track(self,distance):
        track=[]#移动轨迹
        current=0#当前位移
        mid=distance*4/5#减速阈值
        t=0.2#计算间隔
        v=0#初始速度

        while current<distance:
            if current<mid:
                a=2 #加速度为2
            else:
                a=-3#加速度-3
            v0=v#初始速度
            v=v0+a*t#当前速度
            move=v0*t+1/2*a*t*t#当前位移
            current=current+move
            track.append(round(move))
        return track

#按照轨迹滑动滑块
    def move_to_gap(self,slider,tracks):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(1)
        ActionChains(self.browser).release().perform()

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')
    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)
    def crack(self):
        # 输入用户名密码
        time.sleep(2)
        self.open()
        # 点击验证按钮
        time.sleep(2)
        button = self.get_geetest_button()
        button.click()
        # 获取验证码图片
        image1 = self.get_geetest_image('captcha1.png')
        # 点按呼出缺口
        slider = self.get_slider()
        slider.click()
        # 获取带缺口的验证码图片
        image2 = self.get_geetest_image('captcha2.png')
        # 获取缺口位置
        gap = self.get_gap(image1, image2)
        print('缺口位置', gap)
        # 减去缺口位移
        gap -= BORDER
        # 获取移动轨迹
        track = self.get_track(gap)
        print('滑动轨迹', track)
        # 拖动滑块
        self.move_to_gap(slider, track)

        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        print(success)

        # 失败后重试
        if not success:
            self.crack()
        else:
            self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
