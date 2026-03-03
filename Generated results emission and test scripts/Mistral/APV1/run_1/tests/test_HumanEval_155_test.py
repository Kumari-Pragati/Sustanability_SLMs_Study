You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

 Here is a comprehensive unittest test suite for the given Python function `even_odd_count`. The test cases cover both positive and negative numbers, as well as edge cases like zero and single-digit numbers.


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(0), (0, 0))
        self.assertEqual(even_odd_count(1), (0, 1))
        self.assertEqual(even_odd_count(2), (1, 0))
        self.assertEqual(even_odd_count(3), (0, 1))
        self.assertEqual(even_odd_count(10), (2, 1))
        self.assertEqual(even_odd_count(100), (5, 1))
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(-1), (0, 1))
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-100), (4, 2))
        self.assertEqual(even_odd_count(-123), (1, 3))

if __name__ == '__main__':
    unittest.main()


This test suite uses the `unittest.TestCase.assertEqual` method to compare the expected and actual results. If the function works correctly, all test cases will pass, and the test suite will have a 100% test coverage.