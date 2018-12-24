#Author guo
#json 文件存储 json全称 javascript object notation

#轻量级的数据交换格式

#对象是在js中拿{}包着的,数据类型是{key1:value1,key2:value2}的key-value键值对结构，key为对象的属性，value为对象值

#数组在JavaScript中是方括号[]包裹的内容，数据结构["java","javascript"]可以使用的索引比较多

#json对象可以在这两个之间无限的记性嵌套，是数据结构的极佳的方式

#读取json

import json
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

print(type(str))#<class 'str'>
data=json.loads(str)#[{'birthday': '1992-10-18', 'gender': 'male', 'name': 'Bob'}, {'birthday': '1995-10-18', 'gender': 'female', 'name': 'Selina'}]
print(data)
print(type(data))#<class 'list'>
#使用loads方法，将字符串转换为了json对象是个列表（原因是最外层是中括号）
#利用索引来获取相关的内容
print(data[0]['name'])#中括号加键名
print(data[0].get('name'))#通过get（）方法传入键名
#！！！！！特别注意，json内的数据一定是要使用双引号来获取的“”

#输出json
#调用dumps（）方法，将json对象转换为字符串

with open ('data.json','w') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii='utf-8'))#indent代表缩进的字符个数，这里代表两个缩进
    #同时需要规定文件的编码类型

