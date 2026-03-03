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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('nine eight seven'), 'eight seven nine')
        self.assertEqual(sort_numbers('zero one'), 'one zero')
        self.assertEqual(sort_numbers('five four three'), 'three four five')
        self.assertEqual(sort_numbers('six five four'), 'four five six')
        self.assertEqual(sort_numbers('nine eight seven six five four three two one zero'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers(''), '')
        self.assertEqual(sort_numbers('one'), 'one')
        self.assertEqual(sort_numbers('one two'), 'one two')
        self.assertEqual(sort_numbers('one two three'), 'one two three')
        self.assertEqual(sort_numbers('one two three four'), 'one two three four')
        self.assertEqual(sort_numbers('one two three four five'), 'one two three four five')
        self.assertEqual(sort_numbers('one two three four five six'), 'one two three four five six')
        self.assertEqual(sort_numbers('one two three four five six seven'), 'one two three four five six seven')
        self.assertEqual(sort_numbers('one two three four five six seven eight'), 'one two three four five six seven eight')
        self.assertEqual(sort_numbers('one two three four five six seven eight nine'), 'one two three four five six seven eight nine')

if __name__ == '__main__':
    unittest.main()


This script includes 15 test cases to cover various scenarios, including empty string, single number, multiple numbers, and edge cases. Each test case uses the `assertEqual` method to compare the output of the `sort_numbers` function with the expected result.