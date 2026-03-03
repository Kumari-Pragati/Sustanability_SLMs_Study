You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_90_code import next_smallest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):

    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertEqual(next_smallest([]), None)
        self.assertEqual(next_smallest([1, 1]), None)
        self.assertEqual(next_smallest([1, 2, 2, 3]), 2)
        self.assertEqual(next_smallest([1]), None)
        self.assertEqual(next_smallest([1, 2]), 1)
        self.assertEqual(next_smallest([1, 2, 3]), 2)
        self.assertEqual(next_smallest([1, 2, 3, 4]), 2)
        self.assertEqual(next_smallest([1, 2, 3, 4, 4]), 2)
        self.assertEqual(next_smallest([1, 2, 3, 4, 5, 5]), 2)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestNextSmallest` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_next_smallest` that tests the `next_smallest` function with a variety of inputs. Each test case uses the `assertEqual` method to check if the output of `next_smallest` matches the expected result.

The `if __name__ == '__main__': unittest.main()` line at the end of the script is used to run the tests when the script is executed directly.