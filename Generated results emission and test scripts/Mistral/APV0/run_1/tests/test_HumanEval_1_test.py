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

 Here is a unittest test script for the `separate_paren_groups` function:


import unittest
from HumanEval_1_code import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_separate_paren_groups(self):
        self.assertEqual(separate_paren_groups(''), [])
        self.assertEqual(separate_paren_groups('('), ['()'])
        self.assertEqual(separate_paren_groups('()'), [''])
        self.assertEqual(separate_paren_groups('((()))'), ['()', '()'])
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
        self.assertEqual(separate_paren_groups('(a + b)(c + d)'), ['(a + b)', '(c + d)'])
        self.assertEqual(separate_paren_groups('((a + b)(c + d))'), ['((a + b)(c + d))'])
        self.assertEqual(separate_paren_groups('(a + b(c + d))'), ['(a + (b(c + d)))'])
        self.assertEqual(separate_paren_groups('(a + b(c + d))(e + f)'), ['(a + (b(c + d)))', '(e + f)'])

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for an empty string, single parentheses, nested parentheses, mixed parentheses with spaces, and more complex cases with nested expressions. Make sure to save this script as a .py file and run it using the command `python test_separate_paren_groups.py` to execute the tests.