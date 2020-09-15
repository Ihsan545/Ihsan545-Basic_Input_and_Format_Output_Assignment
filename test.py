"""
Program: test.py
Author: Ihsanullah Anwary
Last date modified: 09/14/2020
This tests the program for average_score.py.
"""


import unittest

import average_scores

class MyTestCase(unittest.TestCase):  # test class
    def test_average(self):  # Function definition.
        scores = 3
        self.assertEquals(average_scores.average(85, 90, 95, scores), 90)


if __name__ == '__main__':
    unittest.main()  # call the function.