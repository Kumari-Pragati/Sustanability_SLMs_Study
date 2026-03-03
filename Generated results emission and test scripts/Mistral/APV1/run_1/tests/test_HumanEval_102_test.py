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

 Here is a comprehensive unittest test suite for the `choose_num` function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):
    def test_choose_num_within_range(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(10, 12), 10)
        self.assertEqual(choose_num(5, 8), 6)

    def test_choose_num_even_number(self):
        self.assertEqual(choose_num(14, 16), 14)
        self.assertEqual(choose_num(10, 12), 10)
        self.assertEqual(choose_num(6, 8), 6)

    def test_choose_num_outside_range(self):
        self.assertEqual(choose_num(1, 10), -1)
        self.assertEqual(choose_num(15, 10), -1)
        self.assertEqual(choose_num(10, 5), -1)

    def test_choose_num_same_numbers(self):
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(5, 5), -1)

    def test_choose_num_negative_numbers(self):
        self.assertEqual(choose_num(-1, 10), -1)
        self.assertEqual(choose_num(10, -1), -1)
        self.assertEqual(choose_num(-1, -1), -1)

    def test_choose_num_zero(self):
        self.assertEqual(choose_num(0, 10), -1)
        self.assertEqual(choose_num(10, 0), -1)
        self.assertEqual(choose_num(0, 0), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as:

1. When the number is within the range and even.
2. When the number is within the range but odd.
3. When the numbers are outside the range.
4. When the numbers are the same.
5. When the numbers are negative.
6. When the numbers are zero.

Each test case uses the `assertEqual` method to compare the expected output with the actual output of the `choose_num` function. If the function returns the correct output, the test case passes; otherwise, it fails.