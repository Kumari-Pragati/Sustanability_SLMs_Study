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

    return (even_palindrome_count, odd_palindrome_count)

 Here is a unittest test script for the `even_odd_palindrome` function:


import unittest
from HumanEval_107_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_even_odd_palindrome(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
        self.assertEqual(even_odd_palindrome(5), (1, 3))
        self.assertEqual(even_odd_palindrome(7), (1, 4))
        self.assertEqual(even_odd_palindrome(10), (3, 5))
        self.assertEqual(even_odd_palindrome(12), (4, 6))
        self.assertEqual(even_odd_palindrome(15), (4, 7))
        self.assertEqual(even_odd_palindrome(20), (6, 10))
        self.assertEqual(even_odd_palindrome(25), (7, 12))
        self.assertEqual(even_odd_palindrome(30), (8, 14))
        self.assertEqual(even_odd_palindrome(100), (26, 50))
        self.assertEqual(even_odd_palindrome(1000), (154, 342))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the function with various input values, and it checks if the function returns the expected output for each test case. The test script can be run directly to test the function.