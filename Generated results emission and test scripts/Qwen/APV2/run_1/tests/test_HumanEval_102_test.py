system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_102_code import choose_num
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


assistant

import unittest

# Function to be tested
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        # Test cases covering different scenarios
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(14, 16), 16)
        self.assertEqual(choose_num(17, 18), -1)
        self.assertEqual(choose_num(19, 18), -1)

    def test_edge_cases(self):
        # Edge case where x equals y
        self.assertEqual(choose_num(10, 10), -1)
        # Edge case where y is less than x
        self.assertEqual(choose_num(15, 12), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `choose_num` function behaves as expected across various inputs, including edge cases.