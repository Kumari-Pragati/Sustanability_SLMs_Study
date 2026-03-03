### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_119_code import match_parens
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
### Instruction:
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

import unittest
from HumanEval_119_code import match_parens

class TestMatchParens(unittest.TestCase):
    def test_good_strings(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens(['(', ')()']), 'Yes')
        self.assertEqual(match_parens(['()', '()']), 'Yes')

    def test_bad_strings(self):
        self.assertEqual(match_parens(['(', ')']), 'No')
        self.assertEqual(match_parens(['()(', ')(']), 'No')
        self.assertEqual(match_parens(['(', '(']), 'No')

    def test_balanced_strings(self):
        self.assertEqual(match_parens(['()', '()']), 'Yes')
        self.assertEqual(match_parens(['(', ')']), 'Yes')
        self.assertEqual(match_parens(['()()', ')(']), 'Yes')

    def test_empty_strings(self):
        self.assertEqual(match_parens(['', '']), 'Yes')
        self.assertEqual(match_parens(['', '()']), 'Yes')
        self.assertEqual(match_parens(['()', '']), 'Yes')

if __name__ == '__main__':
    unittest.main()

This test suite includes tests for both good and bad cases, as well as cases where the strings are already balanced. It also includes tests for empty strings.