system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_27_code import flip_case
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()


assistant

import unittest

# Provided function to be tested
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    
    def test_flip_case(self):
        # Test case 1: Single character input
        self.assertEqual(flip_case('a'), 'A')
        
        # Test case 2: All uppercase input
        self.assertEqual(flip_case('HELLO'), 'hELLO')
        
        # Test case 3: All lowercase input
        self.assertEqual(flip_case('hello'), 'Hello')
        
        # Test case 4: Mixed case input
        self.assertEqual(flip_case('H3LL0'), 'h3ll0')
        
        # Test case 5: Edge case with empty string
        self.assertEqual(flip_case(""), "")
        
        # Test case 6: Edge case with non-string input (should raise TypeError)
        with self.assertRaises(TypeError):
            flip_case(123)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure that `flip_case` works correctly across different scenarios, including edge cases such as empty strings and non-string inputs.