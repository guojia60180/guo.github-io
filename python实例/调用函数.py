#Author guo
def hello(x):
    print(' hello world'*x)

def hello1():
    for i in range(10):
        hello(i)

if __name__=='__main__':
    hello1()