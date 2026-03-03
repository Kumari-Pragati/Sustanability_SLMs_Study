You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_63_code import fibfib

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

 import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)

    def test_known_values(self):
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(10), 124)
        self.assertEqual(fibfib(15), 10946)

    def test_edge_cases(self):
        self.assertEqual(fibfib(-1), None)  # Assuming the function should handle negative inputs
        self.assertEqual(fibfib(20), 1346269)  # Known value for fibfib(20)

    def test_performance(self):
        # This test is not a typical unit test and would require a performance test
        # Here we can use timeit or similar to measure the execution time
        import timeit
        execution_time = timeit.timeit('fibfib(30)', globals=globals(), number=100)
        self.assertLess(execution_time, 1)  # Assuming the function should run in less than 1 second for n=30

if __name__ == '__main__':
    unittest.main()