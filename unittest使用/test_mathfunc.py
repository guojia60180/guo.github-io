#Author guo
#给方法写一个测试用例
import unittest
from mathfunc import*
class TestMathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertEqual(3,add(1,2))

    def test_minus(self):
        self.assertEqual(1,minus(2,1))

    def test_multi(self):
        self.assertEqual(6,multi(2,3))

    def test_divide(self):
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2.5,divide(5,2))

if __name__=='__main__':
    unittest.main(verbosity=2)

