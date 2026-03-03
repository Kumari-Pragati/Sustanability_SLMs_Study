You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


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
        self.assertEqual(filter_integers([None, False, 0, 1]), [1])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios. It tests the function with a list containing both integers and non-integers, with a list of integers only, with an empty list, with a list containing strings, and with a list containing other types of values. It also tests the function with a list containing None, False, and 0, which are not considered integers but are included in the function's output.