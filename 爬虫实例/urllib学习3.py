#Author guo
#完成打开一个url 是否有产出，出现错误，显示出出错原因
from urllib import request,error

try:
    reponse=request.urlopen("http://cuiqingcai.com/index.htm")

except error.HTTPError as a:
    print(a.reason,a.code,a.headers,sep=' ')#作为urlerror的子类，只负责处理http的请求错误
except error.URLError as a:
     print(a.reason)
else:
    print("requst success")#先捕获httperror 再捕获urlerror 输出错误原因

#reason返回值有可能是一个对象，因此使用isinstance来判断会更好