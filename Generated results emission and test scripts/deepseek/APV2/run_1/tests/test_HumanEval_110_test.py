You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_110_code import exchange

class TestExchange(unittest.TestCase):

    def test_exchange_possible(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "YES")
        self.assertEqual(exchange([2, 2, 2, 2], [1, 1, 1, 1]), "YES")
        self.assertEqual(exchange([1, 1, 1, 1], [2, 2, 2, 2]), "YES")
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 6, 8]), "YES")

    def test_exchange_not_possible(self):
        self.assertEqual(exchange([1, 3, 5, 7], [1, 3, 5, 7]), "NO")
        self.assertEqual(exchange([1, 2, 3, 4], [5, 6, 7, 8]), "NO")
        self.assertEqual(exchange([2, 4, 6, 8], [1, 3, 5, 7]), "NO")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 3, 5, 7]), "NO")
        self.assertEqual(exchange([1, 1, 1, 1], [2, 2, 2, 2]), "NO")

if __name__ == '__main__':
    unittest.main()


This test suite includes two test methods: `test_exchange_possible` and `test_exchange_not_possible`. The first method tests cases where the exchange is possible, while the second method tests cases where the exchange is not possible. Each method uses the `assertEqual` method to check if the output of the `exchange` function matches the expected result.