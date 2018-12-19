#Author guo
#sub（）方法实现每日知乎火热话题
import re
import requests
#抓取知乎现在的问题选项
headers={
    'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac Os X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'

}
r=requests.get("https://www.zhihu.com/explore",headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(pattern,r.text)
x='''['\n人什么时候会试图反抗大脑？\n', '\n苏联究竟发达到什么程度？\n', '\n哪些时候有让你想掐死你家狗子的冲动？\n', '\n实体店是不是越来越难赚钱了？\n', '\n如何看待杨超越粉丝群体的特殊构成？\n', '\n如何评价《海贼王》第925话？\n', '\n什么时候你觉得家长对抑郁症的理解很少？\n', '\n你觉得《三体》中最残忍的一句话是什么？\n', '\n怎样看待华晨宇说自己做音乐的天赋占百分之九十九，努力占百分之一？\n', '\n英雄联盟中有哪些冷知识？\n']'''

print(titles)
results=re.findall('\n(.*?)\n',"".join(titles))

for i,result in enumerate(results):

    print("排名%s 问题%s" % (i + 1, result))

