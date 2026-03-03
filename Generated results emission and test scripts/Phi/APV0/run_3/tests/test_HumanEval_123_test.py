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
    return sorted(odd_collatz)

 import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_collatz_sequence_for_5(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_collatz_sequence_for_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_collatz_sequence_for_10(self):
        self.assertEqual(get_odd_collatz(10), [1])

    def test_collatz_sequence_for_15(self):
        self.assertEqual(get_odd_collatz(15), [1, 17])

    def test_collatz_sequence_for_21(self):
        self.assertEqual(get_odd_collatz(21), [1, 7])

    def test_collatz_sequence_for_22(self):
        self.assertEqual(get_odd_collatz(22), [1])

    def test_collatz_sequence_for_23(self):
        self.assertEqual(get_odd_collatz(23), [23])

    def test_collatz_sequence_for_24(self):
        self.assertEqual(get_odd_collatz(24), [1])

    def test_collatz_sequence_for_25(self):
        self.assertEqual(get_odd_collatz(25), [1, 16])

    def test_collatz_sequence_for_26(self):
        self.assertEqual(get_odd_collatz(26), [1])

    def test_collatz_sequence_for_27(self):
        self.assertEqual(get_odd_collatz(27), [27])

    def test_collatz_sequence_for_28(self):
        self.assertEqual(get_odd_collatz(28), [1])

    def test_collatz_sequence_for_29(self):
        self.assertEqual(get_odd_collatz(29), [29])

    def test_collatz_sequence_for_30(self):
        self.assertEqual(get_odd_collatz(30), [1])

if __name__ == '__main__':
    unittest.main()