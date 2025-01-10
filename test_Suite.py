import unittest
import numpy as np
from Function2Test import fitline

class TestFunction(unittest.TestCase):

    def test_stats(self):
        result = fitline('gender-wage-gap-UK.csv')
        slope = result[0]
        self.assertAlmostEqual(slope,-0.613, 2)

    def test_filetype(self):
        result = fitline('gender-wage-gap-UK.numbers')
        self.assertEqual(result, "Please enter the correct file type and try again")

if __name__ == '__main__':
    unittest.main()