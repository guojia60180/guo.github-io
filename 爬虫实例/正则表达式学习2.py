#Author guo
#search()的使用
import re
#match方法是从匹配的字符串开头开始匹配的，一旦开头匹配不了，整个匹配就会失败

#利用search来扫描整个字符串，返回第一个成功匹配的结果
content='aaaHello 123 4567 World_This is a regex Demo'

result=re.search('Hello\s123\s(\d+)',content)#第一个传入正则表达式，第二个传入要匹配的字符串
print(result)
print(result.span())

#findall方法搜索整个字符串，返回匹配正则表达式的所有内容
#返回列表中 每一个都是元组类型的，根据索引，一次提取
# for result,i in results:
#     print(result)
#     print(result[i])

