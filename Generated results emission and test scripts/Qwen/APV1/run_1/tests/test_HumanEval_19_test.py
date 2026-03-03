system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('nine eight seven six five four three two one zero'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers('ten'), 'ten')
        self.assertEqual(sort_numbers('eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'), 'one ten twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen')

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSortNumbers` class that inherits from `unittest.TestCase`. It contains a single method `test_sort_numbers`, which tests the `sort_numbers` function with various inputs to ensure it works as expected. The `assertEqual` methods compare the output of `sort_numbers` against the expected results, ensuring the function behaves correctly under different conditions.