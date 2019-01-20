#Author guo
#通过csv获取代理
import requests
import random
def check_local_ip(fn, test_url):
    """
    检查存放在本地ip池的代理ip是否可用

    通过读取fn内容,加载每一条ip对test_url进行连接测试,链接成功则储存在 ips_pool.csv 文件中
    :param fn: filename,储存代理ip的文件名
    :param test_url: 要进行测试的ip
    :return: None
    """
    with open(fn, 'r') as f:
        datas = f.readlines()
        ip_pools = []
    for data in datas:
        # time.sleep(1)
        ip_msg = data.strip().split(',')
        http = ip_msg[0]
        host = ip_msg[1]
        port = ip_msg[2]
        proxies = {http: host + ':' + port}
        try:
            res = requests.get(test_url, proxies=proxies, timeout=2)
            if res.status_code == 200:
                ip_pools.append(data)
                print('{0}检测通过'.format(proxies))
                with open('ips_pool.csv', 'a+') as f:
                    f.write(','.join([http, host, port]) + '\n')
        except Exception as e:
            print(e)
            continue

def get_proxies(ip_pool_name='ips_pool.csv'):
    """
    从ip池获得一个随机的代理ip
    :param ip_pool_name: str,存放ip池的文件名,
    :return: 返回一个proxies字典,形如:{'HTTPS': '106.12.7.54:8118'}
    """
    with open(ip_pool_name, 'r') as f:
        datas = f.readlines()
    ran_num = random.choice(datas)
    ip = ran_num.strip().split(',')
    proxies = {ip[0]: ip[1] + ':' + ip[2]}
    return proxies
proxy=get_proxies()
if 'HTTP' in proxy:
    proxies={
    'http':'http://'+proxy['HTTP']

    }
else:proxy={
    'https': 'https://' + proxy['HTTPS']
}
try:
    reponse=requests.get('http://httpbin.org/get',proxies=proxies)
    print(reponse.text)
except requests.exception.ConnectionRefuseError as e:#如果连接报错
    print('Error',e.args)
#输出结果示例
'''{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Cache-Control": "max-age=259200", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.19.1"
  }, 
  "origin": "171.80.136.220", 
  "url": "http://httpbin.org/get"
}'''

