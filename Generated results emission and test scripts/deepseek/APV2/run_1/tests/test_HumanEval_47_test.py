You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):
    def test_odd_length_list(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1]), 1)
        self.assertEqual(median([1, 2]), 1.5)

    def test_even_length_list(self):
        self.assertEqual(median([3, 1, 2, 4]), 2.5)
        self.assertEqual(median([-10, 4, 6, 10]), 5)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            median([])

    def test_single_element_list(self):
        self.assertEqual(median([10]), 10)

    def test_duplicate_elements(self):
        self.assertEqual(median([1, 1, 2, 2]), 1.5)
        self.assertEqual(median([1, 1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for lists of odd and even lengths, as well as tests for an empty list and a list with a single element. It also includes a test for lists with duplicate elements. The test for an empty list checks that the function raises an IndexError, as it should, because it's trying to access an element at index 0 of an empty list.