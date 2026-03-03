user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return (even_count, odd_count)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(456), (2, 2))
        self.assertEqual(even_odd_count(789), (0, 3))
        self.assertEqual(even_odd_count(-456), (2, 2))
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(111), (0, 3))
        self.assertEqual(even_odd_count(-111), (0, 3))

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios, including negative numbers, zero, and single-digit numbers. The `assertEqual` method is used to compare the expected output with the actual output of the `even_odd_count` function.