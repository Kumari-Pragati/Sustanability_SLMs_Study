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
   - Include from HumanEval_148_code import bf
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
2. Include: from HumanEval_148_code import bf
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return planet_names[planet1_index + 1: planet2_index]
    else:
        return planet_names[planet2_index + 1: planet1_index]


assistant

import unittest

# Importing the function from the given context
from HumanEval_148_code import bf

class TestBf(unittest.TestCase):
    
    # Test case for positive numbers
    def test_positive_planets(self):
        result = bf("Jupiter", "Neptune")
        expected_result = ("Saturn", "Uranus")
        self.assertCountEqual(result, expected_result)
        
    # Test case for negative numbers
    def test_negative_planets(self):
        result = bf("-Jupiter", "-Neptune")
        expected_result = ("-Venus", "-Earth", "-Mars", "-Jupiter", "-Saturn")
        self.assertCountEqual(result, expected_result)
        
    # Test case for empty list
    def test_empty_input(self):
        result = bf("", "")
        expected_result = ()
        self.assertEqual(result, expected_result)
        
    # Test case for incorrect input
    def test_incorrect_input(self):
        result = bf("Mercury", "Pluto")
        expected_result = ()
        self.assertEqual(result, expected_result)
        
    # Test case for same planet name
    def test_same_planet_name(self):
        result = bf("Earth", "Earth")
        expected_result = ()
        self.assertEqual(result, expected_result)
        
    # Test case for valid input
    def test_valid_input(self):
        result = bf("Earth", "Mars")
        expected_result = ("Venus", "Mars")
        self.assertCountEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()