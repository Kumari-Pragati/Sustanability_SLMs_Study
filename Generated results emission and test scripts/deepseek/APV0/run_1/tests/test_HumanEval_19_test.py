You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('five four one two three'), 'one two three four five')
        self.assertEqual(sort_numbers('zero one two three four five six seven eight nine'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers('nine eight seven six five four three two one zero'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers('one one one one one'), 'one one one one one')
        self.assertEqual(sort_numbers(''), '')
        self.assertEqual(sort_numbers('one'), 'one')
        self.assertEqual(sort_numbers('two one'), 'one two')
        self.assertEqual(sort_numbers('two one one'), 'one one two')
        self.assertEqual(sort_numbers('two one one one'), 'one one one two')
        self.assertEqual(sort_numbers('two one one one one'), 'one one one one two')
        self.assertEqual(sort_numbers('two one one one one one'), 'one one one one one two')
        self.assertEqual(sort_numbers('two one one one one one one'), 'one one one one one one two')
        self.assertEqual(sort_numbers('two one one one one one one one'), 'one one one one one one one two')
        self.assertEqual(sort_numbers('two one one one one one one one one'), 'one one one one one one one one two')

if __name__ == '__main__':
    unittest.main()


This script includes a test case for each possible input scenario, including empty strings, single-word strings, and strings with multiple words. It also tests the function with strings that contain duplicate words.

Please note that the function is case-sensitive and does not handle invalid inputs. If you want to add more test cases, you might want to consider these aspects.