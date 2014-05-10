# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def sum_squares_even(n):
    # TODO: need to write this code!!!
    res = [x**2 for x in range(n+1) if x%2==0]
    return sum(res)

class SumSquaresEvenTests(unittest.TestCase):
    def test_sum_squares_even_basic(self):
        self.assertEqual(sum_squares_even(10),220)
        self.assertEqual(sum_squares_even(5),20)

if __name__ == '__main__':
    unittest.main()