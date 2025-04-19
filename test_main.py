import unittest
from main import greet

class TestGreet(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_non_str(self):
        with self.assertRaises(ValueError):
            greet(123)

if __name__ == "__main__":
    unittest.main()
