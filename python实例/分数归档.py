#Author guo
#利用条件算数符学习成绩》=90 A

points=int(input("请输入学生成绩"))
if points>=90:
    grade='A'
elif points<60:
    grade="C"
else:grade='B'

print(grade)

#这个题目要设置边界条件
#设计测试用例
#输入的学生成绩
#1.非数字型 预期期望为输出 输入类型错误
#2.数字型 但》100或者小于0 输入提示范围
#3.输入的为边界值
#4.输入的为小数值 转换为int是可以的，因为只保留整数部分，靠整数部分来进行判定
