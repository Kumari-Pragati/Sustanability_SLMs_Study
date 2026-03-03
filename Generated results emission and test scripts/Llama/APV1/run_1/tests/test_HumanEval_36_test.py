user

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
    return ansassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_50(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_78(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_79(self):
        self.assertEqual(fizz_buzz(79), 3)

    def test_fizz_buzz_0(self):
        self.assertEqual(fizz_buzz(0), 0)

    def test_fizz_buzz_negative(self):
        self.assertEqual(fizz_buzz(-1), 0)

    def test_fizz_buzz_non_integer(self):
        with self.assertRaises(TypeError):
            fizz_buzz('a')

    def test_fizz_buzz_large_number(self):
        self.assertEqual(fizz_buzz(10000), 166)

if __name__ == '__main__':
    unittest.main()


This test suite includes the following test cases:

- `test_fizz_buzz_50`: Tests the function with the input 50, which is a small number.
- `test_fizz_buzz_78`: Tests the function with the input 78, which is a number that should return 2.
- `test_fizz_buzz_79`: Tests the function with the input 79, which is a number that should return 3.
- `test_fizz_buzz_0`: Tests the function with the input 0, which should return 0.
- `test_fizz_buzz_negative`: Tests the function with a negative number, which should return 0.
- `test_fizz_buzz_non_integer`: Tests the function with a non-integer input, which should raise a TypeError.
- `test_fizz_buzz_large_number`: Tests the function with a large number, which should return the correct result.