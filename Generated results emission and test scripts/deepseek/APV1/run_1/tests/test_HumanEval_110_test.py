You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_110_code import exchange

class TestExchange(unittest.TestCase):

    def test_all_even(self):
        self.assertEqual(exchange([2, 4, 6, 8], [1, 2, 3, 4]), "YES")

    def test_all_odd(self):
        self.assertEqual(exchange([1, 3, 5, 7], [1, 2, 3, 4]), "NO")

    def test_mixed(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_empty_lists(self):
        self.assertEqual(exchange([], []), "YES")

    def test_single_element(self):
        self.assertEqual(exchange([1], [2]), "YES")
        self.assertEqual(exchange([2], [1]), "YES")

    def test_large_lists(self):
        self.assertEqual(exchange(list(range(1, 10001, 2)), list(range(2, 10002, 2))), "YES")
        self.assertEqual(exchange(list(range(1, 10001, 2)), list(range(1, 10001, 2))), "NO")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- When all elements in the first list are even and the second list has at least as many even numbers as odd numbers in the first list.
- When all elements in the first list are odd.
- When the first list has a mix of even and odd numbers, and the second list has at least as many even numbers as odd numbers in the first list.
- When both lists are empty.
- When both lists have a single element.
- When both lists have large numbers of elements.

The test suite assumes that the function `exchange` is correctly implemented in the module `HumanEval_110_code`.