You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_1_code import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_single_group(self):
        self.assertEqual(separate_paren_groups('()'), ['()'])

    def test_multiple_groups(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_nested_groups(self):
        self.assertEqual(separate_paren_groups('(())()(()())'), ['(())', '()', '(()())'])

    def test_spaces_in_string(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_unbalanced_groups(self):
        with self.assertRaises(Exception):
            separate_paren_groups('( ) (( )) )( ( )')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty strings, single groups, multiple groups, nested groups, spaces in the string, and unbalanced groups. The test for unbalanced groups checks that the function raises an exception when given an unbalanced string of parentheses.