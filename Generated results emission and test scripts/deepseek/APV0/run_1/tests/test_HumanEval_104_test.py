You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_all_odd_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_all_even_digits(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_mixed_digits(self):
        self.assertEqual(unique_digits([152, 33, 1422, 10, 11]), [33, 11])

    def test_single_digit(self):
        self.assertEqual(unique_digits([1]), [1])

    def test_no_digits(self):
        self.assertEqual(unique_digits([]), [])

    def test_large_numbers(self):
        self.assertEqual(unique_digits([12345678901234567890]), [])

    def test_negative_numbers(self):
        self.assertEqual(unique_digits([-15, -33, -1422, -1]), [1, 15, 33])

    def test_zero(self):
        self.assertEqual(unique_digits([0]), [])

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestUniqueDigits` that inherits from `unittest.TestCase`. Each method in this class is a test case that tests a specific scenario. The `assertEqual` method is used to check if the output of the `unique_digits` function matches the expected output.

To run the tests, you can simply execute this script. If all tests pass, the script will exit without any output. If a test fails, the unittest framework will output a detailed error message indicating which test failed and why.