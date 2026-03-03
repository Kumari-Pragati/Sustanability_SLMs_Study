system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Function to be tested
from HumanEval_81_code import unknown_function

class TestNumericalLetterGrade(unittest.TestCase):

    def test_grades(self):
        # Test cases to verify the correctness of the function
        self.assertEqual(unknown_function([4.0, 3, 1.7, 2, 3.5]), ["A+", "B", "C-", "C", "A-"])
        self.assertEqual(unknown_function([3.9, 2.9, 1.6, 1.1, 0.5]), ["B-", "C-", "D-", "D-", "E"])
        self.assertEqual(unknown_function([4.5, 3.5, 2.5, 1.5, 0.5]), ["A+", "A-", "B+", "B-", "C-"])
        self.assertEqual(unknown_function([4.0, 3.0, 2.0, 1.0, 0.0]), ["A+", "A", "B", "C", "D"])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `numerical_letter_grade` function works as expected across different input scenarios.