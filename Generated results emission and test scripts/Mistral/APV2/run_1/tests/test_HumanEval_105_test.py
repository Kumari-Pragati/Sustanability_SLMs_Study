You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
      arr = [1, -1 , 55] 
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
    return new_arr

 Here is a comprehensive unittest test suite for the provided Python function `by_length`. The test suite includes various test cases to cover different scenarios, such as empty arrays, arrays with numbers outside the range of 1 to 9, and arrays with a mix of numbers.


import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_array_with_numbers_outside_range(self):
        self.assertEqual(by_length([1, -1, 55]), ['One'])
        self.assertEqual(by_length([10, 20, 30]), [])
        self.assertEqual(by_length([0]), [])

    def test_array_with_numbers_in_range(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), [
            'Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'
        ])
        self.assertEqual(by_length([9, 1, 2]), ['Nine', 'One', 'Two'])
        self.assertEqual(by_length([1, 9]), ['One', 'Nine'])
        self.assertEqual(by_length([4, 5, 6]), ['Four', 'Five', 'Six'])

    def test_array_with_duplicates(self):
        self.assertEqual(by_length([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]), [
            'One', 'One', 'Two', 'Two', 'Three', 'Three', 'Four', 'Four', 'Five', 'Five', 'Six', 'Six', 'Seven', 'Seven', 'Eight', 'Eight', 'Nine', 'Nine'
        ])

if __name__ == '__main__':
    unittest.main()


This test suite covers various edge cases and ensures that the `by_length` function works as expected.