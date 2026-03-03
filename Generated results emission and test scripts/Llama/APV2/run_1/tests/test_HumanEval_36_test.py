system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_50(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_78(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_79(self):
        self.assertEqual(fizz_buzz(79), 3)

    def test_fizz_buzz_100(self):
        self.assertEqual(fizz_buzz(100), 6)

    def test_fizz_buzz_0(self):
        with self.assertRaises(TypeError):
            fizz_buzz(0)

    def test_fizz_buzz_negative(self):
        with self.assertRaises(TypeError):
            fizz_buzz(-1)

if __name__ == '__main__':
    unittest.main()