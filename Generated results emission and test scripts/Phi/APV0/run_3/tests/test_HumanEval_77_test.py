Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_non_cube_integers(self):
        self.assertFalse(iscube(180))
        self.assertFalse(iscube(27))  # This should be False because 27 is a cube, but we want to test non-cubes

    def test_zero(self):
        self.assertTrue(iscube(0))

    def test_edge_cases(self):
        self.assertTrue(iscube(1000))  # Large positive cube
        self.assertTrue(iscube(-1000))  # Large negative cube

if __name__ == '__main__':
    unittest.main()