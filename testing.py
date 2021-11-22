#!/usr/bin/python3

import unittest
import math

from functions import *

class TestCircle(unittest.TestCase):
    def test_multiply(self):
        testCases = {
           (2, 3) : 6,
           (0, 2) : 0,
           (2, -1) : -2
        }
        for case in testCases:
            self.assertEqual(multiply(case[0], case[1]), testCases[case])

    def test_square(self):
        testCases = {
            2 : 4,
            0 : 0,
            1 : 1,
            -1 : 1
        }
        for case in testCases:
            self.assertEqual(square(case), testCases[case])
    
    def test_circle_perimeter(self):
        testCases = {
            2 : 2*math.pi*2,
            0 : 0,
            -1 : 0
        }
        for case in testCases:
            self.assertEqual(circle_perimeter(case), testCases[case])
    
    def test_circle_area(self):
        testCases = {
            2 : math.pi*pow(2,2),
            0 : 0,
            -1 : 0
        }
        for case in testCases:
            self.assertEqual(circle_area(case), testCases[case])

if __name__ == '__main__':
    unittest.main()