You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_94_code import skjkasdkd
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def isPrime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    result = sum(int(digit) for digit in str(maxx))
    return result


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_94_code import skjkasdkd

class TestSkjkasdkd(unittest.TestCase):
    def test_skjkasdkd(self):
        self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(skjkasdkd([0,81,12,3,1,21]), 3)
        self.assertEqual(skjkasdkd([0,8,1,2,1,7]), 7)
        self.assertEqual(skjkasdkd([1]), 1)
        self.assertEqual(skjkasdkd([2]), 2)
        self.assertEqual(skjkasdkd([3]), 3)
        self.assertEqual(skjkasdkd([5]), 5)
        self.assertEqual(skjkasdkd([7]), 7)
        self.assertEqual(skjkasdkd([11]), 2)
        self.assertEqual(skjkasdkd([13]), 4)
        self.assertEqual(skjkasdkd([17]), 5)
        self.assertEqual(skjkasdkd([19]), 4)
        self.assertEqual(skjkasdkd([23]), 7)
        self.assertEqual(skjkasdkd([29]), 5)
        self.assertEqual(skjkasdkd([31]), 5)
        self.assertEqual(skjkasdkd([37]), 5)
        self.assertEqual(skjkasdkd([41]), 6)
        self.assertEqual(skjkasdkd([43]), 5)
        self.assertEqual(skjkasdkd([47]), 6)
        self.assertEqual(skjkasdkd([53]), 6)
        self.assertEqual(skjkasdkd([59]), 7)
        self.assertEqual(skjkasdkd([61]), 7)
        self.assertEqual(skjkasdkd([67]), 8)
        self.assertEqual(skjkasdkd([71]), 8)
        self.assertEqual(skjkasdkd([73]), 8)
        self.assertEqual(skjkasdkd([79]), 8)
        self.assertEqual(skjkasdkd([83]), 9)
        self.assertEqual(skjkasdkd([89]), 9)
        self.assertEqual(skjkasdkd([97]), 10)

if __name__ == '__main__':
    unittest.main()


This script tests the function with a variety of inputs, including both prime and non-prime numbers, as well as single-digit and multi-digit prime numbers. It also tests the function with the smallest and largest prime numbers in the range of 1 to 100.