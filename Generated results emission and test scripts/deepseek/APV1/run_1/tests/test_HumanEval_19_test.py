You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_19_code import sort_numbers

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def sort_numbers(numbers: str) -> str:
    """Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))


### Response:
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_single_number(self):
        self.assertEqual(sort_numbers('one'), 'one')

    def test_multiple_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

    def test_numbers_with_duplicates(self):
        self.assertEqual(sort_numbers('two two one one'), 'one one two two')

    def test_numbers_with_spaces(self):
        self.assertEqual(sort_numbers('three  one five'), 'one three five')

    def test_numbers_with_extra_spaces(self):
        self.assertEqual(sort_numbers('three  one   five'), 'one three five')

    def test_numbers_with_extra_spaces_and_duplicates(self):
        self.assertEqual(sort_numbers('three  one   five  one'), 'one one three five')

    def test_numbers_with_extra_spaces_and_duplicates_and_out_of_order(self):
        self.assertEqual(sort_numbers('three  one   five  one  two'), 'one one two three five')

    def test_numbers_with_extra_spaces_and_duplicates_and_out_of_order_and_invalid_numbers(self):
        self.assertEqual(sort_numbers('three  one   five  one  two  invalid'), 'one one two three five')

    def test_numbers_with_extra_spaces_and_duplicates_and_out_of_order_and_invalid_numbers_and_extra_invalid_numbers(self):
        self.assertEqual(sort_numbers('three  one   five  one  two  invalid  invalid2'), 'one one two three five')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, such as empty strings, single numbers, multiple numbers, numbers with duplicates, numbers with extra spaces, numbers with extra spaces and duplicates, numbers with extra spaces, duplicates, out of order, invalid numbers, and extra invalid numbers.

Please note that the function `sort_numbers` is expected to be in a file named `HumanEval_19_code.py` in the same directory as the test file.