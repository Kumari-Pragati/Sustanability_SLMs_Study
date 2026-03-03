You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a comprehensive unittest test suite for the provided `exchange` function:


import unittest
from HumanEval_110_code import exchange

class TestExchangeFunction(unittest.TestCase):

    def test_exchange_even_lists(self):
        self.assertEqual(exchange([2, 4, 6], [2, 4, 6]), "YES")
        self.assertEqual(exchange([0, 2, 4], [0, 2, 4]), "YES")
        self.assertEqual(exchange([2, 4, 6], [2, 2, 6]), "YES")

    def test_exchange_odd_lists(self):
        self.assertEqual(exchange([1, 3, 5], [1, 3, 5]), "NO")
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "NO")
        self.assertEqual(exchange([1, 3, 5], [1, 2, 4]), "NO")

    def test_exchange_mixed_lists(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 5, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 5]), "NO")

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_exchange_even_lists`: Tests the function with even lists where it should return "YES".
2. `test_exchange_odd_lists`: Tests the function with odd lists where it should return "NO".
3. `test_exchange_mixed_lists`: Tests the function with mixed lists where it should return the correct result based on the possibility of exchanging elements to make all the elements of lst1 even.