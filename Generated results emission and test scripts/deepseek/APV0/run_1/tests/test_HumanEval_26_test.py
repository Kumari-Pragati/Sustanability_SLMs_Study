You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_26_code import remove_duplicates
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])

    def test_mixed_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4, 4, 5]), [1, 5])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2]), [1, 2])

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestRemoveDuplicates` that inherits from `unittest.TestCase`. It then defines several test methods, each testing a different scenario. The `assertEqual` method is used to check that the output of the `remove_duplicates` function matches the expected output.

To run the tests, you can simply execute this script. If you're using a command line, you can do this by typing `python test_script.py` (replace `test_script.py` with the name of this file). If you're using an IDE, you can usually run the script by right-clicking on it and selecting "Run".

Please note that you need to have the `HumanEval_26_code` module with the `remove_duplicates` function defined in it. If you don't have this module, you can create it with the following content:


from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


Save this code in a file named `HumanEval_26_code.py` in the same directory as your test script.