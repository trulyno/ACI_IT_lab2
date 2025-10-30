def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def main():
    """Main function to demonstrate the app."""
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
