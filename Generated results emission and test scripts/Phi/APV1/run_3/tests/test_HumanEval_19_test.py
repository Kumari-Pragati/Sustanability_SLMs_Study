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

 import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_sort_numbers_single_number(self):
        self.assertEqual(sort_numbers('nine'), 'nine')

    def test_sort_numbers_multiple_numbers(self):
        self.assertEqual(sort_numbers('five three one'), 'one three five')

    def test_sort_numbers_numbers_in_reverse_order(self):
        self.assertEqual(sort_numbers('nine seven six'), 'six seven nine')

    def test_sort_numbers_numbers_with_spaces(self):
        self.assertEqual(sort_numbers('three four two'), 'two three four')

    def test_sort_numbers_numbers_with_duplicates(self):
        self.assertEqual(sort_numbers('three three three'), 'three three three')

    def test_sort_numbers_numbers_with_zero(self):
        self.assertEqual(sort_numbers('zero two three'), 'zero two three')

    def test_sort_numbers_numbers_with_one(self):
        self.assertEqual(sort_numbers('one zero two'), 'one zero two')

    def test_sort_numbers_numbers_with_invalid_input(self):
        with self.assertRaises(ValueError):
            sort_numbers('ten')

if __name__ == '__main__':
    unittest.main()