You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
        return letter_grade


### Response:
Here is a unittest script for the given function:


import unittest

# Assuming the function is defined in a file named 'HumanEval_81_code.py'
from HumanEval_81_code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_all_grades(self):
        grades = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
        expected_output = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_repeated_grades(self):
        grades = [3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0, 0.0]
        expected_output = ['B+', 'B+', 'C+', 'C+', 'D+', 'D+', 'D', 'D']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_high_grade(self):
        grades = [4.5, 3.8, 2.4, 1.1]
        expected_output = ['A+', 'A', 'B', 'C+']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_low_grade(self):
        grades = [-1, 0, 0.5]
        expected_output = ['E', 'D-', 'D-']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_empty_list(self):
        grades = []
        expected_output = []
        self.assertEqual(numerical_letter_grade(grades), expected_output)

if __name__ == '__main__':
    unittest.main()


This script includes five test cases:

1. `test_all_grades`: Tests the function with a list of grades that covers all the ranges.
2. `test_repeated_grades`: Tests the function with a list of grades that includes repeated values.
3. `test_high_grade`: Tests the function with a list of grades that includes values above the maximum range.
4. `test_low_grade`: Tests the function with a list of grades that includes values below the minimum range.
5. `test_empty_list`: Tests the function with an empty list.

Please note that the function `numerical_letter_grade` should be defined in a file named `HumanEval_81_code.py` in the same directory as the test script.