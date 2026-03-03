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
   - Include from HumanEval_106_code import f
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
2. Include: from HumanEval_106_code import f
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    ret = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            x = 1
            for j in range(1, i + 1):
                x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1, i + 1):
                x += j
            ret += [x]
    return ret


assistant

import unittest

# Importing the function we want to test
from HumanEval_106_code import f

class TestF(unittest.TestCase):
    
    # Test case for positive integer input
    def test_positive_integer(self):
        result = f(5)
        expected_result = [1, 2, 6, 24, 15]
        self.assertEqual(result, expected_result)
        
    # Test case for negative integer input
    def test_negative_integer(self):
        result = f(-3)
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case for zero input
    def test_zero_input(self):
        result = f(0)
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case for large positive integer input
    def test_large_positive_integer(self):
        result = f(100)
        expected_result = [1, 2, 6, 24, 15, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000, 51090942171709440000, 1124000727777607680000, 25852016738884976640000, 620448401733239439360000, 15511210043330985984000000, 403291461126605635584000000, 108888694504183521607680000000, 30488834461171386050150400000000, 88417619937397019545432674368000000000, 2631308369336935301672180121600000000000, 806581820342394481594290222080000000000000, 2652528598121910586363084800000000000000000, 871782912000000000000000000000000000000000000, 29523279903960414084761860964352000000000000000000000, 9227465585551162146859225960693800000000000000000000000, 326876943551814847068602244313800000000000000000000000000, 108888694504183521