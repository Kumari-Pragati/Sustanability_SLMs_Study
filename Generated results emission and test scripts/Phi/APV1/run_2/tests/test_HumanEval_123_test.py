You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_collatz_sequence_for_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_collatz_sequence_for_5(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_collatz_sequence_for_7(self):
        self.assertEqual(get_odd_collatz(7), [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_10(self):
        self.assertEqual(get_odd_collatz(10), [10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_15(self):
        self.assertEqual(get_odd_collatz(15), [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_100(self):
        self.assertEqual(get_odd_collatz(100), [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_1000(self):
        self.assertEqual(get_odd_collatz(1000), [1000, 500, 250, 125, 376, 188, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1330, 665, 2216, 1108, 554, 277, 832, 416, 208, 104, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

if __name__ == '__main__':
    unittest.main()