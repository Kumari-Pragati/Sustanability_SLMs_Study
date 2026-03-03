Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_36_code import fizz_buzz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

 import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_zero(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_divisible_by_11(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_divisible_by_13(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_divisible_by_both(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_divisible_by_neither(self):
        self.assertEqual(fizz_buzz(1), 0)

    def test_fizz_buzz_divisible_by_11_and_13(self):
        self.assertEqual(fizz_buzz(143), 2)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times(self):
        self.assertEqual(fizz_buzz(154), 3)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_leading_zeros(self):
        self.assertEqual(fizz_buzz(1540), 3)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_leading_zeros_and_other_digits(self):
        self.assertEqual(fizz_buzz(1547), 3)

if __name__ == '__main__':
    unittest.main()