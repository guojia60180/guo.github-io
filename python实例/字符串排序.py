#Author guo
#安一部分排序
a = ["John Smith", "Alice Young", "John Scott Brown"]
a.sort(key=lambda x:x.split()[-1])

#a.sort(key=len)按照长度排序

