user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        return planet_names[planet2_index + 1: planet1_index]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_148_code import bf

class TestBF(unittest.TestCase):

    def test_bf(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
        self.assertEqual(bf("Mars", "Mars"), ())
        self.assertEqual(bf("Jupiter", "Jupiter"), ())
        self.assertEqual(bf("Invalid", "Neptune"), ())
        self.assertEqual(bf("Jupiter", "Invalid"), ())

if __name__ == '__main__':
    unittest.main()


This script includes five test cases:

- The first test case checks if the function returns the correct planets when the input planets are "Jupiter" and "Neptune".
- The second test case checks if the function returns the correct planets when the input planets are "Earth" and "Mercury".
- The third test case checks if the function returns the correct planets when the input planets are "Mercury" and "Uranus".
- The fourth and fifth test cases check if the function returns an empty tuple when the input planets are the same or invalid.