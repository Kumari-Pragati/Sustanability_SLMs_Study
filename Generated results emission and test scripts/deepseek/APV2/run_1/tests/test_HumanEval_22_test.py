You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 'two', 3.0, 'four', 5]), [1, 3, 5])
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(filter_integers([]), [])
        self.assertEqual(filter_integers(['one', 'two', 'three']), [])
        self.assertEqual(filter_integers([1.0, 2.0, 3.0]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios. It tests the function with a list containing both integers and non-integers, with a list of integers only, with an empty list, and with a list of strings and floats.

Please note that the function `filter_integers` is expected to be in a file named `HumanEval_22_code.py` in the same directory as the test file. If the function is in a different location, you will need to adjust the import statement accordingly.