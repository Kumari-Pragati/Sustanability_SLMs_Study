You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_43_code import pairs_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_43_code import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(pairs_sum_to_zero([]))

    def test_single_element(self):
        self.assertFalse(pairs_sum_to_zero([1]))

    def test_no_pairs(self):
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_positive_numbers(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))

    def test_zero_in_list(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, -2, 1]))

    def test_large_list(self):
        self.assertTrue(pairs_sum_to_zero([i for i in range(1, 1000000) if i % 2 == 0] + [-i for i in range(1, 1000000) if i % 2 == 0]))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- An empty list
- A list with a single element
- A list with no pairs that sum to zero
- A list with negative numbers
- A list with positive numbers
- A list with zero
- A large list with pairs that sum to zero

Each test checks the output of the `pairs_sum_to_zero` function with a specific input.