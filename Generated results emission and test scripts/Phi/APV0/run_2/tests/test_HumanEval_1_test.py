Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_1_code import separate_paren_groups
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result

 import unittest
from HumanEval_1_code import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_single_parentheses(self):
        self.assertEqual(separate_paren_groups('()'), ['()'])

    def test_multiple_parentheses(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_balanced_parentheses(self):
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])

    def test_unbalanced_parentheses(self):
        self.assertEqual(separate_paren_groups('((())'), ['((', '()')])

    def test_nested_parentheses(self):
        self.assertEqual(separate_paren_groups('((( ) )'), ['(((', '()')])

    def test_no_parentheses(self):
        self.assertEqual(separate_paren_groups('abc'), [])

    def test_parentheses_with_spaces(self):
        self.assertEqual(separate_paren_groups('( ) ( ) ( )'), ['()', '()', '()'])

    def test_parentheses_with_other_chars(self):
        self.assertEqual(separate_paren_groups('(a) (b) (c)'), ['(a)', '(b)', '(c)'])

if __name__ == '__main__':
    unittest.main()