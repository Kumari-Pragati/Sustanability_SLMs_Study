system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_14_code import all_prefixes
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[: i + 1])
    return result


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertEqual(all_prefixes('hello'), ['h', 'he', 'hel', 'hell', 'hello'])
        self.assertEqual(all_prefixes('x'), ['x'])
        self.assertEqual(all_prefixes('shortest'), ['s', 'sh', 'shi', 'shi', 'short', 'shorte', 'shorter', 'shortest'])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestAllPrefixes` class that inherits from `unittest.TestCase`. It contains a single method `test_all_prefixes`, which tests the `all_prefixes` function using several assertions based on the expected output for different inputs. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.