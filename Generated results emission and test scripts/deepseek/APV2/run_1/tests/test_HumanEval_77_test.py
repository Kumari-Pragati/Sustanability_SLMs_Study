You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return int(round(a ** (1.0 / 3))) ** 3 == a


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_77_code import iscube

class TestIscube(unittest.TestCase):

    def test_positive_cubes(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(125))

    def test_negative_cubes(self):
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(-64))
        self.assertTrue(iscube(-125))

    def test_non_cubes(self):
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(4))
        self.assertFalse(iscube(5))
        self.assertFalse(iscube(6))
        self.assertFalse(iscube(7))
        self.assertFalse(iscube(9))
        self.assertFalse(iscube(10))
        self.assertFalse(iscube(11))
        self.assertFalse(iscube(12))

    def test_zero(self):
        self.assertTrue(iscube(0))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive cubes, negative cubes, non-cubes, and the case where the input is zero. It uses the `assertTrue` method to check that the function returns `True` for valid inputs and `assertFalse` to check that it returns `False` for invalid inputs.