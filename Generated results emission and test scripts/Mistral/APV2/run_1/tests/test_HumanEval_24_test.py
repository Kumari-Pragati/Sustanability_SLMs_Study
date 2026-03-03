You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_24_code import largest_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return i

 Here is the complete unittest test suite for the `largest_divisor` function:


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(1), 1)
        self.assertEqual(largest_divisor(2), 2)
        self.assertEqual(largest_divisor(3), 3)
        self.assertEqual(largest_divisor(4), 2)
        self.assertEqual(largest_divisor(5), 5)
        self.assertEqual(largest_divisor(6), 6)
        self.assertEqual(largest_divisor(7), 7)
        self.assertEqual(largest_divisor(8), 4)
        self.assertEqual(largest_divisor(9), 3)
        self.assertEqual(largest_divisor(10), 2)
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(16), 8)
        self.assertEqual(largest_divisor(17), 1)
        self.assertEqual(largest_divisor(18), 2)
        self.assertEqual(largest_divisor(19), 1)
        self.assertEqual(largest_divisor(20), 4)
        self.assertEqual(largest_divisor(21), 7)
        self.assertEqual(largest_divisor(22), 2)
        self.assertEqual(largest_divisor(23), 1)
        self.assertEqual(largest_divisor(24), 4)
        self.assertEqual(largest_divisor(25), 5)
        self.assertEqual(largest_divisor(26), 2)
        self.assertEqual(largest_divisor(27), 3)
        self.assertEqual(largest_divisor(28), 4)
        self.assertEqual(largest_divisor(29), 1)
        self.assertEqual(largest_divisor(30), 2)
        self.assertEqual(largest_divisor(31), 1)
        self.assertEqual(largest_divisor(32), 8)
        self.assertEqual(largest_divisor(33), 1)
        self.assertEqual(largest_divisor(34), 2)
        self.assertEqual(largest_divisor(35), 5)
        self.assertEqual(largest_divisor(36), 4)
        self.assertEqual(largest_divisor(37), 1)
        self.assertEqual(largest_divisor(38), 2)
        self.assertEqual(largest_divisor(39), 1)
        self.assertEqual(largest_divisor(40), 4)
        self.assertEqual(largest_divisor(41), 1)
        self.assertEqual(largest_divisor(42), 2)
        self.assertEqual(largest_divisor(43), 1)
        self.assertEqual(largest_divisor(44), 2)
        self.assertEqual(largest_divisor(45), 3)
        self.assertEqual(largest_divisor(46), 2)
        self.assertEqual(largest_divisor(47), 1)
        self.assertEqual(largest_divisor(48), 2)
        self.assertEqual(largest_divisor(49), 1)
        self.assertEqual(largest_divisor(50), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes a test function `test_largest_divisor` that checks the function's behavior for a variety of input values. The test suite uses the `unittest.TestCase.assertEqual` method to compare the expected output with the actual output of the `largest_