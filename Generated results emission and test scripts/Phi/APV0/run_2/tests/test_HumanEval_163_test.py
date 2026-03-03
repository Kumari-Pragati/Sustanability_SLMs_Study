Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_generate_integers_no_even_numbers(self):
        self.assertEqual(generate_integers(10, 14), [])

    def test_generate_integers_lower_bound_two(self):
        self.assertEqual(generate_integers(1, 8), [2, 4, 6, 8])

    def test_generate_integers_upper_bound_eight(self):
        self.assertEqual(generate_integers(2, 10), [2, 4, 6, 8])

    def test_generate_integers_lower_bound_greater_than_upper_bound(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_generate_integers_lower_bound_two_and_upper_bound_one(self):
        self.assertEqual(generate_integers(2, 1), [])

    def test_generate_integers_lower_bound_one_and_upper_bound_two(self):
        self.assertEqual(generate_integers(1, 2), [2])

if __name__ == '__main__':
    unittest.main()