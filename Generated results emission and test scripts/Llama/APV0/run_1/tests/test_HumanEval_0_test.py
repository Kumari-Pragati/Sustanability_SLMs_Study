user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_0_code import has_close_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx!= idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return Falseassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_0_code import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_no_elements(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_threshold_zero(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0], 0.0))

    def test_threshold_negative(self):
        self.assertRaises(ValueError, has_close_elements, [1.0, 2.0, 3.0], -0.5)

if __name__ == '__main__':
    unittest.main()


This script includes six test cases:

- `test_no_close_elements`: Tests the function with a list of numbers where no two numbers are closer than the given threshold.
- `test_close_elements`: Tests the function with a list of numbers where two numbers are closer than the given threshold.
- `test_no_elements`: Tests the function with an empty list of numbers.
- `test_single_element`: Tests the function with a list containing only one element.
- `test_threshold_zero`: Tests the function with a threshold of zero.
- `test_threshold_negative`: Tests the function with a negative threshold, which should raise a ValueError.