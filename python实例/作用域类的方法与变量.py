#Author guo
#模仿静态变量另一例子

class dummy:
    num=1
    def Num(self):
        print('class dummy num:',self.num)
        print('globa num:',num)
        self.num=self.num+1

n=dummy()
num=1
for i in range(5):
    num=num*10
    n.Num()
