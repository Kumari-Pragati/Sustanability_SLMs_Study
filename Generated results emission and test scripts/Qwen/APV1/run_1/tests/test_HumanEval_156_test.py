system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_156_code import int_to_mini_roman

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    res = ''
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            res += sym[i]
            div -= 1
        i -= 1
    return res.lower()


assistant

import unittest

# Function to be tested
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_int_to_mini_roman(self):
        # Test cases provided in the docstring
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_edge_cases(self):
        # Edge case tests
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(1000), 'm')
        self.assertEqual(int_to_mini_roman(0), '')

    def test_out_of_range(self):
        # Test out of range values
        with self.assertRaises(ValueError):
            int_to_mini_roman(-1)
        with self.assertRaises(ValueError):
            int_to_mini_roman(1001)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIntToMiniRoman` class that inherits from `unittest.TestCase`. It contains three methods:

- `test_int_to_mini_roman`: This method checks if the `int_to_mini_roman` function returns the correct results for the provided test cases.
- `test_edge_cases`: This method includes edge case tests to ensure the function handles special cases correctly.
- `test_out_of_range`: This method tests the function's behavior when given invalid inputs (negative numbers and numbers greater than 1000).

The `unittest.main()` call at the end runs all the defined test methods.