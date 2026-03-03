You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_15_code import string_sequence

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(x) for x in range(n + 1))


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_positive_numbers(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_negative_numbers(self):
        self.assertEqual(string_sequence(-5), '0 -1 -2 -3 -4 -5')

    def test_large_numbers(self):
        self.assertEqual(string_sequence(1000), ' '.join(str(x) for x in range(1001)))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            string_sequence('a')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            string_sequence(None)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- `test_zero`: Tests the function with the input 0.
- `test_positive_numbers`: Tests the function with a positive input.
- `test_negative_numbers`: Tests the function with a negative input.
- `test_large_numbers`: Tests the function with a large input.
- `test_type_error`: Tests the function with a non-integer input.
- `test_value_error`: Tests the function with a None input.

The `assertEqual` method is used to check if the output of the function matches the expected output. The `assertRaises` method is used to check if the function raises the expected exception when given an invalid input.