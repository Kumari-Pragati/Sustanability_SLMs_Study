Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_110_code import exchange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    odd = 0
    even = 0
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"

 import unittest
from HumanEval_110_code import exchange

class TestExchangeFunction(unittest.TestCase):

    def test_exchange_all_even(self):
        self.assertEqual(exchange([2, 4, 6, 8], [1, 3, 5, 7]), "YES")

    def test_exchange_some_even(self):
        self.assertEqual(exchange([2, 4, 6, 8], [2, 4, 6, 8]), "YES")

    def test_exchange_all_odd(self):
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 6, 8]), "NO")

    def test_exchange_mixed_odd_even(self):
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 6, 8, 10]), "NO")

    def test_exchange_empty_list(self):
        self.assertEqual(exchange([], []), "YES")

    def test_exchange_non_empty_list_with_zero(self):
        self.assertEqual(exchange([0], [1, 2, 3]), "YES")

    def test_exchange_non_empty_list_with_negative(self):
        self.assertEqual(exchange([-1, -3, -5], [2, 4, 6]), "NO")

if __name__ == '__main__':
    unittest.main()