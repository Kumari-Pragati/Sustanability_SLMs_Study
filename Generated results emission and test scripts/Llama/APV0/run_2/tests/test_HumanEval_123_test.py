user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_123_code import get_odd_collatz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    return sorted(odd_collatz)assistant

Here is the unittest test script for the `get_odd_collatz` function:

import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):
    def test_get_odd_collatz_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_get_odd_collatz_5(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_get_odd_collatz_6(self):
        self.assertEqual(get_odd_collatz(6), [])

    def test_get_odd_collatz_10(self):
        self.assertEqual(get_odd_collatz(10), [])

    def test_get_odd_collatz_3(self):
        self.assertEqual(get_odd_collatz(3), [1, 3])

    def test_get_odd_collatz_7(self):
        self.assertEqual(get_odd_collatz(7), [1, 7])

    def test_get_odd_collatz_8(self):
        self.assertEqual(get_odd_collatz(8), [])

    def test_get_odd_collatz_9(self):
        self.assertEqual(get_odd_collatz(9), [1, 9])

    def test_get_odd_collatz_12(self):
        self.assertEqual(get_odd_collatz(12), [])

    def test_get_odd_collatz_15(self):
        self.assertEqual(get_odd_collatz(15), [1, 3, 15])

    def test_get_odd_collatz_20(self):
        self.assertEqual(get_odd_collatz(20), [])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestGetOddCollatz` class with 10 test methods, each testing a different input to the `get_odd_collatz` function. The expected output for each test is specified using the `assertEqual` method.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that the tests were successful. If any tests fail, you will see an error message indicating which test failed and why.