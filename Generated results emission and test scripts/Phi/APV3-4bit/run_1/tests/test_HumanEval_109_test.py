### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_109_code import move_one_ball
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

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
        self.assertTrue(move_one_ball([]), "Empty array should return True")

    def test_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]), "Sorted array should return True")

    def test_unsorted_array_with_possible_sort(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]), "Array with possible sort should return True")

    def test_unsorted_array_with_no_possible_sort(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]), "Array with no possible sort should return False")

    def test_array_with_single_element(self):
        self.assertTrue(move_one_ball([1]), "Array with single element should return True")

    def test_array_with_duplicate_elements(self):
        self.assertTrue(move_one_ball([3, 3, 2, 1, 4]), "Array with duplicate elements should return True")

    def test_array_with_negative_numbers(self):
        self.assertTrue(move_one_ball([-3, -1, -4, -2, -5]), "Array with negative numbers should return True")

    def test_array_with_zero(self):
        self.assertTrue(move_one_ball([0]), "Array with zero should return True")

    def test_array_with_all_same_elements(self):
        self.assertTrue(move_one_ball([5, 5, 5, 5, 5]), "Array with all same elements should return True")

    def test_array_with_large_numbers(self):
        self.assertTrue(move_one_ball([1000000, 2000000, 3000000, 4000000, 5000000]), "Array with large numbers should return True")

if __name__ == '__main__':
    unittest.main()