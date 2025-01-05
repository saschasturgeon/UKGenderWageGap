import unittest
from Function2Test import fitline

class TestFunction(unittest.TestCase):

    def test_filetype(self):
        result = fitline('gender-wage-gap-UK.numbers')
        self.assertEqual(result, "Please enter the correct file type and try again")

    def check_stats(self):
        result = fitline('gender-wage-gap-UK.csv')
        self.assertEqual(result,"-0.6130347593582889, 1251.7967914438502")

if __name__ == '__main__':
    unittest.main()