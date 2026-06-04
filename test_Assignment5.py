import unittest
from Assignment5 import fahrenheit_to_celsius, fibonacci

class TestAssignment5(unittest.TestCase):

    # Test Fahrenheit to Celsius conversion
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37, places=1)

    # Test Fibonacci function
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

        # Test negative input raises ValueError
        with self.assertRaises(ValueError):
            fibonacci(-1)

        # Test non-integer input raises TypeError
        with self.assertRaises(TypeError):
            fibonacci(3.5)


if __name__ == "__main__":
    unittest.main()