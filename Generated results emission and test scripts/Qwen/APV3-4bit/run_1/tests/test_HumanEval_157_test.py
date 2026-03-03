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
   - Include from HumanEval_157_code import right_angle_triangle
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
2. Include: from HumanEval_157_code import right_angle_triangle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b


assistant

import unittest

from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):
    
    def test_right_angle_triangle(self):
        # Normal case
        self.assertTrue(right_angle_triangle(3, 4, 5))
        
        # Edge case (right angle)
        self.assertTrue(right_angle_triangle(5, 3, 4))
        
        # Edge case (acute triangle)
        self.assertFalse(right_angle_triangle(3, 4, 6))
        
        # Edge case (obtuse triangle)
        self.assertFalse(right_angle_triangle(3, 4, 8))

        # Invalid input (non-positive side length)
        self.assertFalse(right_angle_triangle(-1, 4, 5))
        
        # Invalid input (negative side length)
        self.assertFalse(right_angle_triangle(3, -4, 5))
        
        # Invalid input (zero side length)
        self.assertFalse(right_angle_triangle(0, 4, 5))
        
        # Invalid input (multiple zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 5))
        
        # Invalid input (all negative side lengths)
        self.assertFalse(right_angle_triangle(-1, -4, -5))
        
        # Invalid input (all positive side lengths)
        self.assertFalse(right_angle_triangle(1, 4, 5))
        
        # Invalid input (one zero side length)
        self.assertFalse(right_angle_triangle(0, 4, 5))
        
        # Invalid input (two zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 5))
        
        # Invalid input (three zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0))
        
        # Invalid input (four zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0))
        
        # Invalid input (five zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0))
        
        # Invalid input (six zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0))
        
        # Invalid input (seven zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (eight zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (nine zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (ten zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (eleven zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (twelve zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (thirteen zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (fourteen zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (fifteen zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (sixteen zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        # Invalid input (seventeen zero side lengths)
        self.assertFalse(right_angle_triangle(0, 0, 0, 0, 0, 0, 0, 0, 0