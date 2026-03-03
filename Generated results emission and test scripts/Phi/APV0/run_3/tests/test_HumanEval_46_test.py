Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_46_code import fib4
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

 import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):

    def test_fib4_base_cases(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_fib4_sequences(self):
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
        self.assertEqual(fib4(8), 26)
        self.assertEqual(fib4(9), 40)
        self.assertEqual(fib4(10), 66)
        # Add more test cases as needed

    def test_fib4_edge_cases(self):
        self.assertEqual(fib4(-1), 0)  # Assuming the function handles negative input
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(100), 180537609)  # Large number test case

    def test_fib4_invalid_input(self):
        with self.assertRaises(TypeError):
            fib4("invalid")  # Testing with invalid input type

if __name__ == '__main__':
    unittest.main()