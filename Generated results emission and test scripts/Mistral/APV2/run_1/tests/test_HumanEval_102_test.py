You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `choose_num` function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_within_range(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(10, 12), 12)
        self.assertEqual(choose_num(4, 6), 6)

    def test_choose_num_outside_range(self):
        self.assertEqual(choose_num(1, 10), -1)
        self.assertEqual(choose_num(15, 20), -1)
        self.assertEqual(choose_num(0, 5), -1)

    def test_choose_num_odd_numbers(self):
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(15, 13), -1)
        self.assertEqual(choose_num(5, 3), -1)

    def test_choose_num_same_numbers(self):
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(5, 5), -1)
        self.assertEqual(choose_num(0, 0), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_choose_num_within_range` checks that the function correctly returns the biggest even number within the given range.
2. `test_choose_num_outside_range` checks that the function correctly returns -1 when the numbers are outside the given range.
3. `test_choose_num_odd_numbers` checks that the function correctly returns -1 when the numbers are odd and there is no even number in the given range.
4. `test_choose_num_same_numbers` checks that the function correctly returns -1 when the numbers are the same.