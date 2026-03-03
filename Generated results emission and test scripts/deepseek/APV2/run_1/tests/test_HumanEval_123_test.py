You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sorted(odd_collatz)


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_get_odd_collatz(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])
        self.assertEqual(get_odd_collatz(10), [5])
        self.assertEqual(get_odd_collatz(1), [1])
        self.assertEqual(get_odd_collatz(2), [])
        self.assertEqual(get_odd_collatz(3), [3])
        self.assertEqual(get_odd_collatz(4), [5, 11])
        self.assertEqual(get_odd_collatz(6), [5])
        self.assertEqual(get_odd_collatz(7), [7])
        self.assertEqual(get_odd_collatz(8), [5, 11])
        self.assertEqual(get_odd_collatz(9), [5, 11])
        self.assertEqual(get_odd_collatz(12), [5, 11])

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case `test_get_odd_collatz` that tests the function with a variety of inputs. The `assertEqual` method is used to check that the output of the function matches the expected output for each input.

Please note that the function `get_odd_collatz` is expected to be in a file named `HumanEval_123_code.py` in the same directory as the test file.

Also, please note that the Collatz conjecture is a conjecture that has not been proven to be true for all positive integers. The test cases provided here are based on the conjecture and may not cover all possible edge cases.