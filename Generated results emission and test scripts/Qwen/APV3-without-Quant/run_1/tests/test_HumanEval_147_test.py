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

from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_max_triples(5), 1)
    
    def test_edge_case(self):
        self.assertEqual(get_max_triples(1), 0)
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_max_triples(-1)
        
    def test_large_input(self):
        result = get_max_triples(100)
        self.assertGreater(result, 0)
        
    def test_multiple_triplets(self):
        self.assertEqual(get_max_triples(8), 3)
        
    def test_no_triplets(self):
        self.assertEqual(get_max_triples(9), 0)
        
    def test_all_triplets(self):
        self.assertEqual(get_max_triples(10), 10)
        
    def test_zero_sum_triplets(self):
        self.assertEqual(get_max_triples(10), 10)
        
    def test_negative_sum_triplets(self):
        self.assertEqual(get_max_triples(10), 10)
        
    def test_float_input(self):
        with self.assertRaises(TypeError):
            get_max_triples("test")
            
    def test_string_input(self):
        with self.assertRaises(TypeError):
            get_max_triples("test")

if __name__ == '__main__':
    unittest.main()