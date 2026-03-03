You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_119_code import match_parens

class TestMatchParens(unittest.TestCase):

    def test_match_parens_yes(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens(['(', ')(']), 'Yes')
        self.assertEqual(match_parens(['()', '()']), 'Yes')
        self.assertEqual(match_parens(['(', ')']), 'Yes')

    def test_match_parens_no(self):
        self.assertEqual(match_parens([')', ')']), 'No')
        self.assertEqual(match_parens(['()(', '))']), 'No')
        self.assertEqual(match_parens(['(', '))']), 'No')
        self.assertEqual(match_parens(['(', '(']), 'No')

    def test_match_parens_empty(self):
        self.assertEqual(match_parens(['', '']), 'Yes')

    def test_match_parens_single_parentheses(self):
        self.assertEqual(match_parens(['(', ']']), 'No')
        self.assertEqual(match_parens(['(', '(']), 'No')
        self.assertEqual(match_parens(['(', ')']), 'Yes')

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including both 'Yes' and 'No' scenarios, as well as edge cases such as empty strings and strings with a single parentheses.