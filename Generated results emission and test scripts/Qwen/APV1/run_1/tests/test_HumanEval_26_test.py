system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([5, 9, 7, 8, 9, 8]), [5, 7, 8])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([10]), [10])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRemoveDuplicates` class within a `unittest` module. The `test_remove_duplicates` method contains several assertions to check the correctness of the `remove_duplicates` function using different inputs and expected outputs.