#Author guo
'''
function main(splash, args)
  local example_urls={"www.baidu.com","www.taobao.com","www.zhihu.com"}
  local urls=args.urls or example_urls
  local results={}
  for index,url in ipairs(urls) do
    local ok,reason=splash:go("https://"..url)
    if ok then
      splash:wait(2)
      results[url]=splash:png()
    end
  end
  return results
end
lua脚本 支持异步处理 在wait方法中等待时别的生成截图并返回
return的方法主要有
{
html=splash:html()
png=splash:png()
har=splash:har()
}
生成一个报告
'''
#splash API的调动
import requests
url='http://192.168.99.100:8050/render.html?url=https://www.baidu.com'#给接口传递一个url参数来指定渲染的url
#返回页面渲染后的源码
reponse=requests.get(url)
print(reponse.text)
#当然url中也可以添加一些参数
# x='&wait=5'
# url=[url,x]
#
# reponse=requests.get(''.join(url))
# print(reponse.text)
#也可以返回png，jepg，har等数据


