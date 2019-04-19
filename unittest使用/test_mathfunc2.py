#Author guo
#Author guo
import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def setUp(self):
        print( "do something before test.Prepare environment.")

    def tearDown(self):
        print ("do something after test.Clean up.")
        #通过重写了方法
        #这两个方法每次测试方法执行前和执行后分别
        #执行一次，setUp用来准备测试环境，tearDown用来清理环境

    def test_add(self):
        """Test method add(a, b)"""
        print ("add")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        print ("minus")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        print ("multi")
        self.assertEqual(6, multi(2, 3))

    @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        print ("divide")
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))