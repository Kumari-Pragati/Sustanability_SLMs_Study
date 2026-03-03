You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_83_code import starts_one_ends
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_starts_one_ends_positive(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 18)
        self.assertEqual(starts_one_ends(3), 180)
        self.assertEqual(starts_one_ends(4), 1800)
        self.assertEqual(starts_one_ends(5), 18000)
        self.assertEqual(starts_one_ends(6), 180000)
        self.assertEqual(starts_one_ends(7), 1800000)
        self.assertEqual(starts_one_ends(8), 18000000)
        self.assertEqual(starts_one_ends(9), 180000000)
        self.assertEqual(starts_one_ends(10), 1800000000)

    def test_starts_one_ends_negative(self):
        self.assertEqual(starts_one_ends(-1), 1)
        self.assertEqual(starts_one_ends(-2), 18)
        self.assertEqual(starts_one_ends(-3), 180)
        self.assertEqual(starts_one_ends(-4), 1800)
        self.assertEqual(starts_one_ends(-5), 18000)
        self.assertEqual(starts_one_ends(-6), 180000)
        self.assertEqual(starts_one_ends(-7), 1800000)
        self.assertEqual(starts_one_ends(-8), 18000000)
        self.assertEqual(starts_one_ends(-9), 180000000)
        self.assertEqual(starts_one_ends(-10), 1800000000)

    def test_starts_one_ends_zero(self):
        with self.assertRaises(ValueError):
            starts_one_ends(0)

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

- `test_starts_one_ends_positive`: Tests the function with positive integers.
- `test_starts_one_ends_negative`: Tests the function with negative integers.
- `test_starts_one_ends_zero`: Tests the function with zero, which should raise a ValueError.

Please note that the function `starts_one_ends` is expected to be in a file named `HumanEval_83_code.py` in the same directory as the test script.