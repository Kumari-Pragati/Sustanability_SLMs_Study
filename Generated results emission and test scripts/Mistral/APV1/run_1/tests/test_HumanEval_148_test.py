You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `bf`. The test cases cover various scenarios including valid planet names, invalid planet names, and cases where the planets are the same.


import unittest
from HumanEval_148_code import bf

class TestBF(unittest.TestCase):

    def test_valid_planets(self):
        self.assertCountEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertCountEqual(bf("Earth", "Mercury"), ("Venus",))
        self.assertCountEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_invalid_planets(self):
        self.assertCountEqual(bf("Pluto", "Neptune"), ())
        self.assertCountEqual(bf("Mars", "Pluto"), ())
        self.assertCountEqual(bf("Earth", "Moon"), ())

    def test_same_planets(self):
        self.assertCountEqual(bf("Earth", "Earth"), ())
        self.assertCountEqual(bf("Mercury", "Mercury"), ())

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods:

1. `test_valid_planets`: Tests the function with valid planet names.
2. `test_invalid_planets`: Tests the function with invalid planet names.
3. `test_same_planets`: Tests the function when the planets are the same.

Each test method uses the `assertCountEqual` function to compare the expected output with the actual output of the `bf` function. If the outputs match, the test passes; otherwise, it fails.