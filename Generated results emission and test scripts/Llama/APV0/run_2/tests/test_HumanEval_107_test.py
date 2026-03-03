user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_107_code import even_odd_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        if i % 2 == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i):
            even_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)assistant

Here is the unittest test script for the `even_odd_palindrome` function:

import unittest
from HumanEval_107_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_example2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_small_numbers(self):
        self.assertEqual(even_odd_palindrome(5), (1, 4))
        self.assertEqual(even_odd_palindrome(7), (2, 5))
        self.assertEqual(even_odd_palindrome(9), (3, 6))

    def test_large_numbers(self):
        self.assertEqual(even_odd_palindrome(1000), (199, 801))
        self.assertEqual(even_odd_palindrome(1001), (200, 801))

    def test_edge_cases(self):
        self.assertEqual(even_odd_palindrome(1), (1, 0))
        self.assertEqual(even_odd_palindrome(2), (1, 1))
        self.assertEqual(even_odd_palindrome(3), (1, 2))

if __name__ == '__main__':
    unittest.main()

This script includes 6 test cases:

1. `test_example1` and `test_example2` test the function with the provided examples.
2. `test_small_numbers` tests the function with small numbers (5, 7, 9).
3. `test_large_numbers` tests the function with large numbers (1000, 1001).
4. `test_edge_cases` tests the function with edge cases (1, 2, 3).

Each test case uses the `assertEqual` method to check that the output of the `even_odd_palindrome` function matches the expected result.