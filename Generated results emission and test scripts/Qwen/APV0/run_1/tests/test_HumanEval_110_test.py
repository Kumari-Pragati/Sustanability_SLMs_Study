system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
def exchange(lst1, lst2):
    # Your implementation here

class TestExchange(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4], [1, 2, 3, 4], 'YES'),
            ([1, 2, 3, 4], [1, 5, 3, 4], 'NO'),
            ([1, 3, 5, 7], [2, 4, 6, 8], 'YES'),
            ([1, 3, 5, 7], [1, 3, 5, 7], 'YES')
        ]

    def test_exchange(self):
        for lst1, lst2, expected in self.test_cases:
            result = exchange(lst1, lst2)
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


This script defines a `TestExchange` class within the `unittest` module to test the `exchange` function. The `setUp` method initializes some test cases, each consisting of three lists (`lst1`, `lst2`, and the expected outcome). The `test_exchange` method iterates through these test cases, calling the `exchange` function with the given inputs and comparing the output against the expected result using assertions. Finally, the `unittest.main()` call runs the tests when the script is executed directly.