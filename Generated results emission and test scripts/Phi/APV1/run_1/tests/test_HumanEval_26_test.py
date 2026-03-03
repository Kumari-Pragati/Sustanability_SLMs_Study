You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_26_code import remove_duplicates
from typing import List


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        # Test case 1: Basic functionality
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

        # Test case 2: Empty list
        self.assertEqual(remove_duplicates([]), [])

        # Test case 3: List with all elements being duplicates
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

        # Test case 4: List with no duplicates
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

        # Test case 5: List with negative numbers
        self.assertEqual(remove_duplicates([-1, -2, -3, -2, -1]), [-1, -3])

        # Test case 6: List with mixed types
        with self.assertRaises(TypeError):
            remove_duplicates([1, "2", 3, "3", 4])

        # Test case 7: List with None values
        with self.assertRaises(TypeError):
            remove_duplicates([1, None, 3, None, 4])

        # Test case 8: List with floating-point numbers
        self.assertEqual(remove_duplicates([1.0, 2.5, 3.0, 2.5, 4.0]), [1.0, 3.0, 4.0])

        # Test case 9: List with complex numbers
        with self.assertRaises(TypeError):
            remove_duplicates([1+2j, 2+3j, 3+4j, 2+3j])

        # Test case 10: List with custom objects
        class CustomObject:
            def __init__(self, value):
                self.value = value

        def custom_object_hash(obj):
            return obj.value

        custom_objects = [CustomObject(1), CustomObject(2), CustomObject(2), CustomObject(3)]
        self.assertEqual(remove_duplicates(custom_objects, key=custom_object_hash), [CustomObject(1), CustomObject(3)])


if __name__ == '__main__':
    unittest.main()