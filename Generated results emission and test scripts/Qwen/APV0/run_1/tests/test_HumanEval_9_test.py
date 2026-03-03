system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Function to be tested
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])
        self.assertEqual(rolling_max([]), [])
        self.assertEqual(rolling_max([-10, -3, -6, 7, 4]), [-10, -3, -3, 7, 7])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and `rolling_max`, then defines a class `TestRollingMax` inheriting from `unittest.TestCase`. It contains three test cases using the `assertEqual` method to verify the correctness of the `rolling_max` function against provided data points. Finally, it calls `unittest.main()` to run these tests when the script is executed directly.