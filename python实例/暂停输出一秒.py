#Author guo
#暂停输出一秒 主要是time模块
import time
for i in range (10):
    print(str(int(time.time()))[-2:])
    time.sleep(1)

#可以引申为一个倒计时器

