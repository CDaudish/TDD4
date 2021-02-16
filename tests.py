import unittest
import random
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd("a"))

    def test2(self):
        self.assertFalse(check_pwd("1234567"))

    def test3(self):
        self.assertFalse(check_pwd("123"))

    def test4(self):
        self.assertFalse(check_pwd("1234567890123456789012"))

    def test5(self):
        self.assertFalse(check_pwd("123456789012345678901"))

    def test6(self):
        self.assertFalse(check_pwd("AAAAAAAAAA"))

    def test7(self):
        self.assertFalse(check_pwd("aaaaaaaa"))


if __name__ == '__main__':
    unittest.main()
    
