system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):
    def test_is_cube(self):
        # Test cases for positive numbers
        self.assertTrue(iscube(1), "iscube(1) should return True")
        self.assertTrue(iscube(8), "iscube(8) should return True")
        self.assertTrue(iscube(27), "iscube(27) should return True")

        # Test cases for negative numbers
        self.assertTrue(iscube(-1), "iscube(-1) should return True")
        self.assertTrue(iscube(-8), "iscube(-8) should return True")
        self.assertTrue(iscube(-27), "iscube(-27) should return True")

        # Test cases for zero
        self.assertTrue(iscube(0), "iscube(0) should return True")

        # Test cases for non-cube numbers
        self.assertFalse(iscube(64), "iscube(64) should return False")
        self.assertFalse(iscube(0), "iscube(0) should return True")
        self.assertFalse(iscube(180), "iscube(180) should return False")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIsCube` class within the `unittest` module, which contains a single method `test_is_cube`. This method tests various scenarios using assertions to ensure the `iscube` function behaves as expected. The `unittest.main()` call at the end runs all the tests in the `TestIsCube` class.