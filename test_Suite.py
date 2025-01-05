import unittest
import numpy as np
from Function2Test import fitline

class TestFunction(unittest.TestCase):

    def test_stats(self):
        result = fitline('gender-wage-gap-UK.csv')
        self.assertEqual(result,(np.float64(-0.6130347593582702), np.float64(1251.796791443812)))

    def test_filetype(self):
        result = fitline('gender-wage-gap-UK.numbers')
        self.assertEqual(result, "Please enter the correct file type and try again")

if __name__ == '__main__':
    unittest.main()