system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_147_code import get_max_triples
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)


assistant

import unittest

# Function to be tested
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples(self):
        # Test case 1
        self.assertEqual(get_max_triples(5), 1)
        
        # Test case 2
        self.assertEqual(get_max_triples(6), 1)
        
        # Test case 3
        self.assertEqual(get_max_triples(7), 1)
        
        # Test case 4
        self.assertEqual(get_max_triples(8), 1)
        
        # Test case 5
        self.assertEqual(get_max_triples(9), 1)
        
        # Test case 6
        self.assertEqual(get_max_triples(10), 1)
        
        # Test case 7
        self.assertEqual(get_max_triples(11), 1)
        
        # Test case 8
        self.assertEqual(get_max_triples(12), 1)
        
        # Test case 9
        self.assertEqual(get_max_triples(13), 1)
        
        # Test case 10
        self.assertEqual(get_max_triples(14), 1)
        
        # Test case 11
        self.assertEqual(get_max_triples(15), 1)
        
        # Test case 12
        self.assertEqual(get_max_triples(16), 1)
        
        # Test case 13
        self.assertEqual(get_max_triples(17), 1)
        
        # Test case 14
        self.assertEqual(get_max_triples(18), 1)
        
        # Test case 15
        self.assertEqual(get_max_triples(19), 1)
        
        # Test case 16
        self.assertEqual(get_max_triples(20), 1)
        
        # Test case 17
        self.assertEqual(get_max_triples(21), 1)
        
        # Test case 18
        self.assertEqual(get_max_triples(22), 1)
        
        # Test case 19
        self.assertEqual(get_max_triples(23), 1)
        
        # Test case 20
        self.assertEqual(get_max_triples(24), 1)
        
        # Test case 21
        self.assertEqual(get_max_triples(25), 1)
        
        # Test case 22
        self.assertEqual(get_max_triples(26), 1)
        
        # Test case 23
        self.assertEqual(get_max_triples(27), 1)
        
        # Test case 24
        self.assertEqual(get_max_triples(28), 1)
        
        # Test case 25
        self.assertEqual(get_max_triples(29), 1)
        
        # Test case 26
        self.assertEqual(get_max_triples(30), 1)
        
        # Test case 27
        self.assertEqual(get_max_triples(31), 1)
        
        # Test case 28
        self.assertEqual(get_max_triples(32), 1)
        
        # Test case 29
        self.assertEqual(get_max_triples(33), 1)
        
        # Test case 30
        self.assertEqual(get_max_triples(34), 1)
        
        # Test case 31
        self.assertEqual(get_max_triples(35), 1)
        
        # Test case 32
        self.assertEqual(get_max_triples(36), 1)
        
        # Test case 33
        self.assertEqual(get_max_triples(37), 1)
        
        # Test case 34
        self.assertEqual(get_max_triples(38), 1)
        
        # Test case 35
        self.assertEqual(get_max_triples(39), 1)
        
        # Test case 36
        self.assertEqual(get_max_triples(40), 1)
        
        # Test case 37
        self.assertEqual(get_max_triples(41), 1)
        
        # Test case 38
        self.assertEqual(get_max_triples(42), 1)
        
        # Test case 39
        self.assertEqual(get_max_triples(43), 1)
        
        # Test case 40
        self.assertEqual(get_max_triples(44), 1)
        
        # Test case 41
        self.assertEqual(get_max_triples(45), 1)
        
        # Test case 42
        self.assertEqual(get_max_triples(46), 1)
        
        # Test case 43
        self.assertEqual(get_max_triples(47), 1)
        
        # Test case