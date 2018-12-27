#Author guo
import os
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.weibo.com/carnalness?is_hot=1',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'SINAGLOBAL=1454697051433.4001.1504513715024; _s_tentry=rs.xidian.edu.cn; Apache=5820869191616.697.1545873833879; ULV=1545873834352:571:24:4:5820869191616.697.1545873833879:1545806495672; login_sid_t=151fc2616449a068a9758ca5df00b284; cross_origin_proto=SSL; Ugrow-G0=57484c7c1ded49566c905773d5d00f82; TC-V5-G0=06f20d05fbf5170830ff70a1e1f1bcae; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W58qx1z6mCflJzZd37NNAAu5JpX5K2hUgL.FoeNSKBfS0efSo52dJLoIEBLxK-LBo5L12qLxK-LBo5L12qLxK-L1K5L1KeLxKBLBonL12zt; ALF=1577413980; SSOLoginState=1545877985; SCF=AmNDWxSyO74S8fpruQi0Uv6eCb47Zxc501OvDQ6s230VdlV0QFKvGfXbulBouvWT_HgLIzioysTXl7Kmo_cOfug.; SUB=_2A25xIEmyDeRhGeVJ7lYU9y3JzTyIHXVSVDx6rDV8PUNbmtBeLWvZkW9NT_eX9R2EObcb8WdGx4rj6Sbj2yKFdaU_; SUHB=0XDVvAJTZn9mYk; un=15529200391; wvr=6; YF-V5-G0=fec5de0eebb24ef556f426c61e53833b; YF-Page-G0=854ebb7f403eecfa60ed1f0e977c6825; wb_view_log_3754573560=1920*10801; TC-Page-G0=8dc78264df14e433a87ecb460ff08bfe; UOR=rs.xidian.edu.cn,widget.weibo.com,www.google.com.hk'
}#登录自己的cookies



def main():

    if not os.path.exists('pic'):
        os.mkdir('pic')#创建一个文件夹存储pic

    for i in range(0, 10):
        for j in range(0, 2):
            url = 'https://www.weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_hot=1&pagebar=%s&pl_name=Pl_Official_MyProfileFeed__19&id=1005055626547919&script_uri=/carnalness&feed_type=0&page=%s&pre_page=%s&domain_op=100505&__rnd=1545901101456' % (str(j), str(i), str(i))
            #获取url 通过开发者工具 ajax来获得 选择xhr变化的值，找到变化的值，在这里用%s来替代传入参数
            print(url)
            res = requests.get(url, headers=headers)
            res_data = res.json()#转化为json格式
            html = res_data['data']
            soup = BeautifulSoup(html, 'html.parser')#解析html
            # print(soup.prettify())  # 格式化html内容
            ul_list = soup.select('.WB_detail .media_box ul')#找到这两个标签内的地址
            for ul in ul_list:
                # print(ul)
                action_data = ul.attrs.get('action-data', '')#得到属性值
                for item in action_data.split('&'):#取出里面的&
                    if 'clear_picSrc' in item:
                        pic_urls = item.split('=')[1].replace('%2F', '/').split(',')
                        for pic_url in pic_urls:
                            pic_name = pic_url.split('/')[-1]
                            res_of_pic = requests.get('http:' + pic_url)#得到图片的地址
                            if res_of_pic.status_code == 200:#如果返回时可以连接的正常通信状态
                                with open('pic/' + pic_name, 'wb') as f:
                                    f.write(res_of_pic.content)#把图片信息写入
                                    print('抓取成功', pic_name)


if __name__ == '__main__':
    main()