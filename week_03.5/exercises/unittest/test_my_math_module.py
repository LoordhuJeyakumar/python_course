# test_my_math_module.py
import unittest # Import unittest module
from my_math_module import add # Import the function to be tested

class TestAddFunction(unittest.TestCase): # 1. Define a test class inheriting from unittest.TestCase

    def test_add_positive_numbers(self): # 2. Test method name starts with 'test_'
        self.assertEqual(add(2, 3), 5) # 3. Assertion: Check if add(2, 3) is equal to 5

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -2), 3)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)

if __name__ == '__main__': # Standard way to run tests when the script is executed directly
    unittest.main()