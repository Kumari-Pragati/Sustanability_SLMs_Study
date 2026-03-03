Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

 import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_negative_number(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_positive_number(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_single_digit_number(self):
        self.assertEqual(even_odd_count(5), (0, 1))

    def test_multiple_digit_number(self):
        self.assertEqual(even_odd_count(123456789), (4, 5))

    def test_all_even_digits(self):
        self.assertEqual(even_odd_count(24680), (5, 0))

    def test_all_odd_digits(self):
        self.assertEqual(even_odd_count(13579), (0, 5))

    def test_mixed_digits(self):
        self.assertEqual(even_odd_count(1234567890), (4, 5))

    def test_no_digits(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            even_odd_count("123")

if __name__ == '__main__':
    unittest.main()