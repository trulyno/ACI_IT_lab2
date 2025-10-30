import unittest
from app import greet, add


class TestApp(unittest.TestCase):
    """Test cases for the app module."""

    def test_greet(self):
        """Test the greet function."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("World"), "Hello, World!")

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10, -5), 5)


if __name__ == "__main__":
    unittest.main()
