Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `count_up_to` function:


import unittest
from HumanEval_96_code import count_up_to

class TestCountUpTo(unittest.TestCase):
    def test_count_up_to(self):
        self.assertEqual(count_up_to(0), [])
        self.assertEqual(count_up_to(1), [])
        self.assertEqual(count_up_to(2), [2])
        self.assertEqual(count_up_to(3), [2])
        self.assertEqual(count_up_to(5), [2, 3])
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(count_up_to(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `count_up_to` function with various input values. It uses the `assertEqual` method to check if the output of the function matches the expected output. If the function returns the correct output for all test cases, the test will pass. If not, the test will fail and provide an error message indicating which test case failed.