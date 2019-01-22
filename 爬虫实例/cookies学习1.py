#Author guo
import requests
from lxml import etree
class Login(object):
    def __init__(self):
        self.headers={
            'Referer':'http://rs.xidian.edu.cn/home.php?mod=spacecp&ac=usergroup',
            'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac Os X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'Host':'rs.xidian.edu.cn'
        }
        self.login_url='http://rs.xidian.edu.cn/home.php?mod=spacecp&ac=usergroup'
        self.post_url='http://rs.xidian.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=Lt4pp&inajax=1'
        self.logined_url='http://rs.xidian.edu.cn/portal.php'
        self.session=requests.Session()

#定义一个登陆类，初始化变量

#session帮助我们维持一个会话，自动处理cookies



    # def token(self):
    #     resonse=self.session.get(self.login_url,headers=self.headers)
    #     selector=etree.HTML()

    def login(self,username,password):
        post_data={
            'formhash': 'c9f59385',
            'username':'小小吓下',
            'password':'guojia60180',
            'questionid': 0,
            'cookietime': 2592000
        }#创建一个表单，以变量的形式进行赋予，request自动处理重定向的信息

        response=self.session.post(self.post_url,data=post_data,headers=self.headers)
        if response.status_code==200:
            self.dynamics(response.text)

        response=self.session.get(self.logined_url,headers=self.headers)
        if response.status_code==200:
            self.profile(response.text)#处理登陆后的个人信息

    def dynamics(self,html):
        selector=etree.HTML(html)
        dynamics=selector.xpath('//div[contains(@class,"news")]//div[contains(@class,"alert")]')
        for item in dynamics:
            dynamic=''.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self,html):
        selector = etree.HTML(html)
        name=selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        username=selector.xpath('//select[@id="user_profile_email"]/option[@value=-""]/text()')
        print(name,username)


if __name__=="__main__":
    login=Login()
    login.login(username='小小吓下',password='guojia60180')