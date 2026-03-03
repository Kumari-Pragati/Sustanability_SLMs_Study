You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the provided `bf` function:


import unittest
from HumanEval_148_code import bf

class TestBF(unittest.TestCase):

    def test_bf_valid_planets(self):
        self.assertCountEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertCountEqual(bf("Earth", "Mercury"), ("Venus"))
        self.assertCountEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_bf_invalid_planets(self):
        self.assertCountEqual(bf("Pluto", "Neptune"), ())
        self.assertCountEqual(bf("Mars", "Mars"), ())
        self.assertCountEqual(bf("Mercury", "Pluto"), ())

    def test_bf_same_planets(self):
        self.assertCountEqual(bf("Mercury", "Mercury"), ())
        self.assertCountEqual(bf("Neptune", "Neptune"), ())

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases for valid planet pairs, two test cases for invalid planet pairs, and two test cases for the same planet. The `assertCountEqual` function is used to compare the expected and actual results.