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

 Here is a unittest test script for the `generate_integers` function:


import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(1, 2), [2])
        self.assertEqual(generate_integers(2, 1), [])
        self.assertEqual(generate_integers(0, 2), [])
        self.assertEqual(generate_integers(2, 0), [])
        self.assertEqual(generate_integers(15, 20), [10, 12, 14, 16, 18, 20])
        self.assertEqual(generate_integers(20, 15), [10, 12, 14, 16, 18, 20])
        self.assertEqual(generate_integers(21, 20), [])
        self.assertEqual(generate_integers(20, 21), [])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover various edge cases and different input combinations. It uses the `assertEqual` method to compare the expected output with the actual output of the `generate_integers` function.