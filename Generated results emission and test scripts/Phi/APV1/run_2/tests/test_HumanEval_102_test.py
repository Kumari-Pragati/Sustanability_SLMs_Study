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
    return y - 1

 import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_with_even_numbers(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(8, 12), 12)
        self.assertEqual(choose_num(6, 6), -1)

    def test_choose_num_with_odd_numbers(self):
        self.assertEqual(choose_num(11, 15), 14)
        self.assertEqual(choose_num(9, 12), 10)
        self.assertEqual(choose_num(7, 8), 8)
        self.assertEqual(choose_num(5, 5), -1)

    def test_choose_num_with_x_greater_than_y(self):
        self.assertEqual(choose_num(15, 12), -1)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(10, 15), -1)

    def test_choose_num_with_equal_numbers(self):
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(10, 10), -1)

if __name__ == '__main__':
    unittest.main()