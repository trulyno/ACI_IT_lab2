#!/usr/bin/env python3
"""
Test suite for the simple calculator app.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10.5, 2.5), 13.0)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10.5, 2.5), 8.0)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(10, 4), 2.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()