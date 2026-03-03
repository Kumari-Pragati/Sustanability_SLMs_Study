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
        # Edge case: All elements are the same
        self.assertEqual(smallest_change([1, 1, 1, 1]), 0)
    
    def test_case_5(self):
        # Edge case: Array length is odd
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7]), 3)
    
    def test_case_6(self):
        # Edge case: Array contains duplicates
        self.assertEqual(smallest_change([1, 2, 3, 3, 2, 1]), 1)
    
    def test_case_7(self):
        # Edge case: Empty array
        self.assertEqual(smallest_change([]), 0)
    
    def test_case_8(self):
        # Edge case: Single-element array
        self.assertEqual(smallest_change([1]), 0)
    
    def test_case_9(self):
        # Edge case: Palindromic array
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)
    
    def test_case_10(self):
        # Edge case: Reverse of itself
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
    
    def test_case_11(self):
        # Edge case: Contains negative numbers
        self.assertEqual(smallest_change([1, 2, 3, 5, -4, 7, 9, 6]), 4)
    
    def test_case_12(self):
        # Edge case: Contains zero
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 0]), 4)
    
    def test_case_13(self):
        # Edge case: Contains float
        self.assertEqual(smallest_change([1.1, 2.2, 3.3, 5.5, 4.4, 7.7, 9.9, 6.6]), 4)
    
    def test_case_14(self):
        # Edge case: Contains string
        self.assertEqual(smallest_change(['a', 'b', 'c', 'd']), 0)
    
    def test_case_15(self):
        # Edge case: Contains dictionary
        self.assertEqual(smallest_change({'key': 'value'}), 0)
    
    def test_case_16(self):
        # Edge case: Contains set
        self.assertEqual(smallest_change({1, 2, 3}), 0)
    
    def test_case_17(self):
        # Edge case: Contains tuple
        self.assertEqual(smallest_change((1, 2, 3)), 0)
    
    def test_case_18(self):
        # Edge case: Contains complex number
        self.assertEqual(smallest_change([1 + 2j, 2 + 3j, 3 + 4j]), 0)


This completes the test suite by including tests for various cases, ensuring the function behaves as expected under different conditions.