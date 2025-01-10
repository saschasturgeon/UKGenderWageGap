import unittest
import numpy as np
import pandas as pd
from Function2Test import fitline

class TestFunction(unittest.TestCase): 

    def test_slope(self): # checks if the slope calculated is correct
        result = fitline('gender-wage-gap-UK.csv')
        slope = result[0]
        self.assertAlmostEqual(slope,-0.613, 2)
    
    def test_intercept(self): # checks if the intercept calculated is correct
        result = fitline('gender-wage-gap-UK.csv')
        intercept = result[1]
        self.assertAlmostEqual(intercept,1251.80, 2)

    def test_filetype(self): # checks that the file type is a csv
        result = fitline('gender-wage-gap-UK.numbers')
        self.assertEqual(result, "Please enter the correct file type and try again")
    
    def test_columns(self): # checks that the data has two columns
        data1 = pd.read_csv("gender-wage-gap-UK.csv")
        data2 = pd.read_csv("female-labor-force-participation-UK.csv")
        result = [len(data1.columns),len(data2.columns)]
        self.assertEqual(result,[2,2])
    
    def test_corrolation_wagegap(self): # checks the data points are statistically significant
        data = pd.read_csv("gender-wage-gap-UK.csv")
        result = data.iloc[:,0].corr(data.iloc[:,1])
        self.assertLessEqual(result,0.7)

    def test_corrolation_laborforce(self): # checks the data points are statistically significant
        data = pd.read_csv("female-labor-force-participation-UK.csv")
        result = data.iloc[:,0].corr(data.iloc[:,1])
        self.assertGreaterEqual(result,0.7)

    def test_datapoints_wagegap(self): # checks there are enough data points to create a meaningful model fit
        data = pd.read_csv("gender-wage-gap-UK.csv")
        rows = len(data)
        self.assertGreaterEqual(rows,10)

    def test_datapoints_laborforce(self): # checks there are enough data points to create a meaningful model fit
        data = pd.read_csv("female-labor-force-participation-UK.csv")
        rows = len(data)
        self.assertGreaterEqual(rows,10)

if __name__ == '__main__':
    unittest.main()