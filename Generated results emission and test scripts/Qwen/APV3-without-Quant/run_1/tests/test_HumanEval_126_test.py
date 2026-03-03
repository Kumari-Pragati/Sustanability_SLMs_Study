system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_126_code import is_sorted
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_126_code import is_sorted
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False


assistant

import unittest

from HumanEval_126_code import is_sorted

class TestIsSorted(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_edge_cases(self):
        self.assertTrue(is_sorted([1]))
        self.assertTrue(is_sorted([1, 1]))
        self.assertTrue(is_sorted([1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([1, 1, 1, 1,