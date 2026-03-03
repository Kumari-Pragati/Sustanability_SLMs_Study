You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a comprehensive unittest test suite for the given Python function:


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
        self.assertEqual(skjkasdkd([4]), 4)
        self.assertEqual(skjkasdkd([5]), 5)
        self.assertEqual(skjkasdkd([6]), 6)
        self.assertEqual(skjkasdkd([7]), 7)
        self.assertEqual(skjkasdkd([8]), 8)
        self.assertEqual(skjkasdkd([9]), 9)
        self.assertEqual(skjkasdkd([10]), 1)
        self.assertEqual(skjkasdkd([11]), 2)
        self.assertEqual(skjkasdkd([12]), 3)
        self.assertEqual(skjkasdkd([13]), 4)
        self.assertEqual(skjkasdkd([14]), 5)
        self.assertEqual(skjkasdkd([15]), 6)
        self.assertEqual(skjkasdkd([16]), 7)
        self.assertEqual(skjkasdkd([17]), 8)
        self.assertEqual(skjkasdkd([18]), 9)
        self.assertEqual(skjkasdkd([19]), 1)
        self.assertEqual(skjkasdkd([20]), 2)
        self.assertEqual(skjkasdkd([21]), 4)
        self.assertEqual(skjkasdkd([22]), 5)
        self.assertEqual(skjkasdkd([23]), 7)
        self.assertEqual(skjkasdkd([24]), 6)
        self.assertEqual(skjkasdkd([25]), 8)
        self.assertEqual(skjkasdkd([26]), 1)
        self.assertEqual(skjkasdkd([27]), 4)
        self.assertEqual(skjkasdkd([28]), 8)
        self.assertEqual(skjkasdkd([29]), 3)
        self.assertEqual(skjkasdkd([30]), 4)
        self.assertEqual(skjkasdkd([31]), 7)
        self.assertEqual(skjkasdkd([32]), 1)
        self.assertEqual(skjkasdkd([33]), 5)
        self.assertEqual(skjkasdkd([34]), 9)
        self.assertEqual(skjkasdkd([35]), 5)
        self.assertEqual(skjkasdkd([36]), 7)
        self.assertEqual(skjkasdkd([37]), 1)
        self.assertEqual(