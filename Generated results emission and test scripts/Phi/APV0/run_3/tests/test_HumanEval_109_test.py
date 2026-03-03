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

 import unittest
from HumanEval_109_code import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]), "An empty array should return True")

    def test_single_element_array(self):
        self.assertTrue(move_one_ball([1]), "A single element array should return True")

    def test_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]), "A sorted array should return True")

    def test_unsorted_array_with_right_shifts(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]), "An array that can be sorted with right shifts should return True")

    def test_unsorted_array_without_right_shifts(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]), "An array that cannot be sorted with right shifts should return False")

    def test_array_with_duplicates(self):
        self.assertTrue(move_one_ball([1, 1, 2, 3, 3]), "An array with duplicates should return True")

    def test_array_with_negative_numbers(self):
        self.assertTrue(move_one_ball([-3, -1, -4, -2, -5]), "An array with negative numbers should return True")

    def test_array_with_zero(self):
        self.assertTrue(move_one_ball([0, 1, 2, 3, 4]), "An array with zero should return True")

    def test_array_with_single_duplicate(self):
        self.assertTrue(move_one_ball([1, 1, 2, 3, 4]), "An array with a single duplicate should return True")

if __name__ == '__main__':
    unittest.main()