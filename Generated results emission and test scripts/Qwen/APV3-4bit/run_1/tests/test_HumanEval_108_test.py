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
   - Include from HumanEval_108_code import count_nums
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
2. Include: from HumanEval_108_code import count_nums
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


assistant

import unittest

from HumanEval_108_code import count_nums

class TestCountNums(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_nums([]), 0)
    
    def test_single_element_array(self):
        self.assertEqual(count_nums([1]), 1)
        self.assertEqual(count_nums([-1]), 1)
    
    def test_multiple_elements(self):
        self.assertEqual(count_nums([1, 2, 3]), 3)
        self.assertEqual(count_nums([1, -2, 3]), 2)
        self.assertEqual(count_nums([-1, 2, -3]), 2)
    
    def test_large_numbers(self):
        self.assertEqual(count_nums([9, 87654321, -987654321]), 3)
        self.assertEqual(count_nums([-987654321, 9, 87654321]), 3)
    
    def test_all_negative(self):
        self.assertEqual(count_nums([-1, -2, -3]), 3)
    
    def test_all_positive(self):
        self.assertEqual(count_nums([1, 2, 3]), 3)
    
    def test_mixed_signs(self):
        self.assertEqual(count_nums([1, -2, 3]), 2)
        self.assertEqual(count_nums([-1, 2, -3]), 2)
    
    def test_zero_sum(self):
        self.assertEqual(count_nums([0, 0, 0]), 0)
    
    def test_one_sum(self):
        self.assertEqual(count_nums([1, 1, 1]), 1)
    
    def test_two_sum(self):
        self.assertEqual(count_nums([2, 2, 2]), 3)
    
    def test_three_sum(self):
        self.assertEqual(count_nums([3, 3, 3]), 3)
    
    def test_four_sum(self):
        self.assertEqual(count_nums([4, 4, 4, 4]), 4)
    
    def test_five_sum(self):
        self.assertEqual(count_nums([5, 5, 5, 5, 5]), 5)
    
    def test_six_sum(self):
        self.assertEqual(count_nums([6, 6, 6, 6, 6, 6, 6]), 6)
    
    def test_seven_sum(self):
        self.assertEqual(count_nums([7, 7, 7, 7, 7, 7, 7, 7]), 7)
    
    def test_eight_sum(self):
        self.assertEqual(count_nums([8, 8, 8, 8, 8, 8, 8, 8, 8]), 8)
    
    def test_nine_sum(self):
        self.assertEqual(count_nums([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]), 9)
    
    def test_ten_sum(self):
        self.assertEqual(count_nums([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10)
    
    def test_hundred_sum(self):
        self.assertEqual(count_nums([100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), 10)
    
    def test_thousand_sum(self):
        self.assertEqual(count_nums([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]), 10)
    
    def test_million_sum(self):
        self.assertEqual(count_nums([1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]), 10)
    
    def test_trillion_sum(self):
        self.assertEqual(count_nums([1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000