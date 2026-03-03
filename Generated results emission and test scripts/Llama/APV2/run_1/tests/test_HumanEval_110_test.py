system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return "NO"assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_110_code import exchange

class TestExchange(unittest.TestCase):

    def test_exchange_YES(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_exchange_NO(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_exchange_YES_empty(self):
        self.assertEqual(exchange([], [2, 4, 6]), "YES")

    def test_exchange_NO_empty(self):
        self.assertEqual(exchange([1, 3], []), "NO")

    def test_exchange_YES_single_element(self):
        self.assertEqual(exchange([2], [4]), "YES")

    def test_exchange_NO_single_element(self):
        self.assertEqual(exchange([1], [4]), "NO")

    def test_exchange_YES_multiple_elements(self):
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_exchange_NO_multiple_elements(self):
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "NO")

if __name__ == '__main__':
    unittest.main()