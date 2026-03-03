user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return y - 1assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_positive_numbers(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(10, 20), 20)
        self.assertEqual(choose_num(20, 20), -1)
        self.assertEqual(choose_num(1, 2), 2)
        self.assertEqual(choose_num(2, 4), 4)
        self.assertEqual(choose_num(4, 6), 4)
        self.assertEqual(choose_num(5, 7), -1)

    def test_choose_num_negative_numbers(self):
        self.assertEqual(choose_num(-12, -15), -1)
        self.assertEqual(choose_num(-13, -12), -1)
        self.assertEqual(choose_num(-10, -20), -1)
        self.assertEqual(choose_num(-20, -20), -1)
        self.assertEqual(choose_num(-1, -2), -1)
        self.assertEqual(choose_num(-2, -4), -1)
        self.assertEqual(choose_num(-4, -6), -1)
        self.assertEqual(choose_num(-5, -7), -1)

    def test_choose_num_zero(self):
        self.assertEqual(choose_num(0, 0), -1)
        self.assertEqual(choose_num(0, 1), 0)
        self.assertEqual(choose_num(1, 0), -1)

    def test_choose_num_edge_cases(self):
        self.assertEqual(choose_num(1, 1), -1)
        self.assertEqual(choose_num(2, 2), -1)
        self.assertEqual(choose_num(3, 3), -1)
        self.assertEqual(choose_num(4, 4), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes four test methods: `test_choose_num_positive_numbers`, `test_choose_num_negative_numbers`, `test_choose_num_zero`, and `test_choose_num_edge_cases`. Each test method includes several assertions to test the function with different inputs.