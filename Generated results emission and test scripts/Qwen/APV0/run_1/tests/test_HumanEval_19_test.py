system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function from the given code snippet
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers("three one five"), "one three five")
        self.assertEqual(sort_numbers("nine eight seven six five four three two one zero"), "one zero two three four five six seven eight nine")
        self.assertEqual(sort_numbers(""), "")
        self.assertEqual(sort_numbers("ten"), "ten")

if __name__ == '__main__':
    unittest.main()


This script imports the `sort_numbers` function from the provided code snippet and creates a test class `TestSortNumbers` that contains a test method `test_sort_numbers`. The test method checks various cases to ensure the function behaves as expected.