You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_x_greater_than_y(self):
        self.assertEqual(choose_num(15, 12), -1)

    def test_y_is_even(self):
        self.assertEqual(choose_num(12, 14), 14)

    def test_x_equals_y(self):
        self.assertEqual(choose_num(12, 12), -1)

    def test_x_less_than_y(self):
        self.assertEqual(choose_num(12, 15), 14)

    def test_x_and_y_are_odd(self):
        self.assertEqual(choose_num(13, 13), -1)

    def test_x_and_y_are_even(self):
        self.assertEqual(choose_num(14, 16), 16)

    def test_x_and_y_are_close(self):
        self.assertEqual(choose_num(14, 15), 14)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for all possible scenarios: when x is greater than y, when y is even, when x and y are equal, when x is less than y, when both x and y are odd, when both x and y are even, and when x and y are close.