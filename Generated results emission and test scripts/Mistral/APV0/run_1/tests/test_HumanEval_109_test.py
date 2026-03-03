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

 Here is a unittest test script for the `move_one_ball` function:


import unittest
from HumanEval_109_code import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element_array(self):
        self.assertTrue(move_one_ball([1]))

    def test_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_unsorted_array_with_one_swap(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_unsorted_array_with_multiple_swaps(self):
        self.assertTrue(move_one_ball([5, 4, 3, 1, 2]))

    def test_unsorted_array_not_possible(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_duplicate_values(self):
        self.assertTrue(move_one_ball([1, 1, 2, 3, 4]))
        self.assertTrue(move_one_ball([3, 3, 2, 1, 4]))
        self.assertTrue(move_one_ball([4, 3, 3, 2, 1]))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as empty arrays, single-element arrays, sorted arrays, unsorted arrays with one or multiple swaps, unsorted arrays that cannot be sorted, and arrays with duplicate values.