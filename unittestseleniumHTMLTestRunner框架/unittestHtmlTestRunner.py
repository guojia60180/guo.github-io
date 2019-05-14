#Author guo
import unittest
import HTMLTestRunner
import chromegetselenium

class MyTestCase(unittest.TestCase):

    #初始化
    def setUp(self):
        pass

    #退出
    def tearDown(self):
        pass

    #测试用例
    def test_case1(self):
        self.assertMultiLineEqual(chromegetselenium.baiducase1(),u'百度一下，你就知道')

    def test_case2(self):
        self.assertMultiLineEqual(chromegetselenium.baiducase2(),u'京公网安备11000002000001号')

def Suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(MyTestCase('test_case1'))
    suiteTest.addTest(MyTestCase('test_case2'))
    return suiteTest

if __name__=='__main__':
    #生成路径
    filepath='resultHTML.html'
    f=open(filepath,'wb')

    #title 描述

    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='testreport',description='百度的测试报告')

    runner.run(Suite())