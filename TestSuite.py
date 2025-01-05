import unittest
from Function2Test import fitline

class TestFunction(unittest.TestCase):
    def test_filetype(self):
        result = fitline('gender-wage-gap-UK.numbers')
        self.assertEqual(result, "Please enter the correct file type and try again")

if __name__ == '__main__':
    unittest.main()
