system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_9_code import rolling_max

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list where each element is the maximum of all elements up to that index.
    >>> rolling_max([1, 2, 3, 2, 5])
    [1, 2, 3, 3, 5]
    >>> rolling_max([])
    []
    """
    result: List[int] = []
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result


assistant

import unittest
from typing import List
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])
        self.assertEqual(rolling_max([]), [])
        self.assertEqual(rolling_max([-10, -3, -6, 7, 8]), [-10, -3, -3, 7, 8])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRollingMax` class within the `unittest` module, which contains a single method `test_rolling_max`. This method tests the `rolling_max` function using several test cases:

- The first test case checks if the function correctly computes the rolling maximum for `[1, 2, 3, 2, 5]`, expecting `[1, 2, 3, 3, 5]`.
- The second test case checks if the function returns an empty list when passed an empty list, expecting `[]`.
- The third test case checks if the function correctly computes the rolling maximum for a list containing negative numbers and zeros, expecting `[-10, -3, -3, 7, 8]`.

The `unittest.main()` call at the end runs these tests.