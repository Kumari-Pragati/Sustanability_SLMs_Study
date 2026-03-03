system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_15_code import string_sequence

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(x) for x in range(n + 1))


assistant

import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestStringSequence` class that inherits from `unittest.TestCase`. It contains a single method `test_string_sequence`, which uses assertions to check if the `string_sequence` function returns the expected results for different input values (0 and 5). The `assertEqual` method compares the output of `string_sequence` with the expected strings, ensuring that the function behaves as intended. Finally, the `unittest.main()` call at the end runs all tests defined within this class.