You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_163_code import generate_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper + 1) if i % 2 == 0]

 
import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_ascending_order(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_generate_integers_descending_order(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_generate_integers_no_even_digits(self):
        self.assertEqual(generate_integers(10, 14), [])

    def test_generate_integers_edge_cases(self):
        self.assertEqual(generate_integers(2, 2), [2])
        self.assertEqual(generate_integers(8, 8), [8])
        self.assertEqual(generate_integers(2, 10), [2, 4, 6, 8])
        self.assertEqual(generate_integers(1, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 12), [10, 12])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover the function's expected behavior, including ascending and descending order, no even digits, and edge cases where the start and end values are the same or when the start is greater than the end. The `unittest` framework is used to define and run these tests.