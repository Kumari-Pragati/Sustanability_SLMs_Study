user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_81_code import unknown_function
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

    letter_grade = []
        for gpa in grades:
            if gpa == 4.0:
                letter_grade.append("A+")
            elif gpa > 3.7:
                letter_grade.append("A")
            elif gpa > 3.3:
                letter_grade.append("A-")
            elif gpa > 3.0:
                letter_grade.append("B+")
            elif gpa > 2.7:
                letter_grade.append("B")
            elif gpa > 2.3:
                letter_grade.append("B-")
            elif gpa > 2.0:
                letter_grade.append("C+")
            elif gpa > 1.7:
                letter_grade.append("C")
            elif gpa > 1.3:
                letter_grade.append("C-")
            elif gpa > 1.0:
                letter_grade.append("D+")
            elif gpa > 0.7:
                letter_grade.append("D")
            elif gpa > 0.0:
                letter_grade.append("D-")
            else:
                letter_grade.append("E")
        return letter_gradeassistant

Here is the unittest test script for the `numerical_letter_grade` function:

import unittest
from HumanEval_81_code import unknown_function  # Replace with the actual name of the module

class TestNumericalLetterGrade(unittest.TestCase):
    def test_perfect_score(self):
        grades = [4.0]
        expected_output = ['A+']
        self.assertEqual(unknown_function(grades), expected_output)

    def test_high_grade(self):
        grades = [3.8]
        expected_output = ['A']
        self.assertEqual(unknown_function(grades), expected_output)

    def test_low_grade(self):
        grades = [1.9]
        expected_output = ['D+']
        self.assertEqual(unknown_function(grades), expected_output)

    def test_multiple_grades(self):
        grades = [4.0, 3, 1.7, 2, 3.5]
        expected_output = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(unknown_function(grades), expected_output)

    def test_edge_cases(self):
        grades = [0.0]
        expected_output = ['E']
        self.assertEqual(unknown_function(grades), expected_output)

        grades = [4.1]
        expected_output = ['A+']
        self.assertEqual(unknown_function(grades), expected_output)

    def test_invalid_input(self):
        grades = ['a']
        with self.assertRaises(TypeError):
            unknown_function(grades)

        grades = [4.0, 'b', 1.7]
        with self.assertRaises(TypeError):
            unknown_function(grades)

if __name__ == '__main__':
    unittest.main()

This test script covers various scenarios, including:

* Perfect score (4.0)
* High grade (3.8)
* Low grade (1.9)
* Multiple grades
* Edge cases (0.0 and 4.1)
* Invalid input (non-numeric values)

Note that you'll need to replace `unknown_function` with the actual name of the module that contains the `numerical_letter_grade` function.