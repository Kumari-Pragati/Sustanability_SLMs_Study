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
    return (even_count, odd_count)

 Here is a unittest test script for the `even_odd_count` function:


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(10), (1, 0))
        self.assertEqual(even_odd_count(20), (2, 1))
        self.assertEqual(even_odd_count(30), (1, 2))
        self.assertEqual(even_odd_count(40), (2, 1))
        self.assertEqual(even_odd_count(50), (1, 2))
        self.assertEqual(even_odd_count(60), (2, 1))
        self.assertEqual(even_odd_count(70), (1, 2))
        self.assertEqual(even_odd_count(80), (2, 1))
        self.assertEqual(even_odd_count(90), (1, 2))
        self.assertEqual(even_odd_count(100), (2, 0))
        self.assertEqual(even_odd_count(-100), (2, 0))
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(-0), (1, 0))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `even_odd_count` function with various positive and negative numbers. The test case uses the `assertEqual` method to check if the output of the function matches the expected output. If the function returns the correct output, the test will pass; otherwise, it will fail.