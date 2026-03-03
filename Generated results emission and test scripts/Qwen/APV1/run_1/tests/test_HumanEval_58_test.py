system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_58_code import common

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))


assistant

import unittest
from HumanEval_58_code import common

class TestCommon(unittest.TestCase):
    def test_common(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestCommon` class that inherits from `unittest.TestCase`. It contains a single method `test_common`, which tests the `common` function using assertEqual assertions. The first test case checks if the function correctly identifies common elements between two lists `[1, 4, 3, 34, 653, 2, 5]` and `[5, 7, 1, 5, 9, 653, 121]`, expecting the output `[1, 5, 653]`. The second test case checks if it correctly identifies common elements between `[5, 3, 2, 8]` and `[3, 2]`, expecting the output `[2, 3]`. If any of these tests fail, the corresponding assertion will raise an error, indicating that something went wrong with the implementation of the `common` function.