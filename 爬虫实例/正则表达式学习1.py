#Author guo
import re

content='Hello 123 4567 World_This is a regex Demo'

result=re.match('Hello\s123\s(\d+)',content)#第一个传入正则表达式，第二个传入要匹配的字符串
print(result)
print(result.group())
print(result.group(1))#找到括号中的匹配项
print(result.span(1))#找到括号中的下标
result2=re.match('^Hello(.*)Demo$',content)
print(result2.group())
print(result2.group(1))#找到括号中的匹配项
print(result2.span(1))#找到括号中的下标

#使用（）把想提取的子字符串括起来（）实际上标明
'''
贪婪和非贪婪
在贪婪匹配下，.*会匹配尽可能多的字符
非贪婪匹配则是.?*会匹配尽可能少的字符

'''

#加入修饰符
#re.S#匹配换行等字符
#re.I#对匹配大小写不敏感
content='''Hello 123 4567 World_This 
         is a regex Demo'''
result2=re.match('^Hello(.*)Demo$',content,re.S)
print(result2.group())
print(result2.group(1))#找到括号中的匹配项
print(result2.span(1))#找到括号中的下标
#转义匹配

content='(百度)www.baidu.com'
result=re.match('\(百度\)www\.baidu\.com',content)#通过转义.来进行匹配的过程
print(result)