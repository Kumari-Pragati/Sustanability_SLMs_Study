You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9]), 6)
        self.assertEqual(add([10, 11, 12, 13, 14, 15]), 24)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10]), 0)
        self.assertEqual(add([1, 3, 5, 2, 4, 6, 7, 8, 9, 10]), 6)
        self.assertEqual(add([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 24)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 6)
        self.assertEqual(add([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 24)
        self.assertEqual(add([0, 2, 4, 6, 8, 10]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including both even and odd numbers, as well as numbers at both even and odd indices. It also includes test cases where the sum of the even numbers at odd indices is not zero.