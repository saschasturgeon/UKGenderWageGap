import unittest
from Function2Test import isnumber

class TestFunction(unittest.TestCase):
    def test_positive_number(self):
        result = isnumber(4)
        self.assertEqual(result, "Positive")

    def test_negative_number(self):
        result = isnumber(-14)
        self.assertEqual(result, "Negative")
    
    def test_zero(self):
        result = isnumber(0)
        self.assertEqual(result, "Neither")
    
    def test_is_a_number(self):
        result = isnumber("fhweuh")
        self.assertEqual(result,"Not a number")

if __name__ == '__main__':
    unittest.main()
