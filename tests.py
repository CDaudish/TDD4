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

    def test8(self):
        self.assertFalse(check_pwd("aaaAAAaaaAAA"))

    def test9(self):
        self.assertFalse(check_pwd("aaaAAAaa111"))

    def test10(self):
        self.assertTrue(check_pwd("aaaAAA123-"))


    def test11(self):
        self.assertTrue(check_pwd("aaaAAA123+"))

    def test12(self):
        self.assertTrue(check_pwd("aaaAAA123_"))

    def test13(self):
        self.assertTrue(check_pwd("aaaAAA123)"))

    def test14(self):
        self.assertTrue(check_pwd("aaaAAA123("))

    def test15(self):
        self.assertTrue(check_pwd("aaaAAA123*"))

    def test16(self):
        self.assertTrue(check_pwd("aaaAAA123&"))





if __name__ == '__main__':
    unittest.main()
    

#~`!@#$%^&*()_+-=