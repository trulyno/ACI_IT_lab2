#!/usr/bin/env python3
"""
A simple Python calculator app with basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Main function to demonstrate the calculator."""
    print("Simple Python Calculator")
    print("========================")
    
    # Example calculations
    a, b = 10, 5
    
    print(f"Adding {a} + {b} = {add(a, b)}")
    print(f"Subtracting {a} - {b} = {subtract(a, b)}")
    print(f"Multiplying {a} * {b} = {multiply(a, b)}")
    print(f"Dividing {a} / {b} = {divide(a, b)}")
    
    return "Calculator demo completed successfully!"

if __name__ == "__main__":
    result = main()
    print(result)