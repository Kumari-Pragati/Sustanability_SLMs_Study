You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `separate_paren_groups` function:


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
        self.assertEqual(separate_paren_groups('((()))'), ['()', '()'])

    def test_mixed_characters(self):
        self.assertEqual(separate_paren_groups('(a b (c d) e)'), ['(a b (c d) e)', '()'])

    def test_unbalanced_parentheses(self):
        self.assertNotEqual(separate_paren_groups('(('), separate_paren_groups('(()')), 'Unbalanced parentheses should not return a list.')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as empty strings, single groups, multiple groups, nested groups, mixed characters, and unbalanced parentheses. The last test case checks for unbalanced parentheses to ensure that the function behaves correctly when it encounters invalid input.