You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_148_code import bf

class TestBF(unittest.TestCase):

    def test_valid_planets(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_invalid_planet1(self):
        self.assertEqual(bf("InvalidPlanet", "Neptune"), ())

    def test_invalid_planet2(self):
        self.assertEqual(bf("Jupiter", "InvalidPlanet"), ())

    def test_same_planets(self):
        self.assertEqual(bf("Earth", "Earth"), ())

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_valid_planets`: Tests the function with valid planet names.
2. `test_invalid_planet1`: Tests the function with an invalid planet name for planet1.
3. `test_invalid_planet2`: Tests the function with an invalid planet name for planet2.
4. `test_same_planets`: Tests the function with the same planet name for both planet1 and planet2.

Each test case checks if the function's output matches the expected output. If the function's output is different, the test case will fail, indicating that the function does not behave as expected.