#Author guo
#模仿静态变量的用法

def dummy():
    i=0
    print(i)
    i=i+1

class cls:
    i=0
    def dummy(self):

        print(self.i)
        self.i=self.i+1

a=cls()
for i in range (50):
    dummy()
    a.dummy()

#方法是需要实例化的，是面向对象的