You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])
        self.assertEqual(unique([1, 1, 1, 1]), [1])
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(unique([]), [])
        self.assertEqual(unique([1]), [1])
        self.assertEqual(unique([1, 1, 2, 2, 3, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios:

- A list with duplicate elements.
- A list with all identical elements.
- A list with no duplicate elements.
- An empty list.
- A list with a single element.
- A list with multiple duplicate elements.

Each test case checks if the `unique` function returns the expected result. If any of these test cases fail, the test suite will report the failure, indicating that the function does not behave as expected.