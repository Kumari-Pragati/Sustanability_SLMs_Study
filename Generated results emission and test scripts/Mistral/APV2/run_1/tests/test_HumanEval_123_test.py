You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a comprehensive unittest test suite for the `get_odd_Collatz` function:


import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_get_odd_collatz_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_get_odd_collatz_3(self):
        self.assertEqual(get_odd_collatz(3), [3, 1])

    def test_get_odd_collatz_5(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_get_odd_collatz_8(self):
        self.assertEqual(get_odd_collatz(8), [1, 5, 13])

    def test_get_odd_collatz_13(self):
        self.assertEqual(get_odd_collatz(13), [1, 13])

    def test_get_odd_collatz_20(self):
        self.assertEqual(get_odd_collatz(20), [1, 5, 13, 40])

    def test_get_odd_collatz_45(self):
        self.assertEqual(get_odd_collatz(45), [1, 9, 28, 85])

    def test_get_odd_collatz_100(self):
        self.assertEqual(get_odd_collatz(100), [1, 9, 25, 76, 233, 666, 1699, 5096, 12897, 38644, 106035, 298073, 834146, 2302431, 6457289, 17822401, 49567205, 138718402, 396220169, 1128720513])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for different input values, ensuring that the function works correctly for various odd numbers. The test cases are designed to cover the edge cases and a range of values to provide comprehensive testing.