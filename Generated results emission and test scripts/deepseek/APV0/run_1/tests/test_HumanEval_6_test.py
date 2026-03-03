You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('()'), [1])
        self.assertEqual(parse_nested_parens('(())'), [2])
        self.assertEqual(parse_nested_parens('((()))'), [3])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
        self.assertEqual(parse_nested_parens('() (()) ((())) ()'), [1, 2, 3, 1])

    def test_mixed_depths(self):
        self.assertEqual(parse_nested_parens('() (()) ((())) () (())'), [1, 2, 3, 1, 2])

    def test_spaces(self):
        self.assertEqual(parse_nested_parens('  (())  ()  ((()))  '), [2, 1, 3])

    def test_no_spaces(self):
        self.assertEqual(parse_nested_parens('(())()((()))'), [2, 1, 3])

if __name__ == '__main__':
    unittest.main()


This script includes tests for empty strings, single groups, multiple groups with different depths, and cases with spaces and no spaces.