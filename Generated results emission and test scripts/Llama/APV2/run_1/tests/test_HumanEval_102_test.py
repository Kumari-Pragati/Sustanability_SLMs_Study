system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return y - 1assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_positive_numbers(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(14, 16), 16)
        self.assertEqual(choose_num(16, 18), 18)
        self.assertEqual(choose_num(20, 22), 20)

    def test_choose_num_negative_numbers(self):
        with self.assertRaises(ValueError):
            choose_num(-1, 1)
        with self.assertRaises(ValueError):
            choose_num(1, -1)

    def test_choose_num_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            choose_num(1.5, 2.5)
        with self.assertRaises(TypeError):
            choose_num(1, 2.5)

if __name__ == '__main__':
    unittest.main()