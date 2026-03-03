You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_58_code import common
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_58_code import common

class TestCommon(unittest.TestCase):
    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertEqual(common([], []), [])
        self.assertEqual(common([1, 2, 3], []), [])
        self.assertEqual(common([], [4, 5, 6]), [])
        self.assertEqual(common([1, 1, 2, 2], [1, 2, 2, 2]), [1, 2])
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios:

- Two lists with common elements.
- Two lists with no common elements.
- Two empty lists.
- One list is empty.
- Lists with duplicate elements.
- Lists with no common elements after removing duplicates.

The `assertEqual` method is used to check if the output of the `common` function matches the expected result for each test case.