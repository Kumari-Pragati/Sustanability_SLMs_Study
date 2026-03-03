### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_68_code import pluck
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
### Instruction:
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_68_code import pluck
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4, 2, 3]
        Output: [2, 1]

    Example 2:
        Input: [1, 2, 3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if len(arr) == 0:
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if evens == []:
        return []
    return [min(evens), arr.index(min(evens))]


### Response:
import unittest
from HumanEval_68_code import pluck

class TestPluck(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
        self.assertEqual(pluck([1, 2, 3]), [2, 1])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_empty_list(self):
        self.assertEqual(pluck([]), [])

    def test_no_even_numbers(self):
        self.assertEqual(pluck([1, 3, 5]), [])

if __name__ == '__main__':
    unittest.main()