system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return int(round(a ** (1.0 / 3))) ** 3 == aassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):

    def test_is_cube(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(180))

    def test_is_cube_edge_cases(self):
        self.assertTrue(iscube(0))
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(-64))
        self.assertTrue(iscube(125))
        self.assertTrue(iscube(-125))
        self.assertTrue(iscube(216))
        self.assertTrue(iscube(-216))

    def test_is_not_cube(self):
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(4))
        self.assertFalse(iscube(5))
        self.assertFalse(iscube(6))
        self.assertFalse(iscube(7))
        self.assertFalse(iscube(8))
        self.assertFalse(iscube(9))
        self.assertFalse(iscube(10))
        self.assertFalse(iscube(11))
        self.assertFalse(iscube(12))
        self.assertFalse(iscube(13))
        self.assertFalse(iscube(14))
        self.assertFalse(iscube(15))
        self.assertFalse(iscube(16))
        self.assertFalse(iscube(17))
        self.assertFalse(iscube(18))
        self.assertFalse(iscube(19))
        self.assertFalse(iscube(20))

if __name__ == '__main__':
    unittest.main()