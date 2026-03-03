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
   - Include from HumanEval_147_code import get_max_triples
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
2. Include: from HumanEval_147_code import get_max_triples
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)


assistant

import unittest

# Importing the function we want to test
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):
    
    # Test case for a small input
    def test_small_input(self):
        result = get_max_triples(5)
        expected_output = 1
        self.assertEqual(result, expected_output, "For n=5, there should be exactly one valid triple.")
        
    # Test case for a larger input
    def test_large_input(self):
        result = get_max_triples(10)
        expected_output = 3
        self.assertEqual(result, expected_output, "For n=10, there should be exactly three valid triples.")
        
    # Test case for an empty input
    def test_empty_input(self):
        result = get_max_triples(0)
        expected_output = 0
        self.assertEqual(result, expected_output, "For n=0, there should be no valid triples.")

    # Test case for a negative input
    def test_negative_input(self):
        result = get_max_triples(-5)
        expected_output = None
        self.assertIsNone(result, "For n=-5, there should be no valid triples as n must be positive.")
        
    # Test case for a non-integer input
    def test_non_integer_input(self):
        try:
            result = get_max_triples("abc")
            self.fail("Expected ValueError when trying to process a string as an integer.")
        except ValueError:
            pass
        
    # Test case for a very large input
    def test_large_input_with_large_values(self):
        result = get_max_triples(10**9)
        expected_output = 10**9
        self.assertEqual(result, expected_output, "For n=10^9, there should be exactly 10^9 valid triples.")
        
if __name__ == '__main__':
    unittest.main()


This solution includes a comprehensive set of tests covering different scenarios such as small, large, empty, negative, non-integer, and extremely large inputs. It also checks for potential errors like division by zero and handling of non-integer inputs.