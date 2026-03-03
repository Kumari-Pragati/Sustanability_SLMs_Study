You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_119_code import match_parens
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_119_code import match_parens

class TestMatchParens(unittest.TestCase):
    def test_match_parens(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens(['(', ')']), 'No')
        self.assertEqual(match_parens(['()', ')(']), 'Yes')
        self.assertEqual(match_parens(['(', '(']), 'No')
        self.assertEqual(match_parens(['()', '()']), 'Yes')
        self.assertEqual(match_parens(['(', ')(']), 'Yes')
        self.assertEqual(match_parens(['()(', ')(']), 'Yes')
        self.assertEqual(match_parens(['()(', '(']), 'No')
        self.assertEqual(match_parens(['(', ')(']), 'No')
        self.assertEqual(match_parens(['()', ')']), 'Yes')
        self.assertEqual(match_parens(['(', '(']), 'No')
        self.assertEqual(match_parens(['()', '()']), 'Yes')

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestMatchParens` that inherits from `unittest.TestCase`. The `test_match_parens` method in this class contains a series of `assertEqual` calls that test the `match_parens` function with a variety of different inputs. Each call checks that the function's output matches the expected output.

The script ends with a call to `unittest.main()`, which runs all the test methods in the `TestMatchParens` class. If all the tests pass, the script will exit without printing anything. If any test fails, the script will print a detailed error message indicating which test failed and why.