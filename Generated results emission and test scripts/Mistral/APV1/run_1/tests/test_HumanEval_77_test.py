You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_77_code import iscube

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
        iscube(1) ==> True
        iscube(2) ==> False
        iscube(-1) ==> True
        iscube(64) ==> True
        iscube(0) ==> True
        iscube(180) ==> False
    '''

    a = abs(a)
    return int(round(a ** (1.0 / 3))) ** 3 == a

 Here is a comprehensive unittest test suite for the given Python function `iscube`:


import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):

    def test_iscube_positive_numbers(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(125))
        self.assertTrue(iscube(216))
        self.assertTrue(iscube(512))
        self.assertTrue(iscube(729))
        self.assertTrue(iscube(1000))

    def test_iscube_negative_numbers(self):
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(-64))
        self.assertTrue(iscube(-125))
        self.assertTrue(iscube(-216))
        self.assertTrue(iscube(-512))
        self.assertTrue(iscube(-729))
        self.assertTrue(iscube(-1000))

    def test_iscube_zero(self):
        self.assertTrue(iscube(0))

    def test_iscube_non_cube_numbers(self):
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(4))
        self.assertFalse(iscube(5))
        self.assertFalse(iscube(7))
        self.assertFalse(iscube(9))
        self.assertFalse(iscube(10))
        self.assertFalse(iscube(11))
        self.assertFalse(iscube(13))
        self.assertFalse(iscube(14))
        self.assertFalse(iscube(15))
        self.assertFalse(iscube(16))
        self.assertFalse(iscube(17))
        self.assertFalse(iscube(19))
        self.assertFalse(iscube(20))
        self.assertFalse(iscube(22))
        self.assertFalse(iscube(23))
        self.assertFalse(iscube(26))
        self.assertFalse(iscube(29))
        self.assertFalse(iscube(30))
        self.assertFalse(iscube(31))
        self.assertFalse(iscube(32))
        self.assertFalse(iscube(33))
        self.assertFalse(iscube(34))
        self.assertFalse(iscube(35))
        self.assertFalse(iscube(36))
        self.assertFalse(iscube(37))
        self.assertFalse(iscube(38))
        self.assertFalse(iscube(39))
        self.assertFalse(iscube(40))
        self.assertFalse(iscube(41))
        self.assertFalse(iscube(42))
        self.assertFalse(iscube(43))
        self.assertFalse(iscube(44))
        self.assertFalse(iscube(45))
        self.assertFalse(iscube(46))
        self.assertFalse(iscube(47))
        self.assertFalse(iscube(48))
        self.assertFalse(iscube(49))
        self.assertFalse(iscube(50))
        self.assertFalse(iscube(53))
        self.assertFalse(iscube(54))
        self.assertFalse(iscube(55))
        self.assertFalse(iscube(56))
        self.assertFalse(iscube(57))
        self.assertFalse(iscube(58))
        self.assertFalse(iscube(59))
        self.assertFalse(iscube(60))
        self.assertFalse(iscube(61))
        self.assertFalse(iscube(62))
        self.assertFalse(iscube(63))
        self.assertFalse(iscube(65))