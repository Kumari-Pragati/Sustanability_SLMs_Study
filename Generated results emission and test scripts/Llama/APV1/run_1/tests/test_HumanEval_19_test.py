user

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
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
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
    return''.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('zero one five'), 'one zero five')
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('nine eight seven'),'seven eight nine')
        self.assertEqual(sort_numbers('four three two'), 'two three four')
        self.assertEqual(sort_numbers('six five four'), 'four five six')
        self.assertEqual(sort_numbers('nine eight seven six five four three two one'), 'one two three four five six seven eight nine')
        self.assertEqual(sort_numbers(''), '')
        self.assertEqual(sort_numbers('zero'), 'zero')
        self.assertEqual(sort_numbers('one'), 'one')
        self.assertEqual(sort_numbers('nine'), 'nine')

    def test_invalid_input(self):
        with self.assertRaises(KeyError):
            sort_numbers('ten')
        with self.assertRaises(KeyError):
            sort_numbers('ten one')
        with self.assertRaises(KeyError):
            sort_numbers('zero ten')

    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_single_number(self):
        self.assertEqual(sort_numbers('zero'), 'zero')
        self.assertEqual(sort_numbers('one'), 'one')
        self.assertEqual(sort_numbers('nine'), 'nine')

if __name__ == '__main__':
    unittest.main()


This test suite includes the following test cases:

- `test_sort_numbers`: This test case checks the function with various inputs and expected outputs.
- `test_invalid_input`: This test case checks the function with invalid inputs (i.e., numbers that are not in the range 'zero' to 'nine') and verifies that it raises a KeyError.
- `test_empty_string`: This test case checks the function with an empty string as input and verifies that it returns an empty string.
- `test_single_number`: This test case checks the function with a single number as input and verifies that it returns the same string.