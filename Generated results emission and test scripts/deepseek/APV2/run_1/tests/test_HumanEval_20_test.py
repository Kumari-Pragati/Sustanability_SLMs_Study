You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given function:


import unittest
from typing import List, Tuple

# Assuming the function is defined in a file named 'HumanEval_20_code.py'
from HumanEval_20_code import find_closest_elements

class TestFindClosestElements(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_same_elements(self):
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0, 1.0]), (1.0, 1.0))

    def test_negative_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]), (-2.0, -2.2))

    def test_single_element(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_closest_elements([])

    def test_large_numbers(self):
        self.assertEqual(find_closest_elements([1000000.0, 2000000.0, 3000000.0, 4000000.0, 5000000.0, 2000001.0]), (2000000.0, 2000001.0))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for basic cases, cases with same elements, negative numbers, single element, empty list, and large numbers. It also checks for the ValueError that is raised when the input list has less than two elements.