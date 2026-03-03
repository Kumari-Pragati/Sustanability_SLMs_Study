system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_21_code import rescale_to_unit

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


assistant

import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # Test case 1
        result1 = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(result1, [0.0, 0.25, 0.5, 0.75, 1.0])

        # Test case 2
        result2 = rescale_to_unit([-1.0, 0.0, 1.0, 2.0, 3.0])
        self.assertEqual(result2, [-0.5, 0.0, 0.5, 1.0, 1.5])

        # Test case 3
        result3 = rescale_to_unit([0.0, 0.0, 0.0, 0.0, 0.0])
        self.assertEqual(result3, [0.0, 0.0, 0.0, 0.0, 0.0])

        # Test case 4
        result4 = rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0])
        self.assertEqual(result4, [0.0, 0.25, 0.5, 0.75, 1.0])

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRescaleToUnit` class within the `unittest` framework, which contains several test cases to verify the correctness of the `rescale_to_unit` function. Each test case uses the `assertEqual` method to check if the output of the function matches the expected results. The `print("All tests passed!")` statement at the end confirms that all tests have been successfully executed.