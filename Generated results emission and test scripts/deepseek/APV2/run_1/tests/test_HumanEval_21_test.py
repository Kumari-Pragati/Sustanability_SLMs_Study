You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([10.0, 20.0, 30.0]), [0.0, 0.5, 1.0])
        self.assertEqual(rescale_to_unit([-1.0, 0.0, 1.0]), [0.0, 0.5, 1.0])
        self.assertEqual(rescale_to_unit([1.0]), [0.0])
        self.assertEqual(rescale_to_unit([1.0, 1.0, 1.0]), [0.0, 0.0, 0.0])
        self.assertEqual(rescale_to_unit([0.0, 0.0, 0.0]), [0.0, 0.0, 0.0])
        self.assertEqual(rescale_to_unit([-1.0, -1.0, -1.0]), [0.0, 0.0, 0.0])
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 2.0, 1.0]), [0.0, 0.3333333333333333, 0.6666666666666666, 0.3333333333333333, 0.0])

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case, `test_rescale_to_unit`, which tests the function with a variety of different input lists. Each test case checks that the function's output matches the expected output.