Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_36_code import fizz_buzz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

 Here is a unittest test script for the `fizz_buzz` function:


import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(78), 2)
        self.assertEqual(fizz_buzz(79), 3)
        self.assertEqual(fizz_buzz(100), 3)
        self.assertEqual(fizz_buzz(111), 1)
        self.assertEqual(fizz_buzz(130), 0)
        self.assertEqual(fizz_buzz(143), 1)
        self.assertEqual(fizz_buzz(150), 2)
        self.assertEqual(fizz_buzz(200), 13)
        self.assertEqual(fizz_buzz(300), 29)

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the given examples and some additional test cases to ensure the function works correctly for a range of inputs. You can run this script directly to test the `fizz_buzz` function.