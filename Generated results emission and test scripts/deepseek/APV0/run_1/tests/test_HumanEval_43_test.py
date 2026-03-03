You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given function:


import unittest
from HumanEval_43_code import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))
        self.assertFalse(pairs_sum_to_zero([1, 3, -2, 1]))
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 7]))

    def test_negative_numbers(self):
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_single_element(self):
        self.assertFalse(pairs_sum_to_zero([1]))

    def test_empty_list(self):
        self.assertFalse(pairs_sum_to_zero([]))

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestPairsSumToZero` that inherits from `unittest.TestCase`. It includes four test methods:

- `test_positive_numbers` tests the function with a list of positive numbers.
- `test_negative_numbers` tests the function with a list of negative numbers.
- `test_single_element` tests the function with a list containing a single element.
- `test_empty_list` tests the function with an empty list.

Each test method uses the `assertEqual` or `assertFalse` method to check if the function's output matches the expected result.

To run the tests, you can simply execute the script. The `unittest.main()` call at the end runs all the test methods in the `TestPairsSumToZero` class.