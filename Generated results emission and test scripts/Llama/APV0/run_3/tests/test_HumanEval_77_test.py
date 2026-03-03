user

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
    return int(round(a ** (1.0 / 3))) ** 3 == aassistant

Here is the unittest test script for the `iscube` function:

import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):
    def test_positive_cubes(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(125))
        self.assertTrue(iscube(216))

    def test_negative_cubes(self):
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(-64))
        self.assertTrue(iscube(-125))
        self.assertTrue(iscube(-216))

    def test_non_cubes(self):
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(4))
        self.assertFalse(iscube(5))
        self.assertFalse(iscube(6))
        self.assertFalse(iscube(7))
        self.assertFalse(iscube(180))

    def test_zero(self):
        self.assertTrue(iscube(0))

if __name__ == '__main__':
    unittest.main()

This script defines a `TestIsCube` class that contains four test methods:

* `test_positive_cubes`: Tests that the function returns `True` for positive integers that are cubes (e.g. 1, 8, 27, etc.).
* `test_negative_cubes`: Tests that the function returns `True` for negative integers that are cubes (e.g. -1, -8, -27, etc.).
* `test_non_cubes`: Tests that the function returns `False` for integers that are not cubes (e.g. 2, 3, 4, etc.).
* `test_zero`: Tests that the function returns `True` for the integer 0, which is a special case.

Each test method uses the `assertTrue` or `assertFalse` method to verify that the function returns the expected result for a given input.

To run the tests, simply execute the script. The `unittest` module will automatically discover and run the tests.