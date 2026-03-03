You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_96_code import count_up_to
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    For example:
    count_up_to(5) => [2, 3]
    count_up_to(11) => [2, 3, 5, 7]
    count_up_to(0) => []
    count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
    count_up_to(1) => []
    count_up_to(18) => [2, 3, 5, 7, 11, 13, 17]
    """

    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_96_code import count_up_to

class TestCountUpTo(unittest.TestCase):

    def test_count_up_to_5(self):
        self.assertEqual(count_up_to(5), [2, 3])

    def test_count_up_to_11(self):
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])

    def test_count_up_to_0(self):
        self.assertEqual(count_up_to(0), [])

    def test_count_up_to_20(self):
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_up_to_1(self):
        self.assertEqual(count_up_to(1), [])

    def test_count_up_to_18(self):
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for all the given examples in the function's docstring. It uses the `unittest` framework's `assertEqual` method to check that the output of the `count_up_to` function matches the expected output for each test case.

Please note that the `count_up_to` function is not optimized for large inputs. It has a time complexity of O(n^2), which can be improved to O(n log n) by using a more efficient algorithm to check for primality, such as the Sieve of Eratosthenes.