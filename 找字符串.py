#Author guo
import re
def hasNumbers(inputString):
    return any(char.isdigit() for char in (inputString))

f = open('1.txt','r')
result = list()
for line in open('1.txt'):
    line = f.readline()
    print(line)
    # pattern = re.compile(r'.*\d+')
    # print(pattern.match(line))
    #print(type(line))
    if hasNumbers(line)==True:
        dig=re.findall(r"\d{3}", line)
    #print(type(dig))
        results = list(map(int, dig))
        num=int(''.join([str(t) for t in results]))
        print(num)
    result.append(line)
print (result)
f.close()
'''
1.txt实例
adas123
qwrfasf645
adHFLK142
tttt
sarard795
gfaosjh756
ASDW1QWE23124'''