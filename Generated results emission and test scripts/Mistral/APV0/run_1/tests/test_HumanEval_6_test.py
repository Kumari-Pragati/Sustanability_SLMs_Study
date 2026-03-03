Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_6_code import parse_nested_parens
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """For a string of balanced parentheses groups separated by spaces,
    return a list with the maximum nesting depth for each group.
    >>> parse_nested_parens('(()) () ((()))')
    [2, 1, 3]
    """
    def parse_paren_group(group: str) -> int:
        depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                depth -= 1
        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

 Here is a unittest test script for the `parse_nested_parens` function:


import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
        self.assertEqual(parse_nested_parens('()'), [0])
        self.assertEqual(parse_nested_parens('(()())'), [2])
        self.assertEqual(parse_nested_parens('(())(())'), [2, 2])
        self.assertEqual(parse_nested_parens(''), [])
        self.assertEqual(parse_nested_parens('(()) (())'), [2, 2])
        self.assertEqual(parse_nested_parens('((()))'), [3])
        self.assertEqual(parse_nested_parens('(()) ((()))'), [2, 3])
        self.assertEqual(parse_nested_parens('() ()'), [0, 0])
        self.assertEqual(parse_nested_parens('(()) ()'), [2, 0])
        self.assertEqual(parse_nested_parens('() (())'), [0, 2])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover various scenarios, such as empty strings, strings with only one group of parentheses, strings with multiple groups of parentheses, and strings with mixed spaces and parentheses. The test cases are designed to ensure that the function correctly identifies the maximum nesting depth for each group of parentheses.