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

 import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))

    def test_negative_integers(self):
        self.assertTrue(iscube(-1))
        self.assertFalse(iscube(-8))

    def test_zero(self):
        self.assertTrue(iscube(0))

    def test_non_integer_numbers(self):
        self.assertFalse(iscube(1.5))
        self.assertFalse(iscube(-2.3))

    def test_large_integers(self):
        self.assertTrue(iscube(1000))
        self.assertTrue(iscube(-1000))

    def test_edge_cases(self):
        self.assertTrue(iscube(0))
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(4))
        self.assertFalse(iscube(5))
        self.assertFalse(iscube(6))
        self.assertFalse(iscube(7))
        self.assertFalse(iscube(8))
        self.assertFalse(iscube(9))
        self.assertFalse(iscube(10))

if __name__ == '__main__':
    unittest.main()