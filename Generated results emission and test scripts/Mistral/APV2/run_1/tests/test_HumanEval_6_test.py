You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `parse_nested_parens` function:


import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(parse_nested_parens(''), [])

    def test_single_group(self):
        self.assertListEqual(parse_nested_parens('(())'), [2])
        self.assertListEqual(parse_nested_parens('()'), [0])
        self.assertListEqual(parse_nested_parens('()()'), [0])
        self.assertListEqual(parse_nested_parens('((()))'), [3])

    def test_multiple_groups(self):
        self.assertListEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
        self.assertListEqual(parse_nested_parens('((())) (())'), [3, 2])
        self.assertListEqual(parse_nested_parens('() () ()'), [0, 0, 0])

    def test_spaces_and_newlines(self):
        self.assertListEqual(parse_nested_parens('(()) ()\n  ((()))'), [2, 1, 3])
        self.assertListEqual(parse_nested_parens('(()) ()\t ((()))'), [2, 1, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the edge cases, multiple groups, and handling spaces and newlines in the input string. Make sure to run this test suite after making any changes to the `parse_nested_parens` function to ensure that the function still works as expected.