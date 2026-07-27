import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        result = greet("AnjuKudhail")
        self.assertIn("AnjuKudhail", result)
        self.assertIn("INFO 52170", result)

    def test_farewell(self):
        result = farewell("AnjuKudhail")
        self.assertIn("AnjuKudhail", result)

if __name__ == "__main__":
    unittest.main()
