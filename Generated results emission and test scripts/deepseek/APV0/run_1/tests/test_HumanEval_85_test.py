You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 3, 5, 7]), 0)
        self.assertEqual(add([2, 4, 6, 8]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)
        self.assertEqual(add([10, 20, 30, 40, 50]), 10)
        self.assertEqual(add([1, 3, 5, 2, 4, 6, 7, 8, 9]), 4)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 2)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestAdd` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_add` that tests the `add` function with various test cases. Each test case checks if the output of the `add` function matches the expected result.

The `if __name__ == '__main__': unittest.main()` line at the end of the script is used to run the tests when the script is executed directly.

Please note that the `HumanEval_85_code` module and the `add` function should be defined in a separate Python file for this script to work correctly.