#Author guo
#输入一行字符，分别统计出其中的英文字母，空格、数字、和其他字符个数

#用is来判断
alp=num=spa=oth=0
string=input("请输入字符串：")
for i in range(len(string)):
    if string[i].isspace():
        spa+=1
    elif string[i].isalpha():
        alp+=1
    elif string[i].isdigit():
        num+=1
    else:
        oth+=1
print("spa:",spa)
print("alp",alp)
print("num",num)
print("oth",oth)