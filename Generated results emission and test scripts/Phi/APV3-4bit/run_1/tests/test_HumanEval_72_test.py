### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_72_code import will_it_fly
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
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_72_code import will_it_fly
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements
    is less than or equal to the maximum possible weight w.

    Example:
        will_it_fly([1, 2], 5) ➞ False 
        # 1+2 is less than the maximum possible weight, but it's unbalanced.

        will_it_fly([3, 2, 3], 1) ➞ False
        # it's balanced, but 3+2+3 is more than the maximum possible weight.

        will_it_fly([3, 2, 3], 9) ➞ True
        # 3+2+3 is less than the maximum possible weight, and it's balanced.

        will_it_fly([3], 5) ➞ True
        # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True

 import unittest

from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_unbalanced_with_sum_less_than_w(self):
        self.assertFalse(will_it_fly([1, 2], 5))

    def test_unbalanced_with_sum_greater_than_w(self):
        self.assertFalse(will_it_fly([3, 2, 3], 9))

    def test_balanced_with_sum_less_than_w(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))

    def test_balanced_with_sum_equal_to_w(self):
        self.assertTrue(will_it_fly([3], 5))

    def test_balanced_with_sum_greater_than_w(self):
        self.assertFalse(will_it_fly([3, 2, 3], 5))

    def test_empty_list(self):
        self.assertTrue(will_it_fly([]))

    def test_single_element(self):
        self.assertTrue(will_it_fly([3]))

    def test_negative_numbers(self):
        self.assertTrue(will_it_fly([-1, -1], 2))

    def test_max_w_with_balanced_list(self):
        self.assertTrue(will_it_fly([1, 1], 2))

    def test_max_w_with_unbalanced_list(self):
        self.assertFalse(will_it_fly([1, 2], 2))

if __name__ == '__main__':
    unittest.main()