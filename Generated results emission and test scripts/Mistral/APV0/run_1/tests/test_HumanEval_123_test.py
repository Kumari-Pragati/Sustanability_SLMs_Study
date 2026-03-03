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

 Here is a unittest test script for the `get_odd_Collatz` function:


import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_get_odd_collatz_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_get_odd_collatz_2(self):
        self.assertEqual(get_odd_collatz(2), [1])

    def test_get_odd_collatz_3(self):
        self.assertEqual(get_odd_collatz(3), [3, 1])

    def test_get_odd_collatz_4(self):
        self.assertEqual(get_odd_collatz(4), [1])

    def test_get_odd_collatz_5(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_get_odd_collatz_6(self):
        self.assertEqual(get_odd_collatz(6), [1, 7])

    def test_get_odd_collatz_7(self):
        self.assertEqual(get_odd_collatz(8), [1, 9])

    def test_get_odd_collatz_8(self):
        self.assertEqual(get_odd_collatz(9), [9, 25, 125, 66, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(get_odd_collatz(9)[::-1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296])

if __name__ == '__main__':
    unittest.main()


This test script includes test cases for the base case (`n=1`), even numbers, and various odd numbers. The test case for `n=9` also checks that the function returns the correct sequence in reverse order and that the reversed sequence is also sorted in increasing order.