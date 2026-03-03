You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits_with_odd_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_unique_digits_with_no_odd_digits(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_unique_digits_with_single_odd_digit(self):
        self.assertEqual(unique_digits([11, 23, 45, 6]), [11, 23, 45])

    def test_unique_digits_with_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_unique_digits_with_negative_numbers(self):
        self.assertEqual(unique_digits([-15, -33, -1422, -1]), [])

    def test_unique_digits_with_non_integer_numbers(self):
        self.assertEqual(unique_digits([15.5, 33.3, 1422.2, 1]), [1])

    def test_unique_digits_with_zero(self):
        self.assertEqual(unique_digits([0, 33, 1422, 1]), [1])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `unique_digits` function, including:

- Lists with only odd digits
- Lists with no odd digits
- Lists with a single odd digit
- An empty list
- Lists with negative numbers
- Lists with non-integer numbers
- Lists with zero

Each test case checks the function's output against the expected result using `self.assertEqual`. This ensures that the function behaves correctly across a range of inputs.