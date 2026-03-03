system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_6_code import parse_nested_parens
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

# Importing the function we want to test
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    
    def test_normal_input(self):
        # Normal input case
        result = parse_nested_parens("(()) () ((()))")
        expected_result = [2, 1, 3]
        self.assertListEqual(result, expected_result)
        
    def test_edge_case(self):
        # Edge case where there's no space between strings
        result = parse_nested_parens("()()")
        expected_result = [1, 1]
        self.assertListEqual(result, expected_result)
        
    def test_invalid_input(self):
        # Invalid input (contains non-parentheses characters)
        result = parse_nested_parens("((())")
        expected_result = []
        self.assertListEqual(result, expected_result)
        
    def test_empty_input(self):
        # Empty input
        result = parse_nested_parens("")
        expected_result = []
        self.assertListEqual(result, expected_result)
        
    def test_single_element_input(self):
        # Single element input
        result = parse_nested_parens("()")
        expected_result = [1]
        self.assertListEqual(result, expected_result)
        
    def test_complex_input(self):
        # Complex input with nested groups
        result = parse_nested_parens("(()()) (()) (((())))")
        expected_result = [3, 2, 3]
        self.assertListEqual(result, expected_result)
        
    def test_large_input(self):
        # Large input with many groups
        result = parse_nested_parens("((((((((()()()())(())()))))))")
        expected_result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertListEqual(result, expected_result)
        
    def test_mixed_input(self):
        # Mixed input with different types of parentheses
        result = parse_nested_parens("((())()())")
        expected_result = [2, 1, 2]
        self.assertListEqual(result, expected_result)
        
    def test_unbalanced_input(self):
        # Unbalanced input
        result = parse_nested_parens("(()")
        expected_result = []
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_spaces(self):
        # Balanced input with spaces
        result = parse_nested_parens("() () ()")
        expected_result = [1, 1, 1]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_trailing_space(self):
        # Balanced input with trailing space
        result = parse_nested_parens("() () ")
        expected_result = [1, 1]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_leading_space(self):
        # Balanced input with leading space
        result = parse_nested_parens(" () ()")
        expected_result = [1, 1]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_multiple_groups(self):
        # Balanced input with multiple groups
        result = parse_nested_parens("()(())()((()))")
        expected_result = [2, 1, 3]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_different_types_of_parens(self):
        # Balanced input with different types of parentheses
        result = parse_nested_parens("((())()())")
        expected_result = [2, 1, 2]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_all_types_of_parens(self):
        # Balanced input with all types of parentheses
        result = parse_nested_parens("((())()()())")
        expected_result = [3, 2, 3]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_longest_nesting(self):
        # Balanced input with longest nesting
        result = parse_nested_parens("(((())()()())"))
        expected_result = [4, 3, 4]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_shortest_nesting(self):
        # Balanced input with shortest nesting
        result = parse_nested_parens("((())()())")
        expected_result = [2, 1, 2]
        self.assertListEqual(result, expected_result)
        
    def test_balanced_input_with_evenly_distributed_nesting(self):
        # Balanced input with evenly distributed nesting
        result = parse_nested_parens("((())()()())")
        expected_result = [3, 2, 3]
        self.assertListEqual(result, expected