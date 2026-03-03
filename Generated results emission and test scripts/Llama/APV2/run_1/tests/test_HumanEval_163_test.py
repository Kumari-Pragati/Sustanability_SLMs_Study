system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return [i for i in range(lower, upper + 1) if i % 2 == 0]assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_2_to_8(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_generate_integers_8_to_2(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_generate_integers_10_to_14(self):
        self.assertEqual(generate_integers(10, 14), [])

    def test_generate_integers_1_to_5(self):
        self.assertEqual(generate_integers(1, 5), [])

    def test_generate_integers_5_to_9(self):
        self.assertEqual(generate_integers(5, 9), [6, 8])

    def test_generate_integers_9_to_5(self):
        self.assertEqual(generate_integers(9, 5), [6, 8])

    def test_generate_integers_1_to_1(self):
        self.assertEqual(generate_integers(1, 1), [])

    def test_generate_integers_2_to_2(self):
        self.assertEqual(generate_integers(2, 2), [2])

    def test_generate_integers_8_to_8(self):
        self.assertEqual(generate_integers(8, 8), [8])

if __name__ == '__main__':
    unittest.main()