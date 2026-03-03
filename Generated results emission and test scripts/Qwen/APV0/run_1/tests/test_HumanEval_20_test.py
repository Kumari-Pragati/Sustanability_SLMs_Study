system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_20_code import find_closest_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From a supplied list of numbers (of length at least two), select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair


assistant

import unittest

# Assuming the 'find_closest_elements' function is defined in a file named 'HumanEval_20_code.py'
from HumanEval_20_code import find_closest_elements

class TestFindClosestElements(unittest.TestCase):

    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
        self.assertEqual(find_closest_elements([-1.0, 0.0, 1.0, 2.0, 3.0]), (-1.0, 0.0))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestFindClosestElements` that inherits from `unittest.TestCase`. It contains methods to test the `find_closest_elements` function with various inputs. The `assertEqual` method checks if the output of the function matches the expected result. Finally, the `if __name__ == '__main__':` block runs all tests when the script is executed directly.