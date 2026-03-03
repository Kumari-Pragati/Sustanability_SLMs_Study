system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    
    def test_rescale_to_unit(self):
        # Test case 1
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0], "Test Case 1 Failed")
        
        # Test case 2
        self.assertEqual(rescale_to_unit([-1.0, 0.0, 1.0]), [-0.5, 0.0, 0.5], "Test Case 2 Failed")
        
        # Test case 3
        self.assertEqual(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]), [0.0, 0.25, 0.5, 0.75, 1.0], "Test Case 3 Failed")
        
        # Test case 4
        self.assertEqual(rescale_to_unit([0.0, 0.0, 0.0]), [0.0, 0.0, 0.0], "Test Case 4 Failed")

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases to ensure the `rescale_to_unit` function works as expected across different scenarios.