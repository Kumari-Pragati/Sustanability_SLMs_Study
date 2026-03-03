system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]


assistant

import unittest

# Function to be tested
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(parse_nested_parens(""), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens("()"), [1])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens("(()) () ((()))"), [2, 1, 3])

    def test_balanced_groups(self):
        self.assertEqual(parse_nested_parens("(((())))"), [4])

    def test_unbalanced_groups(self):
        self.assertEqual(parse_nested_parens(")("), [])

    def test_mixed_groups(self):
        self.assertEqual(parse_nested_parens("(()) (()) (((())))"), [2, 2, 5])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestParseNestedParens` that inherits from `unittest.TestCase`. It contains several test methods to verify different scenarios as described in the problem statement. The `assertEqual` method is used to check if the output of the `parse_nested_parens` function matches the expected results. Finally, the `unittest.main()` call runs all the tests when this script is executed directly.