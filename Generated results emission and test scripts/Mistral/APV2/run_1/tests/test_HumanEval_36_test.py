You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return ans

 Here is a complete unittest test suite for the `fizz_buzz` function:


import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_with_small_numbers(self):
        self.assertEqual(fizz_buzz(0), 0)
        self.assertEqual(fizz_buzz(1), 0)
        self.assertEqual(fizz_buzz(11), 0)
        self.assertEqual(fizz_buzz(12), 0)
        self.assertEqual(fizz_buzz(13), 0)
        self.assertEqual(fizz_buzz(22), 0)
        self.assertEqual(fizz_buzz(23), 0)
        self.assertEqual(fizz_buzz(33), 0)
        self.assertEqual(fizz_buzz(44), 0)
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(55), 0)
        self.assertEqual(fizz_buzz(66), 0)
        self.assertEqual(fizz_buzz(78), 2)
        self.assertEqual(fizz_buzz(79), 3)

    def test_fizz_buzz_with_large_numbers(self):
        self.assertEqual(fizz_buzz(100), 2)
        self.assertEqual(fizz_buzz(1000), 10)
        self.assertEqual(fizz_buzz(10000), 44)
        self.assertEqual(fizz_buzz(100000), 333)
        self.assertEqual(fizz_buzz(1000000), 2778)

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases: one for small numbers and one for large numbers. The test cases cover the edge cases and some common values from the function's documentation. The test suite uses the `unittest.TestCase.assertEqual` method to compare the expected and actual results.