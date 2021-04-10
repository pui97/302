import unittest
import test

class CalculatorTestCase(unittest.TestCase):


    def test_aaron(self):
        
        result = test.single_calculate(600000 )
        self.assertEqual(result, 58500)

        
    def test_aaron1(self):
        
        result = test.married_single_calculate(600000 ,400000 )
        self.assertEqual(result, 83000)

    def test_aaron2(self):
        
        result = test.married_calculate(600000 ,400000 )
        self.assertEqual(result, 101000)

    def test_aaron3(self):
        
        result = test.suggestion(83000,101000)
        self.assertEqual(result, "suggest use separate Assesment")


if __name__ == '__main__':
    unittest.main()
