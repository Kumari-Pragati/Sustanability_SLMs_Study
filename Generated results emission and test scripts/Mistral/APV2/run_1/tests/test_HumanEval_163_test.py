You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is a complete unittest test suite for the `generate_integers` function:


import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_basic(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(15, 20), [10, 12, 14, 16, 18, 20])
        self.assertEqual(generate_integers(21, 26), [])
        self.assertEqual(generate_integers(0, 1), [])
        self.assertEqual(generate_integers(1, 0), [])

    def test_generate_integers_edge_cases(self):
        self.assertEqual(generate_integers(0, 1), [])
        self.assertEqual(generate_integers(1, 0), [])
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(0, 0), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes a basic test for the function's expected behavior, as well as edge cases to ensure the function handles inputs like 0, 1, and out-of-range values correctly.