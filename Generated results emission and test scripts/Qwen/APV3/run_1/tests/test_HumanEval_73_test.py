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
   - Include from HumanEval_73_code import smallest_change
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
2. Include: from HumanEval_73_code import smallest_change
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
        smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


assistant

import unittest

from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)
    
    def test_case_2(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
    
    def test_case_3(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)
    
    def test_case_4(self):
        self.assertEqual(smallest_change([1, 3, 5, 7, 5, 3, 1]), 2)
    
    def test_case_5(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)
    
    def test_case_6(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]), 1)
    
    def test_case_7(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]), 2)
    
    def test_case_8(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3]), 3)
    
    def test_case_9(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 4]), 4)
    
    def test_case_10(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]), 5)
    
    def test_case_11(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6]), 6)
    
    def test_case_12(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 7]), 7)
    
    def test_case_13(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 8]), 8)
    
    def test_case_14(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9]), 9)
    
    def test_case_15(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]), 10)
    
    def test_case_16(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7,