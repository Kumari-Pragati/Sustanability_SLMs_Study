user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_26_code import remove_duplicates
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]assistant

Here is a unittest test script for the `remove_duplicates` function:

import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_at_end(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 2]), [1, 2, 3, 4])

    def test_duplicates_in_middle(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4]), [1, 2, 3, 4])

    def test_duplicates_at_start(self):
        self.assertEqual(remove_duplicates([2, 2, 3, 4, 5]), [3, 4, 5])

    def test_duplicates_everywhere(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestRemoveDuplicates` class with 8 test methods, each testing a different scenario:

1. An empty list
2. A list with a single element
3. A list with duplicates
4. A list with no duplicates
5. A list with duplicates at the end
6. A list with duplicates in the middle
7. A list with duplicates at the start
8. A list with duplicates everywhere

Each test method uses the `assertEqual` method to check that the output of the `remove_duplicates` function matches the expected output.

You can run this script directly to execute the tests.