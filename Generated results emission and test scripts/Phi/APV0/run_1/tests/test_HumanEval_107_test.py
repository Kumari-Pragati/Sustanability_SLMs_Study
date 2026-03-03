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

 import unittest
from HumanEval_107_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_even_odd_palindrome_1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_even_odd_palindrome_2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_even_odd_palindrome_3(self):
        self.assertEqual(even_odd_palindrome(10), (4, 6))

    def test_even_odd_palindrome_4(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_even_odd_palindrome_5(self):
        self.assertEqual(even_odd_palindrome(0), (0, 0))

    def test_even_odd_palindrome_6(self):
        self.assertEqual(even_odd_palindrome(100), (18, 18))

    def test_even_odd_palindrome_7(self):
        self.assertEqual(even_odd_palindrome(1000), (180, 180))

    def test_even_odd_palindrome_8(self):
        self.assertEqual(even_odd_palindrome(10000), (1800, 1800))

    def test_even_odd_palindrome_9(self):
        self.assertEqual(even_odd_palindrome(100000), (18000, 18000))

    def test_even_odd_palindrome_10(self):
        self.assertEqual(even_odd_palindrome(1000000), (180000, 180000))

if __name__ == '__main__':
    unittest.main()