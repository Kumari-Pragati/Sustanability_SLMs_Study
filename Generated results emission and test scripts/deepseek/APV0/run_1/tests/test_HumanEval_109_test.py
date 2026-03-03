You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_109_code import move_one_ball
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """

    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    my_arr = []

    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[0:min_index]
    for i in range(len(arr)):
        if my_arr[i] != sorted_array[i]:
            return False
    return True


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_109_code import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_one_shift_possible(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_one_shift_not_possible(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_multiple_shifts_possible(self):
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]))

    def test_multiple_shifts_not_possible(self):
        self.assertFalse(move_one_ball([5, 2, 3, 1, 4]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([1]))

    def test_duplicate_elements(self):
        self.assertTrue(move_one_ball([1, 1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()


This script includes a series of test cases to cover all possible scenarios. It tests the function with empty arrays, already sorted arrays, arrays that can be sorted with one right shift, arrays that cannot be sorted with one right shift, arrays that can be sorted with multiple right shifts, arrays that cannot be sorted with multiple right shifts, arrays with a single element, and arrays with duplicate elements.