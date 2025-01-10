import unittest
import numpy as np
import pandas as pd
from Function2Test import fitline

class TestFunction(unittest.TestCase):

    def test_slope(self):
        result = fitline('gender-wage-gap-UK.csv')
        slope = result[0]
        self.assertAlmostEqual(slope,-0.613, 2)
    
    def test_intercept(self):
        result = fitline('gender-wage-gap-UK.csv')
        intercept = result[1]
        self.assertAlmostEqual(intercept,1251.80, 2)

    def test_filetype(self):
        result = fitline('gender-wage-gap-UK.numbers')
        self.assertEqual(result, "Please enter the correct file type and try again")
    
    def test_columns(self):
        data1 = pd.read_csv("gender-wage-gap-UK.csv")
        data2 = pd.read_csv("female-labor-force-participation-UK.csv")
        result = [len(data1.columns),len(data2.columns)]
        self.assertEqual(result,[2,2])
    
    def test_corrolation_wagegap(self):
        data = pd.read_csv("gender-wage-gap-UK.csv")
        result = data.iloc[:,0].corr(data.iloc[:,1])
        self.assertLessEqual(result,0.7)

    def test_corrolation_laborforce(self):
        data = pd.read_csv("female-labor-force-participation-UK.csv")
        result = data.iloc[:,0].corr(data.iloc[:,1])
        self.assertGreaterEqual(result,0.7)

if __name__ == '__main__':
    unittest.main()