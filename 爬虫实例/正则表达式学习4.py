#Author guo
#正则compile

#将字符串编译成正则对象表达式，以便在以后的匹配中使用
#sub()方法去除字符串中的那些匹配的字
import re

content1='2016-12-15 12:00'
content2='2016-12-17 12:55'
content3='2016-12-22 13:21'
pattern=re.compile('\d{2}:\d{2}')

result1=re.sub(pattern,'',content1)
result2=re.sub(pattern,'',content2)
result1_1=re.findall(pattern,content1)
result3=re.sub(pattern,'',content3)
result2_1=re.findall(pattern,content2)
result3_1=re.findall(pattern,content2)

print(''.join(result1_1)+'\n'+''.join(result1))
print(''.join(result2_1)+'\n'+''.join(result2))
print(''.join(result3_1)+'\n'+''.join(result3))