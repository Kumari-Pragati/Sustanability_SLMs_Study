user

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

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]assistant

Here is the unittest test script for the `parse_nested_parens` function:

import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens("(())"), [2])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens("(()) () ((()))"), [2, 1, 3])

    def test_group_with_no_parens(self):
        self.assertEqual(parse_nested_parens("a b c"), [])

    def test_group_with_unbalanced_parens(self):
        with self.assertRaises(ValueError):
            parse_nested_parens("(())(")

    def test_group_with_spaces(self):
        self.assertEqual(parse_nested_parens("(  ) (  ) ((  ))"), [2, 1, 3])

    def test_group_with_leading_trailing_spaces(self):
        self.assertEqual(parse_nested_parens(" (  ) (  ) ((  )) "), [2, 1, 3])

    def test_group_with_parens_at_end(self):
        self.assertEqual(parse_nested_parens("(()) (()) (())"), [2, 2, 2])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestParseNestedParens` class with 7 test methods:

1. `test_empty_string`: Tests that an empty string returns an empty list.
2. `test_single_group`: Tests that a single group of parentheses returns the correct maximum nesting depth.
3. `test_multiple_groups`: Tests that multiple groups of parentheses return the correct maximum nesting depths.
4. `test_group_with_no_parens`: Tests that a group with no parentheses returns an empty list.
5. `test_group_with_unbalanced_parens`: Tests that a group with unbalanced parentheses raises a `ValueError`.
6. `test_group_with_spaces`: Tests that a group with spaces between the parentheses returns the correct maximum nesting depth.
7. `test_group_with_leading_trailing_spaces`: Tests that a group with leading and trailing spaces returns the correct maximum nesting depth.
8. `test_group_with_parens_at_end`: Tests that a group with parentheses at the end returns the correct maximum nesting depth.

You can run this script directly to execute the tests.