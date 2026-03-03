You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_104_code import unique_digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_all_odd_digits(self):
        self.assertEqual(unique_digits([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed_odd_even_digits(self):
        self.assertEqual(unique_digits([135, 246, 879]), [135, 879])

    def test_all_even_digits(self):
        self.assertEqual(unique_digits([2, 4, 6, 8]), [])

    def test_mixed_odd_even_digits_in_list(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_mixed_odd_even_digits_in_list_2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases:

1. `test_all_odd_digits` checks if the function returns the correct list when all digits in the input list are odd.
2. `test_mixed_odd_even_digits` checks if the function correctly identifies and returns a list of numbers that have only odd digits.
3. `test_all_even_digits` checks if the function returns an empty list when all digits in the input list are even.
4. `test_mixed_odd_even_digits_in_list` checks if the function correctly identifies and returns a list of numbers that have only odd digits among a list of numbers with both odd and even digits.
5. `test_mixed_odd_even_digits_in_list_2` checks if the function correctly identifies and returns an empty list when the input list contains numbers with both odd and even digits.

Please note that the function `unique_digits` should be defined in a file named `HumanEval_104_code.py` for these tests to work.