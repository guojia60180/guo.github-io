#Author guo

#输入星期几的第一个字母来判断是星期几，如果和第一个字母一样，继续判断第二个

#字典形式进行判断

weekT={'h':'thursday','u':'tuesday'}
weekS={'a':'saturday','u':'sunday'}
week={'t':weekT,'s':weekS,'m':'monday','w':'wedsday','f':'friday'}

a=week[str(input("请输入第一位的字母")).lower()]
if a==weekT or a==weekS:
    print(a[str(input("请输入第二位的字母")).lower()])
else:
    print(a)