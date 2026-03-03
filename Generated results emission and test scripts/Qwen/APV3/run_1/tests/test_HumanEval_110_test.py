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
   - Include from HumanEval_110_code import exchange
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
2. Include: from HumanEval_110_code import exchange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    odd = 0
    even = 0
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"


assistant

import unittest

# Importing the exchange function from the given module
from HumanEval_110_code import exchange

class TestExchange(unittest.TestCase):
    
    # Test case for positive numbers
    def test_positive_numbers(self):
        result = exchange([1, 2, 3, 4], [1, 2, 3, 4])
        self.assertEqual(result, "YES")
        
    # Test case for negative numbers
    def test_negative_numbers(self):
        result = exchange([1, 2, 3, 4], [1, 5, 3, 4])
        self.assertEqual(result, "NO")
        
    # Test case for empty list
    def test_empty_list(self):
        result = exchange([], [])
        self.assertEqual(result, "YES")
        
    # Test case for mixed numbers (odd in one list)
    def test_mixed_numbers(self):
        result = exchange([1, 2, 3, 4], [1, 5, 3, 4])
        self.assertEqual(result, "YES")
        
    # Test case for mixed numbers (even in both lists)
    def test_even_both_lists(self):
        result = exchange([1, 2, 3, 4], [2, 4, 6, 8])
        self.assertEqual(result, "YES")
        
    # Test case for mixed numbers (odd in both lists)
    def test_odd_both_lists(self):
        result = exchange([1, 2, 3, 4], [1, 3, 5, 7])
        self.assertEqual(result, "NO")

if __name__ == '__main__':
    unittest.main()