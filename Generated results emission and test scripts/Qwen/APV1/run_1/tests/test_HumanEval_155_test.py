system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(2468), (4, 0))
        self.assertEqual(even_odd_count(-987654321), (4, 8))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestEvenOddCount` class within the `unittest` framework. The `test_even_odd_count` method contains several assertions to check the correctness of the `even_odd_count` function against various inputs. If any assertion fails, it will raise an error indicating which test failed. Running this script will execute all tests defined in the class and print out whether each test passed or failed.