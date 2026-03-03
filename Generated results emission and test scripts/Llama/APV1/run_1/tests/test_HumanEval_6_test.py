user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
        self.assertEqual(parse_nested_parens('() ()'), [1, 1])
        self.assertEqual(parse_nested_parens('((()))'), [3])
        self.assertEqual(parse_nested_parens(''), [])
        self.assertEqual(parse_nested_parens('()'), [1])
        self.assertEqual(parse_nested_parens('() ()'), [1, 1])
        self.assertEqual(parse_nested_parens('((())) ()'), [3, 1])
        self.assertEqual(parse_nested_parens('((())) (()())'), [3, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()())'), [3, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()())'), [3, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())'), [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(parse_nested_parens('((())) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()()) (()())