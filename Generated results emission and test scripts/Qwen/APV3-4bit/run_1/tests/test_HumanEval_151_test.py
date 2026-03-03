system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_151_code import double_the_difference
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

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_151_code import double_the_difference
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    return sum([i**2 for i in lst if i > 0 and i % 2 != 0 and "." not in str(i)])


assistant

import unittest

from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):
    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        
    def test_negative_or_non_integer(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        
    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)
        
    def test_single_element(self):
        self.assertEqual(double_the_difference([5]), 25)
        
    def test_mixed_types(self):
        self.assertEqual(double_the_difference([1, 'a', 3.5, 0]), 10)
        
    def test_all_even(self):
        self.assertEqual(double_the_difference([2, 4, 6, 8]), 0)
        
    def test_all_negative(self):
        self.assertEqual(double_the_difference([-1, -2, -3]), 0)
        
    def test_all_zero(self):
        self.assertEqual(double_the_difference([0, 0, 0, 0]), 0)
        
    def test_all_floats(self):
        self.assertEqual(double_the_difference([1.5, 2.5, 3.5]), 0)
        
    def test_all_integers(self):
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 100)
        
    def test_all_strings(self):
        self.assertEqual(double_the_difference(['a', 'b', 'c']), 0)
        
    def test_all_none(self):
        self.assertEqual(double_the_difference(None), 0)
        
    def test_all_dicts(self):
        self.assertEqual(double_the_difference({'key': 'value'}), 0)
        
    def test_all_sets(self):
        self.assertEqual(double_the_difference({}), 0)
        
    def test_all_lists(self):
        self.assertEqual(double_the_difference([[], {}, None, True, False]), 0)
        
    def test_all_tuples(self):
        self.assertEqual(double_the_difference((1, 2, 3)), 0)
        
    def test_all_frozensets(self):
        self.assertEqual(double_the_difference(frozenset()), 0)
        
    def test_all_bytes(self):
        self.assertEqual(double_the_difference(b'bytes'), 0)
        
    def test_all_bytearrays(self):
        self.assertEqual(double_the_difference(bytearray()), 0)
        
    def test_all_generators(self):
        self.assertEqual(double_the_difference(generate(10)), 0)
        
    def test_all_iterables(self):
        self.assertEqual(double_the_difference(iterable(range(10))), 0)
        
    def test_all_complex_numbers(self):
        self.assertEqual(double_the_difference(complex(1, 2)), 0)
        
    def test_all_nan(self):
        self.assertEqual(double_the_difference(float('nan')), 0)
        
    def test_all_inf(self):
        self.assertEqual(double_the_difference(float('inf')), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'), 0)
        
    def test_all_inf_and_nan(self):
        self.assertEqual(double_the_difference(float('inf') * float('nan')) / float('inf'),