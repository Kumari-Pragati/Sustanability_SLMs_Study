system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_5_code import intersperse

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result


assistant

import unittest
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_large_input(self):
        large_numbers = list(range(100))
        self.assertEqual(intersperse(large_numbers, 4), [x for x in range(100)] + [4] * (len(large_numbers) - 1))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a unit test suite using the `unittest` framework to verify that the `intersperse` function works as expected across different scenarios. The test cases cover empty lists, single-element lists, multiple-element lists, and larger inputs.