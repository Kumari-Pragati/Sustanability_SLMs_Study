system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_105_code import by_length
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1, 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """

    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arrassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_by_length(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1, 55]), ["One"])
        self.assertEqual(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"])
        self.assertEqual(by_length([1, 1, 1, 1, 1]), ["One", "One", "One", "One", "One"])
        self.assertEqual(by_length([2, 2, 2, 2, 2]), ["Two", "Two", "Two", "Two", "Two"])
        self.assertEqual(by_length([3, 3, 3, 3, 3]), ["Three", "Three", "Three", "Three", "Three"])
        self.assertEqual(by_length([4, 4, 4, 4, 4]), ["Four", "Four", "Four", "Four", "Four"])
        self.assertEqual(by_length([5, 5, 5, 5, 5]), ["Five", "Five", "Five", "Five", "Five"])
        self.assertEqual(by_length([6, 6, 6, 6, 6]), ["Six", "Six", "Six", "Six", "Six"])
        self.assertEqual(by_length([7, 7, 7, 7, 7]), ["Seven", "Seven", "Seven", "Seven", "Seven"])
        self.assertEqual(by_length([8, 8, 8, 8, 8]), ["Eight", "Eight", "Eight", "Eight", "Eight"])
        self.assertEqual(by_length([9, 9, 9, 9, 9]), ["Nine", "Nine", "Nine", "Nine", "Nine"])

if __name__ == '__main__':
    unittest.main()