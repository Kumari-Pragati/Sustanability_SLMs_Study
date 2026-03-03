user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_by_length(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1, 55]), ['One'])
        self.assertEqual(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"])
        self.assertEqual(by_length([1, 1, 1, 1, 1]), ["One", "One", "One", "One", "One"])
        self.assertEqual(by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"])
        self.assertEqual(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"])

if __name__ == '__main__':
    unittest.main()


This script includes 7 test cases to cover different scenarios, including an empty array, an array with a single element, an array with a mix of numbers, and an array with all numbers between 1 and 9. The `assertEqual` method is used to compare the output of the `by_length` function with the expected output.