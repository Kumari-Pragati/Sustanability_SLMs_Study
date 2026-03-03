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

 Here is a unittest test script for the `iscube` function:


import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):
    def test_iscube(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(180))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(-27))
        self.assertFalse(iscube(126))
        self.assertTrue(iscube(125))
        self.assertFalse(iscube(129))
        self.assertFalse(iscube(-129))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `iscube` function with various positive and negative integers. The `test_iscube` method contains multiple assertions to check the function's behavior for different inputs. If you run this script, it will execute the tests and print the results.