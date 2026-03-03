system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]


assistant

import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens("(()) () ((()))"), [2, 1, 3])
        self.assertEqual(parse_nested_parens("(() ()) (()) (((())))"), [2, 1, 4, 3])
        self.assertEqual(parse_nested_parens(""), [])
        self.assertEqual(parse_nested_parens("((()))"), [5])
        self.assertEqual(parse_nested_parens("() () () ()"), [1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestParseNestedParens` class that inherits from `unittest.TestCase`. It contains two test methods: `test_parse_nested_parens`, which tests the function with various inputs and expected outputs. The `assertEqual` method checks if the output of `parse_nested_parens` matches the expected result. If any of these tests fail, it will raise an assertion error, indicating that there's a problem with the implementation of `parse_nested_parens`.