You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


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


This script includes four test methods:

- `test_positive_cubes` tests the function with positive cube numbers.
- `test_negative_cubes` tests the function with negative cube numbers.
- `test_non_cubes` tests the function with numbers that are not cubes.
- `test_zero` tests the function with zero, which is a cube.

Each test method uses the `assertTrue` method to check that the function returns `True` for the expected inputs and the `assertFalse` method to check that the function returns `False` for the expected inputs.

Please note that the `HumanEval_77_code` module and the `iscube` function should be defined in a separate Python file in your project.