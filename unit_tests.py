import unittest, sys, os
import statistics as st

list_1 = [3, 6, 3, 5, 7]

def average(values):

    return sum(values) / len(values)

def median(values):

    if len(values) % 2 == 0:
        pass

    else:
        pass 

def mode(values):

    if 

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 2), 4.33)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() # Calling from cmd invokes all tests
