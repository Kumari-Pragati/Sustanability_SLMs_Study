You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        self.assertEqual(fizz_buzz(0), 0)

    def test_fizz_buzz_less_than_one(self):
        self.assertEqual(fizz_buzz(1), 0)

    def test_fizz_buzz_divisible_by_11(self):
        self.assertEqual(fizz_buzz(11), 1)

    def test_fizz_buzz_divisible_by_13(self):
        self.assertEqual(fizz_buzz(13), 1)

    def test_fizz_buzz_divisible_by_both_11_and_13(self):
        self.assertEqual(fizz_buzz(143), 2)

    def test_fizz_buzz_divisible_by_neither_11_nor_13(self):
        self.assertEqual(fizz_buzz(15), 0)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times(self):
        self.assertEqual(fizz_buzz(158), 3)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_7(self):
        self.assertEqual(fizz_buzz(157), 3)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_no_7(self):
        self.assertEqual(fizz_buzz(159), 0)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_7_in_middle(self):
        self.assertEqual(fizz_buzz(1577), 2)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_7_at_end(self):
        self.assertEqual(fizz_buzz(15777), 1)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_7_at_start(self):
        self.assertEqual(fizz_buzz(7157), 1)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_7_at_start_and_middle(self):
        self.assertEqual(fizz_buzz(71577), 2)

    def test_fizz_buzz_divisible_by_11_and_13_multiple_times_with_7_at_start_and_end(self):
        self.assertEqual(fizz_buzz(715777), 2)

if __name__ == '__main__':
    unittest.main()