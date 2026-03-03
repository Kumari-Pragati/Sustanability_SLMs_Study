You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_26_code import remove_duplicates

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4, 4, 5]), [1, 5])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4, 4, 5, 5]), [1])
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `remove_duplicates` function is working as expected. It tests the function with lists that have no duplicates, one duplicate, multiple duplicates, and an empty list. It also tests the function with lists that have multiple pairs of duplicates.