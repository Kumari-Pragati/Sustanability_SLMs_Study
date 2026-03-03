You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_110_code import exchange

class TestExchange(unittest.TestCase):

    def test_exchange_yes(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "YES")
        self.assertEqual(exchange([2, 2, 2, 2], [1, 1, 1, 1]), "YES")
        self.assertEqual(exchange([2, 2, 2, 2], [2, 2, 2, 2]), "YES")
        self.assertEqual(exchange([1, 1, 1, 1], [2, 2, 2, 2]), "YES")

    def test_exchange_no(self):
        self.assertEqual(exchange([1, 3, 5, 7], [1, 2, 3, 4]), "NO")
        self.assertEqual(exchange([1, 3, 5, 7], [1, 3, 5, 7]), "NO")
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 6, 8]), "NO")
        self.assertEqual(exchange([1, 3, 5, 7], [1, 1, 1, 1]), "NO")
        self.assertEqual(exchange([1, 1, 1, 1], [2, 2, 2, 2]), "NO")

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_exchange_yes` and `test_exchange_no`. The first one checks if the function returns "YES" when it's possible to exchange elements between the two lists to make all elements in the first list even. The second one checks if the function returns "NO" when it's not possible to do so.

Please note that you need to have the function `exchange` in the file `HumanEval_110_code.py` for the script to work.