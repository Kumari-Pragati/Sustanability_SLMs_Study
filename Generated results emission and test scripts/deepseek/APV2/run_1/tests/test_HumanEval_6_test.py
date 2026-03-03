You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_no_groups(self):
        self.assertEqual(parse_nested_parens('     '), [])

    def test_nested_groups(self):
        self.assertEqual(parse_nested_parens('((()))'), [5])

    def test_single_group_with_spaces(self):
        self.assertEqual(parse_nested_parens(' ( ) '), [1])

    def test_multiple_groups_with_spaces(self):
        self.assertEqual(parse_nested_parens(' (())  ()  ((())) '), [2, 1, 3])

    def test_mixed_spaces_and_groups(self):
        self.assertEqual(parse_nested_parens('  (())  ()  ((()))  '), [2, 1, 3])

    def test_group_with_inner_spaces(self):
        self.assertEqual(parse_nested_parens('( )'), [1])

    def test_group_with_inner_spaces_and_spaces(self):
        self.assertEqual(parse_nested_parens('(  )'), [1])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, such as empty strings, strings with no groups, groups with different levels of nesting, and groups with spaces within them.